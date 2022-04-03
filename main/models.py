import uuid
from django.apps import apps
from django.db import models, transaction
from django.forms import ValidationError
from users.models import *
from django.db.models import Q


def directory_path_image(instance, filename):
    # путь, куда будет осуществлена загрузка MEDIA_ROOT/user_<id>/<filename>
    return 'images/{0}/{1}'.format(instance.reg_global.pk, filename)


'''Дефолтный класс для всех справочников'''
class spr_default(models.Model):
    guid_update = models.UUIDField(blank=True, default=uuid.uuid4)

    reg_global = models.ForeignKey(reg_Global, on_delete=models.PROTECT, verbose_name = 'Global ID')
    deleted = models.BooleanField(default=False, verbose_name="Блокировка")
    code = models.CharField(max_length=11, verbose_name='Код', blank=True, default='', help_text='')
 
    class Meta:
        abstract = True
        get_latest_by = 'code'
 
    def __str__(self):
        return self.name

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._guid_update = self.guid_update

    def text_code(self):
        return '%s-%s' % (self.reg_global.pref, self.code.rjust(8, '0'))
    text_code.short_description = 'Код'        

    def visible_colum_list(self):
        arr=[]
        arr.append({'id': 'text_code()', 'name': self.text_code.short_description,'width':'1%'})        
        arr.append({'id': 'name', 'name': self._meta.get_field('name').verbose_name,'width':'99%'})
        return arr
 
    def save(self, *args, **kwargs):
        if self.pk and self.guid_update != self._guid_update:              
            raise ValidationError('Не удается сохранить изменения. Данные уже были кем то изменены.') 
        if not self.code:
            try:
                el_obj = apps.get_model('main', self._meta.model_name).objects.filter(reg_global=self.reg_global).latest('code')                 
                self.code = str(int(el_obj.code)+1).rjust(8, '0')
            except:
                self.code = str(1).rjust(8, '0')
        self.guid_update = uuid.uuid4()
        super().save(*args, **kwargs) 

    def tempForms(self):
        return {}


class spr_typemenu(spr_default):
    name = models.CharField(max_length=50, verbose_name='Наименование')

    class Meta:
        verbose_name = 'Тип меню'
        verbose_name_plural = 'Справочник: \"Типы меню\"'


class spr_zaly(spr_default):
    name = models.CharField(max_length=50, verbose_name='Наименование')

    class Meta:
        verbose_name = 'Зал'
        verbose_name_plural = 'Справочник: \"Залы\"'


class spr_company(spr_default):
    TYPE = (
        (0, "Юридическое лицо"),
        (1, "Обособленное подразделение"),
        (2, "Индивидуальный предприниматель"),
    )    
    type_company = models.IntegerField(choices=TYPE, default=0, verbose_name='Вид юр.лица')

    parent = models.ForeignKey('spr_company', null=True, blank=True, on_delete=models.PROTECT,verbose_name='Головная организация')

    name = models.CharField(max_length=50, verbose_name='Наименование')
    name_full = models.CharField(max_length=250, blank=True, default='', verbose_name='Полное наименование')
    inn = models.CharField(max_length=12, blank=True, default='', verbose_name='ИНН')
    kpp = models.CharField(max_length=9, blank=True, default='', verbose_name='КПП')
    addres_u = models.CharField(max_length=250, blank=True, default='',verbose_name='Юридический адрес')
    addres_f = models.CharField(max_length=250, blank=True, default='', verbose_name='Фактический адрес')
    addres_p = models.CharField(max_length=250, blank=True, default='', verbose_name='Почтовый адрес')
    pref = models.CharField(max_length=2, verbose_name='Префикс документов')

    class Meta:
        verbose_name='Организация'
        verbose_name_plural='Справочник: \"Организации\"'

    def visible_colum_list(self):
        arr=super().visible_colum_list(self);
        arr.append({'id': 'pref', 'name': 'Префикс','width':'99%'})
        return arr


