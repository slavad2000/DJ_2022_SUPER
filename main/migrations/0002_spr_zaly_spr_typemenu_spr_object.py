# Generated by Django 4.0.3 on 2022-04-02 22:24

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='spr_zaly',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guid_update', models.UUIDField(blank=True, default=uuid.uuid4)),
                ('deleted', models.BooleanField(default=False, verbose_name='Блокировка')),
                ('code', models.CharField(blank=True, default='', max_length=11, verbose_name='Код')),
                ('name', models.CharField(max_length=50, verbose_name='Наименование')),
                ('reg_global', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.reg_global', verbose_name='Global ID')),
            ],
            options={
                'verbose_name': 'Зал',
                'verbose_name_plural': 'Справочник: "Залы"',
            },
        ),
        migrations.CreateModel(
            name='spr_typemenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guid_update', models.UUIDField(blank=True, default=uuid.uuid4)),
                ('deleted', models.BooleanField(default=False, verbose_name='Блокировка')),
                ('code', models.CharField(blank=True, default='', max_length=11, verbose_name='Код')),
                ('name', models.CharField(max_length=50, verbose_name='Наименование')),
                ('reg_global', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.reg_global', verbose_name='Global ID')),
            ],
            options={
                'verbose_name': 'Тип меню',
                'verbose_name_plural': 'Справочник: "Типы меню"',
            },
        ),
        migrations.CreateModel(
            name='spr_object',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guid_update', models.UUIDField(blank=True, default=uuid.uuid4)),
                ('deleted', models.BooleanField(default=False, verbose_name='Блокировка')),
                ('code', models.CharField(blank=True, default='', max_length=11, verbose_name='Код')),
                ('name', models.CharField(max_length=50, verbose_name='Наименование')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.spr_company', verbose_name='Головная организация')),
                ('reg_global', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.reg_global', verbose_name='Global ID')),
                ('tabl_spr_typemenu', models.ManyToManyField(blank=True, to='main.spr_typemenu')),
                ('tabl_spr_zaly', models.ManyToManyField(blank=True, to='main.spr_zaly')),
            ],
            options={
                'verbose_name': 'Подразделение',
                'verbose_name_plural': 'Справочник: "Подразделения"',
            },
        ),
    ]
