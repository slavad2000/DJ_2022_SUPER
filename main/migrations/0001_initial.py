# Generated by Django 4.0.3 on 2022-04-02 19:42

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='spr_company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guid_update', models.UUIDField(blank=True, default=uuid.uuid4)),
                ('deleted', models.BooleanField(default=False, verbose_name='Блокировка')),
                ('code', models.CharField(blank=True, default='', max_length=11, verbose_name='Код')),
                ('type_company', models.IntegerField(choices=[(0, 'Юридическое лицо'), (1, 'Обособленное подразделение'), (2, 'Индивидуальный предприниматель')], default=0, verbose_name='Вид юр.лица')),
                ('name', models.CharField(max_length=50, verbose_name='Наименование')),
                ('name_full', models.CharField(blank=True, default='', max_length=250, verbose_name='Полное наименование')),
                ('inn', models.CharField(blank=True, default='', max_length=12, verbose_name='ИНН')),
                ('kpp', models.CharField(blank=True, default='', max_length=9, verbose_name='КПП')),
                ('addres_u', models.CharField(blank=True, default='', max_length=250, verbose_name='Юридический адрес')),
                ('addres_f', models.CharField(blank=True, default='', max_length=250, verbose_name='Фактический адрес')),
                ('addres_p', models.CharField(blank=True, default='', max_length=250, verbose_name='Почтовый адрес')),
                ('pref', models.CharField(max_length=2, verbose_name='Префикс документов')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='main.spr_company', verbose_name='Головная организация')),
                ('reg_global', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.reg_global', verbose_name='Global ID')),
            ],
            options={
                'verbose_name': 'Организация',
                'verbose_name_plural': 'Справочник: "Организации"',
            },
        ),
    ]