class spr_object(spr_default):
    owner = models.ForeignKey(spr_company, on_delete=models.PROTECT, verbose_name = 'Головная организация')
    name = models.CharField(max_length=50, verbose_name='Наименование')

    tabl_spr_typemenu = models.ManyToManyField('spr_typemenu', blank=True)
    tabl_spr_zaly = models.ManyToManyField('spr_zaly', blank=True)

    class Meta:
        verbose_name='Подразделение'
        verbose_name_plural='Справочник: \"Подразделения\"' 


class spr_fizlitso(spr_default):
    TYPE_POL = (
        (0, "Мужской"),
        (1, "Женский"),
        )

    name = models.CharField(max_length=100, blank=True, default='', verbose_name='Наименование')
    familiya = models.CharField(max_length=50, verbose_name='Фамилия')
    imy = models.CharField(max_length=50, blank=True, default='', verbose_name='Имя')
    otchestvo = models.CharField(max_length=50, blank=True, default='', verbose_name='Отчество')
    imageFile = models.ImageField(upload_to=directory_path_image, null=True,blank=True,verbose_name="Фото")
    pol = models.IntegerField(choices=TYPE_POL, default=0, verbose_name='Пол')
    DateOfBirth = models.DateField(null=True,blank=True,verbose_name='Дата рождения')

    class Meta:
        verbose_name = 'Физическое лицо'
        verbose_name_plural = 'Справочник: \"Физические лица\"'

    def save(self, *args, **kwargs):
        self.name = self.familiya
        if (self.imy):
            self.name += ' ' + self.imy[:1].upper() + '.'
            if (self.otchestvo):
                self.name += self.otchestvo[:1].upper() + '. '
        super().save(*args, **kwargs)    


class spr_role(spr_default):
    TYPE_ROLE = (
        (0, "Добавление"),
        (1, "Исключение"),
        )

    name = models.CharField(max_length=50, verbose_name='Наименование')
    type_role = models.IntegerField(choices=TYPE_ROLE, default=0, verbose_name='Тип')
    p_smena = models.BooleanField(default=False, verbose_name='Открытие / закрытие смены')
    p_sale = models.BooleanField(default=False, verbose_name='Регистрация продаж')
    p_menu = models.BooleanField(default=False, verbose_name='меню')
    p_obmen = models.BooleanField(default=False, verbose_name='Загрузка с портала обновлений данных.')
    p_report = models.BooleanField(default=False, verbose_name='Отчеты рабочего места')
    p_setting = models.BooleanField(default=False, verbose_name='Установка РМ')
    p_exit = models.BooleanField(default=False, verbose_name='Выход из программы')
    p_zaprosSave = models.BooleanField(default=False, verbose_name='Запрос записи изменений')
    p_return = models.BooleanField(default=False, verbose_name='Возврат')
    p_stoplist = models.BooleanField(default=False, verbose_name='Стоп-лист')
    p_print_tovchek = models.BooleanField(default=False, verbose_name='Печать товарного чека')
    p_print_shet = models.BooleanField(default=False, verbose_name='Печать предчека')
    p_statiySpisaniy = models.BooleanField(default=False, verbose_name='Потверждение статей списания')
    p_onlyYourOrders = models.BooleanField(default=False, verbose_name='Работа только со своими заказами')
    p_removeBlock = models.BooleanField(default=False, verbose_name='Снимать блок с заказа')
    p_opentara = models.BooleanField(default=False, verbose_name='Вскрытие тары')

    class Meta:
        verbose_name = 'Права доступа'
        verbose_name_plural = 'Справочник: \"Права доступа\"'

    def visible_colum_list(self):
        arr=super().visible_colum_list(self);
        arr.append({'id': 'type_role', 'name': 'Тип'})
        return arr


