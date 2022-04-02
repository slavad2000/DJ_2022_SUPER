from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime

'''Глобальный класс'''
class reg_Global(models.Model):
    block = models.BooleanField(default=False, verbose_name = 'Блокировка')
    date_create = models.DateTimeField(default=datetime.now, blank=True, verbose_name = 'Дата создания')
    pref = models.CharField(max_length=2, verbose_name='Префикс')

    class Meta:
        verbose_name='Глобальная служебная единица'
        verbose_name_plural='Глобальные служебные единицы'

    def delete(self, *args, **kwargs):
        pass 

    def __str__(self):
        return "Global ({})".format(self.pk)


'''Нумератор строк'''
class NumeratorDoc(models.Model):
    reg_global = models.ForeignKey(reg_Global, on_delete=models.PROTECT, verbose_name = 'Global ID')
    doc_name = models.CharField(max_length=50, verbose_name='Тип документа')
    year = models.DateTimeField(default=datetime.now, blank=True, verbose_name = 'Дата создания')


'''Справочник пользователи сайтом'''
class CustomUser(AbstractUser):
    reg_global = models.ForeignKey(reg_Global, on_delete=models.PROTECT, null=True)