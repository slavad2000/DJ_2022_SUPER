# Generated by Django 4.0.3 on 2022-04-02 22:38

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('main', '0002_spr_zaly_spr_typemenu_spr_object'),
    ]

    operations = [
        migrations.CreateModel(
            name='spr_doljnosty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guid_update', models.UUIDField(blank=True, default=uuid.uuid4)),
                ('deleted', models.BooleanField(default=False, verbose_name='Блокировка')),
                ('code', models.CharField(blank=True, default='', max_length=11, verbose_name='Код')),
                ('name', models.CharField(max_length=50, verbose_name='Наименование')),
                ('reg_global', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.reg_global', verbose_name='Global ID')),
            ],
            options={
                'verbose_name': 'Должность',
                'verbose_name_plural': 'Справочник: "Должности персонала"',
            },
        ),
        migrations.CreateModel(
            name='spr_fizlitso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guid_update', models.UUIDField(blank=True, default=uuid.uuid4)),
                ('deleted', models.BooleanField(default=False, verbose_name='Блокировка')),
                ('code', models.CharField(blank=True, default='', max_length=11, verbose_name='Код')),
                ('name', models.CharField(blank=True, default='', max_length=100, verbose_name='Наименование')),
                ('familiya', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('imy', models.CharField(blank=True, default='', max_length=50, verbose_name='Имя')),
                ('otchestvo', models.CharField(blank=True, default='', max_length=50, verbose_name='Отчество')),
                ('imageFile', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Фото')),
                ('pol', models.IntegerField(choices=[(0, 'Мужской'), (1, 'Женский')], default=0, verbose_name='Пол')),
                ('DateOfBirth', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
                ('reg_global', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.reg_global', verbose_name='Global ID')),
            ],
            options={
                'verbose_name': 'Физическое лицо',
                'verbose_name_plural': 'Справочник: "Физические лица"',
            },
        ),
        migrations.CreateModel(
            name='spr_nomenklatura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guid_update', models.UUIDField(blank=True, default=uuid.uuid4)),
                ('deleted', models.BooleanField(default=False, verbose_name='Блокировка')),
                ('code', models.CharField(blank=True, default='', max_length=11, verbose_name='Код')),
                ('group', models.BooleanField(default=False, verbose_name='Подгруппа')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование')),
                ('alco', models.BooleanField(default=False, verbose_name='Алкогольная продукция')),
                ('marked', models.BooleanField(default=False, verbose_name='Маркируемый')),
                ('type_nomenklatura', models.IntegerField(blank=True, choices=[(0, 'Товар'), (1, 'Услуга')], default=0, null=True, verbose_name='Вид номенклатуры')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='main.spr_nomenklatura', verbose_name='Подгруппа')),
                ('reg_global', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.reg_global', verbose_name='Global ID')),
            ],
            options={
                'verbose_name': 'Номенклатура',
                'verbose_name_plural': 'Справочник: "Номенклатуры"',
            },
        ),
        migrations.CreateModel(
            name='spr_statiyzatrat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guid_update', models.UUIDField(blank=True, default=uuid.uuid4)),
                ('deleted', models.BooleanField(default=False, verbose_name='Блокировка')),
                ('code', models.CharField(blank=True, default='', max_length=11, verbose_name='Код')),
                ('name', models.CharField(max_length=50, verbose_name='Наименование')),
                ('reg_global', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.reg_global', verbose_name='Global ID')),
            ],
            options={
                'verbose_name': 'Статья затрат',
                'verbose_name_plural': 'Справочник: "Статьи затрат"',
            },
        ),
        migrations.CreateModel(
            name='spr_variantoplaty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guid_update', models.UUIDField(blank=True, default=uuid.uuid4)),
                ('deleted', models.BooleanField(default=False, verbose_name='Блокировка')),
                ('code', models.CharField(blank=True, default='', max_length=11, verbose_name='Код')),
                ('name', models.CharField(max_length=50, verbose_name='Наименование')),
                ('type_oplaty', models.IntegerField(choices=[(0, 'Наличными'), (1, 'Безначичными'), (2, 'Без выручки')], default=0, verbose_name='Вид оплаты')),
                ('reg_global', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.reg_global', verbose_name='Global ID')),
                ('tabl_spr_statiyzatrat', models.ManyToManyField(blank=True, to='main.spr_statiyzatrat', verbose_name='Статьи затрат')),
            ],
            options={
                'verbose_name': 'Вариант оплаты',
                'verbose_name_plural': 'Справочник: "Варианты оплаты"',
            },
        ),
        migrations.CreateModel(
            name='spr_units',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guid_update', models.UUIDField(blank=True, default=uuid.uuid4)),
                ('deleted', models.BooleanField(default=False, verbose_name='Блокировка')),
                ('code', models.CharField(blank=True, default='', max_length=11, verbose_name='Код')),
                ('name', models.CharField(max_length=20, verbose_name='Наименование')),
                ('kod', models.CharField(blank=True, default='', max_length=4, verbose_name='ОКЕА')),
                ('reg_global', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.reg_global', verbose_name='Global ID')),
            ],
            options={
                'verbose_name': 'Единица измерения',
                'verbose_name_plural': 'Справочник: "Классификатор единиц измерения"',
            },
        ),
        migrations.CreateModel(
            name='spr_role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guid_update', models.UUIDField(blank=True, default=uuid.uuid4)),
                ('deleted', models.BooleanField(default=False, verbose_name='Блокировка')),
                ('code', models.CharField(blank=True, default='', max_length=11, verbose_name='Код')),
                ('name', models.CharField(max_length=50, verbose_name='Наименование')),
                ('type_role', models.IntegerField(choices=[(0, 'Добавление'), (1, 'Исключение')], default=0, verbose_name='Тип')),
                ('p_smena', models.BooleanField(default=False, verbose_name='Открытие / закрытие смены')),
                ('p_sale', models.BooleanField(default=False, verbose_name='Регистрация продаж')),
                ('p_menu', models.BooleanField(default=False, verbose_name='меню')),
                ('p_obmen', models.BooleanField(default=False, verbose_name='Загрузка с портала обновлений данных.')),
                ('p_report', models.BooleanField(default=False, verbose_name='Отчеты рабочего места')),
                ('p_setting', models.BooleanField(default=False, verbose_name='Установка РМ')),
                ('p_exit', models.BooleanField(default=False, verbose_name='Выход из программы')),
                ('p_zaprosSave', models.BooleanField(default=False, verbose_name='Запрос записи изменений')),
                ('p_return', models.BooleanField(default=False, verbose_name='Возврат')),
                ('p_stoplist', models.BooleanField(default=False, verbose_name='Стоп-лист')),
                ('p_print_tovchek', models.BooleanField(default=False, verbose_name='Печать товарного чека')),
                ('p_print_shet', models.BooleanField(default=False, verbose_name='Печать предчека')),
                ('p_statiySpisaniy', models.BooleanField(default=False, verbose_name='Потверждение статей списания')),
                ('p_onlyYourOrders', models.BooleanField(default=False, verbose_name='Работа только со своими заказами')),
                ('p_removeBlock', models.BooleanField(default=False, verbose_name='Снимать блок с заказа')),
                ('p_opentara', models.BooleanField(default=False, verbose_name='Вскрытие тары')),
                ('reg_global', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.reg_global', verbose_name='Global ID')),
            ],
            options={
                'verbose_name': 'Права доступа',
                'verbose_name_plural': 'Справочник: "Права доступа"',
            },
        ),
        migrations.CreateModel(
            name='spr_object_users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Псевдоним')),
                ('barcode', models.CharField(blank=True, default='', max_length=30, verbose_name='Штрих-код')),
                ('password', models.CharField(blank=True, default='', max_length=30, verbose_name='Пароль')),
                ('doljnost', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.PROTECT, to='main.spr_doljnosty', verbose_name='Должность')),
                ('fizlitso', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.spr_fizlitso', verbose_name='Физическое лицо')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.spr_object', verbose_name='Подразделение')),
                ('tabl_spr_role', models.ManyToManyField(blank=True, to='main.spr_role', verbose_name='Права доступа')),
            ],
            options={
                'verbose_name': 'Пользователь POS',
                'verbose_name_plural': 'Справочник: "Пользователи POS"',
            },
        ),
        migrations.CreateModel(
            name='spr_nomenklatura_units',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guid_update', models.UUIDField(blank=True, default=uuid.uuid4)),
                ('deleted', models.BooleanField(default=False, verbose_name='Блокировка')),
                ('code', models.CharField(blank=True, default='', max_length=11, verbose_name='Код')),
                ('koef', models.DecimalField(decimal_places=3, max_digits=6, verbose_name='Коеф.')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.spr_nomenklatura', verbose_name='Номенклатура')),
                ('reg_global', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.reg_global', verbose_name='Global ID')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.spr_units', verbose_name='Ед. изм.')),
            ],
            options={
                'verbose_name': 'Единицы номенклатуры',
                'verbose_name_plural': 'Справочник: "Единицы номенклатуры"',
            },
        ),
        migrations.AddField(
            model_name='spr_nomenklatura',
            name='unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='main.spr_units', verbose_name='Ед. изм.'),
        ),
    ]