class spr_object_users(models.Model):
    owner = models.ForeignKey('spr_object', verbose_name="Подразделение", on_delete=models.PROTECT)    
    doljnost = models.ForeignKey('spr_doljnosty',null=True, default='', on_delete=models.PROTECT, verbose_name = 'Должность') 
    name = models.CharField(max_length=50, verbose_name='Псевдоним')
    fizlitso = models.ForeignKey('spr_fizlitso',null=True, verbose_name="Физическое лицо", on_delete=models.PROTECT)
    barcode= models.CharField(max_length=30, blank=True, default='', verbose_name="Штрих-код")
    password= models.CharField(max_length=30, blank=True, default='', verbose_name="Пароль")
    tabl_spr_role = models.ManyToManyField('spr_role', verbose_name="Права доступа", blank=True)

    class Meta:
        verbose_name = 'Пользователь POS'
        verbose_name_plural = 'Справочник: \"Пользователи POS\"'

    def visible_colum_list(self):
        arr=[]
        arr.append({'id': 'name', 'name': self._meta.get_field('name').verbose_name,'width':'99%'})
        return arr  


class spr_doljnosty(spr_default):
    name = models.CharField(max_length=50, verbose_name='Наименование')

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Справочник: \"Должности персонала\"'


class spr_units(spr_default):
    name = models.CharField(max_length=20, verbose_name='Наименование')
    kod = models.CharField(max_length=4, verbose_name='ОКЕА', blank=True, default='')

    class Meta:
        verbose_name = 'Единица измерения'
        verbose_name_plural = 'Справочник: \"Классификатор единиц измерения\"'        
       
    def save(self, *args, **kwargs):
        org = spr_units.objects.filter(Q(name=self.name), ~Q(pk=self.pk), Q(reg_global=self.reg_global))
        if org:
            raise ValidationError('Такое наименование уже присутствует')  

        super().save(*args, **kwargs)


class spr_nomenklatura(spr_default):
    TYPE_nomenklatura = (
        (0, "Товар"),
        (1, "Услуга"),
        )    

    parent = models.ForeignKey('spr_nomenklatura', null=True, blank=True, on_delete=models.PROTECT,verbose_name='Подгруппа')
    group = models.BooleanField(default=False, verbose_name='Подгруппа')

    name = models.CharField(max_length=100, verbose_name='Наименование')
    unit = models.ForeignKey('spr_units', null=True, blank=True, verbose_name="Ед. изм.", on_delete=models.PROTECT)
    alco = models.BooleanField(default=False, verbose_name="Алкогольная продукция")
    marked = models.BooleanField(default=False, verbose_name="Маркируемый")
    type_nomenklatura = models.IntegerField(choices=TYPE_nomenklatura, null=True, blank=True, default=0, verbose_name='Вид номенклатуры')

    class Meta:
        verbose_name = 'Номенклатура'
        verbose_name_plural = 'Справочник: \"Номенклатуры\"'

    def visible_colum_list(self):
        arr=super().visible_colum_list(self)
        arr.append({'id': 'unit', 'name': self._meta.get_field('unit').verbose_name,'width':'99%'})
        return arr        

    def save(self, *args, **kwargs):
        with transaction.atomic():
            super().save(*args, **kwargs)
            if (self.unit):
                spr_nomenklatura_units.objects.update_or_create(owner=self, unit=self.unit, defaults={'koef': 1,'reg_global':self.reg_global})


class spr_nomenklatura_units(spr_default):
    owner = models.ForeignKey('spr_nomenklatura', on_delete=models.PROTECT,verbose_name='Номенклатура')
    unit = models.ForeignKey('spr_units', verbose_name="Ед. изм.", on_delete=models.PROTECT)
    koef = models.DecimalField(max_digits=6, decimal_places=3, verbose_name="Коеф.")

    class Meta:
        verbose_name = 'Единицы номенклатуры'
        verbose_name_plural = 'Справочник: \"Единицы номенклатуры\"'

    def __str__(self):
        return self.unit.name + '(' + "{:10.3f}".format(self.koef) + ') ' + self.owner.name

    def visible_colum_list(self):
        arr=[]
        arr.append({'id': 'owner', 'name': self._meta.get_field('owner').verbose_name,'width':'99%'})
        arr.append({'id': 'unit', 'name': self._meta.get_field('unit').verbose_name,'width':'99%'})
        return arr


