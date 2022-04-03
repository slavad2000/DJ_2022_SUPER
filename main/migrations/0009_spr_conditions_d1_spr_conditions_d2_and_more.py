# Generated by Django 4.0.3 on 2022-04-03 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_rename_spr_discont_categories_spr_discont_tablcategories_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='spr_conditions',
            name='d1',
            field=models.BooleanField(default=False, verbose_name='Понедельник'),
        ),
        migrations.AddField(
            model_name='spr_conditions',
            name='d2',
            field=models.BooleanField(default=False, verbose_name='Вторник'),
        ),
        migrations.AddField(
            model_name='spr_conditions',
            name='d3',
            field=models.BooleanField(default=False, verbose_name='Среда'),
        ),
        migrations.AddField(
            model_name='spr_conditions',
            name='d4',
            field=models.BooleanField(default=False, verbose_name='Четверг'),
        ),
        migrations.AddField(
            model_name='spr_conditions',
            name='d5',
            field=models.BooleanField(default=False, verbose_name='Пятница'),
        ),
        migrations.AddField(
            model_name='spr_conditions',
            name='d6',
            field=models.BooleanField(default=False, verbose_name='Суббота'),
        ),
        migrations.AddField(
            model_name='spr_conditions',
            name='d7',
            field=models.BooleanField(default=False, verbose_name='Воскресенье'),
        ),
        migrations.AddField(
            model_name='spr_conditions',
            name='date_vvoda_start',
            field=models.DateField(blank=True, null=True, verbose_name='Начало'),
        ),
        migrations.AddField(
            model_name='spr_conditions',
            name='date_vvoda_stop',
            field=models.DateField(blank=True, null=True, verbose_name='Окончание'),
        ),
        migrations.AddField(
            model_name='spr_conditions',
            name='guest_max',
            field=models.PositiveSmallIntegerField(blank=True, default=0, verbose_name='Максимальное'),
        ),
        migrations.AddField(
            model_name='spr_conditions',
            name='guest_min',
            field=models.PositiveSmallIntegerField(blank=True, default=0, verbose_name='Минимальное'),
        ),
        migrations.AddField(
            model_name='spr_conditions',
            name='kol_max',
            field=models.PositiveSmallIntegerField(blank=True, default=0, verbose_name='Максимальное'),
        ),
        migrations.AddField(
            model_name='spr_conditions',
            name='kol_min',
            field=models.PositiveSmallIntegerField(blank=True, default=0, verbose_name='Минимальное'),
        ),
        migrations.AddField(
            model_name='spr_conditions',
            name='summa_max',
            field=models.PositiveSmallIntegerField(blank=True, default=0, verbose_name='Максимальное'),
        ),
        migrations.AddField(
            model_name='spr_conditions',
            name='summa_min',
            field=models.PositiveSmallIntegerField(blank=True, default=0, verbose_name='Минимальное'),
        ),
    ]