class spr_nomenklatura_barcode(spr_default):
    owner = models.ForeignKey('spr_nomenklatura_units', on_delete=models.PROTECT,verbose_name='Единица номенклатуры')
    barcode = models.CharField(max_length=13, verbose_name='Штрих-код')

    class Meta:
        verbose_name = 'Штрих-код'
        verbose_name_plural = 'Справочник: \"Штрих-коды единиц измерения\"'

    def visible_colum_list(self):
        arr=[]
        arr.append({'id': 'owner', 'name': self._meta.get_field('owner').verbose_name,'width':'99%'})
        arr.append({'id': 'barcode', 'name': self._meta.get_field('barcode').verbose_name,'width':'99%'})
        return arr


class spr_variantoplaty(spr_default):
    name = models.CharField(max_length=50, verbose_name='Наименование')
    TYPE_VO = (
        (0, "Наличными"),
        (1, "Безначичными"),
        (2, "Без выручки"),
        )

    type_oplaty = models.IntegerField(choices=TYPE_VO, default=0, verbose_name='Вид оплаты')
    tabl_spr_statiyzatrat = models.ManyToManyField('spr_statiyzatrat', verbose_name="Статьи затрат", blank=True)

    class Meta:
        verbose_name = 'Вариант оплаты'
        verbose_name_plural = 'Справочник: \"Варианты оплаты\"'        


class spr_statiyzatrat(spr_default):
    name = models.CharField(max_length=50, verbose_name='Наименование')

    class Meta:
        verbose_name = 'Статья затрат'
        verbose_name_plural = 'Справочник: \"Статьи затрат\"'   


class spr_priznakdelete(spr_default):
    TYPE_delete = (
        (0, "Без списания"),
        (1, "За счет организации"),
        (2, "За счет сотрудника"),
        )    
    name = models.CharField(max_length=50, verbose_name='Наименование')
    b_authorization = models.BooleanField(default=False, verbose_name='Требуется авторизация')
    type_delete = models.IntegerField(choices=TYPE_delete, default=0, verbose_name='Вид удаления')

    class Meta:
        verbose_name = 'Признак удаления'
        verbose_name_plural = 'Справочник: \"Признаки удаления\"'

    def visible_colum_list(self):
        arr=super().visible_colum_list(self)
        arr.append({'id': 'b_authorization', 'name': self._meta.get_field('b_authorization').verbose_name,'width':'99%'})
        return arr      


class spr_pictures(spr_default):
    name = models.CharField(max_length=50, verbose_name='Наименование')
    imageFile = models.ImageField(upload_to=directory_path_image, verbose_name="Картинка")

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Справочник: \"Картинки\"'


class spr_otdely(spr_default):
    name = models.CharField(max_length=50, verbose_name='Наименование')
    number = models.IntegerField(null=True, blank=True, default=0,verbose_name="Номер отдела")    

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Справочник: \"Отделы\"'       


class spr_stavkands(spr_default):
    name = models.CharField(max_length=50, default='', verbose_name='Наименование')
    stavka = models.DecimalField(max_digits=4, default=0, decimal_places=2, verbose_name='Ставка.')
    class Meta:
        verbose_name = 'Ставка НДС'
        verbose_name_plural = 'Справочник: \"Ставки НДС\"'


class spr_categories(spr_default):
    name = models.CharField(max_length=50, verbose_name='Наименование')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Справочник: \"Категории товара\"'


class spr_grprint(spr_default):
    name = models.CharField(max_length=50, verbose_name='Наименование')

    class Meta:
        verbose_name = 'Группа печати'
        verbose_name_plural = 'Справочник: \"Группы печати\"'    


class spr_menu(spr_default):
    owner = models.ForeignKey('spr_typemenu', on_delete=models.PROTECT,verbose_name='Тип меню')
    parent = models.ForeignKey('spr_menu',null=True,blank=True, on_delete=models.PROTECT,verbose_name='Подгруппа')
    group = models.BooleanField(default=False, verbose_name='Группа')
    name = models.CharField(max_length=50, verbose_name='Наименование')
    name_full = models.CharField(max_length=150, verbose_name='Полное наименование')
    nomenklatura = models.ForeignKey('spr_nomenklatura',null=True,blank=True, on_delete=models.PROTECT,verbose_name='Номенклатура')
    unit = models.ForeignKey('spr_nomenklatura_units',null=True,blank=True, on_delete=models.PROTECT,verbose_name='Единица номенклатуры')
    stavkands = models.ForeignKey('spr_stavkands',null=True,blank=True, on_delete=models.PROTECT,verbose_name='Ставка НДС')
    opisanie = models.TextField(null=True,blank=True, verbose_name='Описание') 
    ves = models.PositiveSmallIntegerField(blank=True,default=0,verbose_name='Вес (гр.)')
    time = models.PositiveSmallIntegerField(blank=True,default=0, verbose_name='Время приготовления (мин)')
    calories = models.PositiveSmallIntegerField(blank=True,default=0,verbose_name='ККал')
    belki = models.PositiveSmallIntegerField(blank=True,default=0,verbose_name='Белки')
    jiry = models.PositiveSmallIntegerField(blank=True,default=0,verbose_name='Жири')
    uglevody = models.PositiveSmallIntegerField(blank=True,default=0,verbose_name='Углеводы')
    imageFile = models.ImageField(upload_to=directory_path_image, null=True, blank=True,verbose_name='Фото')
    price = models.DecimalField(max_digits=11, default=0, decimal_places=2, verbose_name='Цена')
    sort = models.PositiveSmallIntegerField(blank=True, default=0,verbose_name='сортировка')
    otdel = models.ForeignKey('spr_otdely',null=True, blank=True, on_delete=models.PROTECT,verbose_name='Отдел')
    izbran = models.BooleanField(default=False, verbose_name='Избранный')
    categorie = models.ForeignKey('spr_categories',null=True,blank=True, on_delete=models.PROTECT,verbose_name='Категория')
    vesovoy = models.BooleanField(default=False, verbose_name='Весовой')
    zaprosprice = models.BooleanField(default=False, verbose_name='Запрашивать цену')
    podarok = models.BooleanField(default=False, verbose_name='Признак \"Подарок\"')
    zapretruchnogovybora = models.BooleanField(default=False, verbose_name='Запрет ручного выбора')
    kodPodbora = models.CharField(blank=True,default='',max_length=6, verbose_name='Наименование')
    name_kuhny = models.CharField(blank=True,default='',max_length=50, verbose_name='Наименование для кухни')
    separate = models.BooleanField(default=False, verbose_name='Отдельный')
    grprint = models.ForeignKey('spr_grprint',null=True, blank=True, on_delete=models.PROTECT,verbose_name='Группа печати')
    
    class Meta:
        verbose_name = 'Состав меню'
        verbose_name_plural = 'Справочник: \"Состав меню\"'

    def visible_colum_list(self):
        arr=super().visible_colum_list(self)
        arr.append({'id': 'group', 'name': self._meta.get_field('group').verbose_name,'width':'99%'})
        return arr  


class spr_conditions(spr_default):
    TYPE_Condition = (
        (0, "Количество гостей"),
        (1, "Временной интервал"),
        (2, "Категория товара"),
        (3, "Количество товара"),
        (4, "Сумма товара"),
        (5, "Дни недели"),
        )       
    name = models.CharField(max_length=100, verbose_name='Наименование')
    guest_min = models.PositiveSmallIntegerField(blank=True,default=0,verbose_name='Минимальное')
    guest_max = models.PositiveSmallIntegerField(blank=True,default=0,verbose_name='Максимальное')
    date_vvoda_start = models.DateField(null=True,blank=True,verbose_name='Начало')
    date_vvoda_stop = models.DateField(null=True,blank=True,verbose_name='Окончание')
    kol_min = models.PositiveSmallIntegerField(blank=True,default=0,verbose_name='Минимальное')
    kol_max = models.PositiveSmallIntegerField(blank=True,default=0,verbose_name='Максимальное')
    summa_min = models.PositiveSmallIntegerField(blank=True,default=0,verbose_name='Минимальное')
    summa_max = models.PositiveSmallIntegerField(blank=True,default=0,verbose_name='Максимальное')
    d1 = models.BooleanField(default=False, verbose_name='Понедельник')
    d2 = models.BooleanField(default=False, verbose_name='Вторник')
    d3 = models.BooleanField(default=False, verbose_name='Среда')
    d4 = models.BooleanField(default=False, verbose_name='Четверг')
    d5 = models.BooleanField(default=False, verbose_name='Пятница')
    d6 = models.BooleanField(default=False, verbose_name='Суббота')
    d7 = models.BooleanField(default=False, verbose_name='Воскресенье')

    class Meta:
        verbose_name = 'Условие применение'
        verbose_name_plural = 'Справочник: \"Условия примнения скидок\наценок\"'


class spr_conditions_tabl_categories(spr_default):
    owner = models.ForeignKey('spr_conditions', on_delete=models.PROTECT,verbose_name='Условия примнения скидок\наценок')
    categorie = models.ForeignKey('spr_categories', verbose_name="Категория", on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Условия (Категория)'
        verbose_name_plural = 'Условия (Категория)'

    def __str__(self):
        return self.categorie.name  + self.owner.name

    def visible_colum_list(self):
        arr=[]
        arr.append({'id': 'owner', 'name': self._meta.get_field('owner').verbose_name,'width':'99%'})
        arr.append({'id': 'categorie', 'name': self._meta.get_field('categorie').verbose_name,'width':'99%'})
        return arr


class spr_mod(spr_default):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    parent = models.ForeignKey('spr_mod',null=True,blank=True, on_delete=models.PROTECT,verbose_name='Подгруппа')
    group = models.BooleanField(default=False, verbose_name='Группа')
    min_quantity = models.PositiveSmallIntegerField(blank=True,default=0,verbose_name='Мин. кол.')
    max_quantity = models.PositiveSmallIntegerField(blank=True,default=0,verbose_name='Макс. кол.')
    bezDubley = models.BooleanField(default=False, verbose_name='Без дублей')
    pr_nomenklatura = models.BooleanField(default=False, verbose_name='Признак номенклатура')
    nomenklatura = models.ForeignKey('spr_nomenklatura',null=True,blank=True, on_delete=models.PROTECT,verbose_name='Номенклатура')
    unit = models.ForeignKey('spr_nomenklatura_units',null=True,blank=True, verbose_name="Ед. изм.", on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=11, default=0, decimal_places=2, verbose_name='Цена')


    class Meta:
        verbose_name = 'Модификатор'
        verbose_name_plural = 'Справочник: \"Модификаторы\"'


class spr_menu_tabl_spr_mod(spr_default):
    owner = models.ForeignKey('spr_menu', on_delete=models.PROTECT,verbose_name='Позиция меню')
    mod = models.ForeignKey('spr_mod', verbose_name="Модификатор", on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Меню (модификатор)'
        verbose_name_plural = 'Справочник: \"Меню (модификаторы)\"'

    def __str__(self):
        return self.mod.name  + self.owner.name

    def visible_colum_list(self):
        arr=[]
        arr.append({'id': 'owner', 'name': self._meta.get_field('owner').verbose_name,'width':'99%'})
        arr.append({'id': 'mod', 'name': self._meta.get_field('mod').verbose_name,'width':'99%'})
        return arr


class spr_discont(spr_default):
    TYPE_discont = (
        (0, "Скидка (%)"),
        (1, "Скидка (сумма)"),
        (2, "Наценка (%)"),
        (3, "Наценка (сумма)"),
        )    
    name = models.CharField(max_length=50, verbose_name='Наименование')
    allcategories = models.BooleanField(default=False, verbose_name='Для всех категорий')
    arbitraryvalue = models.BooleanField(default=False, verbose_name='Произвольное значение')
    enable = models.BooleanField(default=True, verbose_name='вкл.')
    manually = models.BooleanField(default=False, verbose_name='Ручная')
    sort = models.PositiveSmallIntegerField(default=0, verbose_name='Сортировка')
    type_discount = models.IntegerField(choices=TYPE_discont, default=0, verbose_name='Вид скидки/наценки')  
    value = models.DecimalField(max_digits=11, default=0, decimal_places=2, verbose_name='Значение')  

    class Meta:
        verbose_name = 'Скидка\Наценки'
        verbose_name_plural = 'Справочник: \"СкидкиНаценки\"'


class spr_discont_tabl_spr_categories(spr_default):
    owner = models.ForeignKey('spr_discont', on_delete=models.PROTECT,verbose_name='Скидка/Наценка')
    categorie = models.ForeignKey('spr_categories', verbose_name="Категория", on_delete=models.PROTECT)
    value = models.DecimalField(max_digits=11, default=0, decimal_places=2, verbose_name='Значение')

    class Meta:
        verbose_name = 'Скидка\Наценки (Категория)'
        verbose_name_plural = 'Справочник: \"Скидка\Наценки (Категории)\"'

    def __str__(self):
        return self.categorie.name  + self.owner.name

    def visible_colum_list(self):
        arr=[]
        arr.append({'id': 'owner', 'name': self._meta.get_field('owner').verbose_name,'width':'99%'})
        arr.append({'id': 'categorie', 'name': self._meta.get_field('categorie').verbose_name,'width':'99%'})
        return arr


class spr_discont_tabl_spr_object(spr_default):
    owner = models.ForeignKey('spr_discont', on_delete=models.PROTECT,verbose_name='Скидка/Наценка')
    podrazdelenie = models.ForeignKey('spr_object', verbose_name="Подразделение", on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Скидка\Наценки (Подразделение)'
        verbose_name_plural = 'Справочник: \"Скидка\Наценки (Подразделения)\"'

    def __str__(self):
        return self.podrazdelenie.name  + self.owner.name

    def visible_colum_list(self):
        arr=[]
        arr.append({'id': 'owner', 'name': self._meta.get_field('owner').verbose_name,'width':'99%'})
        arr.append({'id': 'podrazdelenie', 'name': self._meta.get_field('podrazdelenie').verbose_name,'width':'99%'})
        return arr        


class spr_discont_tabl_spr_conditions(spr_default):
    owner = models.ForeignKey('spr_discont', on_delete=models.PROTECT,verbose_name='Скидка/Наценка')
    conditions = models.ForeignKey('spr_conditions', verbose_name="Условие", on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Скидка\Наценки (Условия применения)'
        verbose_name_plural = 'Справочник: \"Скидка\Наценки (Условия применения)\"'

    def __str__(self):
        return self.podrazdelenie.name  + self.owner.name

    def visible_colum_list(self):
        arr=[]
        arr.append({'id': 'owner', 'name': self._meta.get_field('owner').verbose_name,'width':'99%'})
        arr.append({'id': 'conditions', 'name': self._meta.get_field('conditions').verbose_name,'width':'99%'})
        return arr                       