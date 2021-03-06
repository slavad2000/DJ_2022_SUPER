# Generated by Django 4.0.3 on 2022-04-03 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='spr_zaly',
            name='reg_global',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.reg_global', verbose_name='Global ID'),
        ),
        migrations.AddField(
            model_name='spr_variantoplaty',
            name='reg_global',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.reg_global', verbose_name='Global ID'),
        ),
        migrations.AddField(
            model_name='spr_variantoplaty',
            name='tabl_spr_statiyzatrat',
            field=models.ManyToManyField(blank=True, to='main.spr_statiyzatrat', verbose_name='Статьи затрат'),
        ),
        migrations.AddField(
            model_name='spr_units',
            name='reg_global',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.reg_global', verbose_name='Global ID'),
        ),
        migrations.AddField(
            model_name='spr_typemenu',
            name='reg_global',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.reg_global', verbose_name='Global ID'),
        ),
        migrations.AddField(
            model_name='spr_stavkands',
            name='reg_global',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.reg_global', verbose_name='Global ID'),
        ),
        migrations.AddField(
            model_name='spr_statiyzatrat',
            name='reg_global',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.reg_global', verbose_name='Global ID'),
        ),
        migrations.AddField(
            model_name='spr_role',
            name='reg_global',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.reg_global', verbose_name='Global ID'),
        ),
        migrations.AddField(
            model_name='spr_priznakdelete',
            name='reg_global',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.reg_global', verbose_name='Global ID'),
        ),
        migrations.AddField(
            model_name='spr_pictures',
            name='reg_global',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.reg_global', verbose_name='Global ID'),
        ),
        migrations.AddField(
            model_name='spr_otdely',
            name='reg_global',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.reg_global', verbose_name='Global ID'),
        ),
        migrations.AddField(
            model_name='spr_object_users',
            name='doljnost',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.PROTECT, to='main.spr_doljnosty', verbose_name='Должность'),
        ),
        migrations.AddField(
            model_name='spr_object_users',
            name='fizlitso',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.spr_fizlitso', verbose_name='Физическое лицо'),
        ),
        migrations.AddField(
            model_name='spr_object_users',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.spr_object', verbose_name='Подразделение'),
        ),
        migrations.AddField(
            model_name='spr_object_users',
            name='tabl_spr_role',
            field=models.ManyToManyField(blank=True, to='main.spr_role', verbose_name='Права доступа'),
        ),
        migrations.AddField(
            model_name='spr_object',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.spr_company', verbose_name='Головная организация'),
        ),
        migrations.AddField(
            model_name='spr_object',
            name='reg_global',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.reg_global', verbose_name='Global ID'),
        ),
        migrations.AddField(
            model_name='spr_object',
            name='tabl_spr_typemenu',
            field=models.ManyToManyField(blank=True, to='main.spr_typemenu'),
        ),
        migrations.AddField(
            model_name='spr_object',
            name='tabl_spr_zaly',
            field=models.ManyToManyField(blank=True, to='main.spr_zaly'),
        ),
        migrations.AddField(
            model_name='spr_nomenklatura_units',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.spr_nomenklatura', verbose_name='Номенклатура'),
        ),
        migrations.AddField(
            model_name='spr_nomenklatura_units',
            name='reg_global',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.reg_global', verbose_name='Global ID'),
        ),
        migrations.AddField(
            model_name='spr_nomenklatura_units',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.spr_units', verbose_name='Ед. изм.'),
        ),
        migrations.AddField(
            model_name='spr_nomenklatura_barcode',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.spr_nomenklatura_units', verbose_name='Единица номенклатуры'),
        ),
        migrations.AddField(
            model_name='spr_nomenklatura_barcode',
            name='reg_global',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.reg_global', verbose_name='Global ID'),
        ),
        migrations.AddField(
            model_name='spr_nomenklatura',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='main.spr_nomenklatura', verbose_name='Подгруппа'),
        ),
        migrations.AddField(
            model_name='spr_nomenklatura',
            name='reg_global',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.reg_global', verbose_name='Global ID'),
        ),
        migrations.AddField(
            model_name='spr_nomenklatura',
            name='unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='main.spr_units', verbose_name='Ед. изм.'),
        ),
        migrations.AddField(
            model_name='spr_modificators',
            name='nomenklatura',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='main.spr_nomenklatura', verbose_name='Номенклатура'),
        ),
        migrations.AddField(
            model_name='spr_modificators',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='main.spr_modificators', verbose_name='Подгруппа'),
        ),
        migrations.AddField(
            model_name='spr_modificators',
            name='reg_global',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.reg_global', verbose_name='Global ID'),
        ),
        migrations.AddField(
            model_name='spr_modificators',
            name='unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='main.spr_nomenklatura_units', verbose_name='Ед. изм.'),
        ),
        migrations.AddField(
            model_name='spr_menu_tabl_spr_modificators',
            name='modificator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.spr_modificators', verbose_name='Модификатор'),
        ),
        migrations.AddField(
            model_name='spr_menu_tabl_spr_modificators',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.spr_menu', verbose_name='Позиция меню'),
        ),
        migrations.AddField(
            model_name='spr_menu_tabl_spr_modificators',
            name='reg_global',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.reg_global', verbose_name='Global ID'),
        ),
        migrations.AddField(
            model_name='spr_menu',
            name='categorie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='main.spr_categories', verbose_name='Категория'),
        ),
        migrations.AddField(
            model_name='spr_menu',
            name='grprint',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='main.spr_grprint', verbose_name='Группа печати'),
        ),
        migrations.AddField(
            model_name='spr_menu',
            name='nomenklatura',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='main.spr_nomenklatura', verbose_name='Номенклатура'),
        ),
        migrations.AddField(
            model_name='spr_menu',
            name='otdel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='main.spr_otdely', verbose_name='Отдел'),
        ),
        migrations.AddField(
            model_name='spr_menu',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.spr_typemenu', verbose_name='Тип меню'),
        ),
        migrations.AddField(
            model_name='spr_menu',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='main.spr_menu', verbose_name='Подгруппа'),
        ),
        migrations.AddField(
            model_name='spr_menu',
            name='reg_global',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.reg_global', verbose_name='Global ID'),
        ),
        migrations.AddField(
            model_name='spr_menu',
            name='stavkands',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='main.spr_stavkands', verbose_name='Ставка НДС'),
        ),
        migrations.AddField(
            model_name='spr_menu',
            name='unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='main.spr_nomenklatura_units', verbose_name='Единица номенклатуры'),
        ),
        migrations.AddField(
            model_name='spr_grprint',
            name='reg_global',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.reg_global', verbose_name='Global ID'),
        ),
        migrations.AddField(
            model_name='spr_fizlitso',
            name='reg_global',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.reg_global', verbose_name='Global ID'),
        ),
        migrations.AddField(
            model_name='spr_doljnosty',
            name='reg_global',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.reg_global', verbose_name='Global ID'),
        ),
        migrations.AddField(
            model_name='spr_discont_tabl_spr_object',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.spr_discont', verbose_name='Скидка/Наценка'),
        ),
        migrations.AddField(
            model_name='spr_discont_tabl_spr_object',
            name='podrazdelenie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.spr_object', verbose_name='Подразделение'),
        ),
        migrations.AddField(
            model_name='spr_discont_tabl_spr_object',
            name='reg_global',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.reg_global', verbose_name='Global ID'),
        ),
        migrations.AddField(
            model_name='spr_discont_tabl_spr_conditions',
            name='conditions',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.spr_conditions', verbose_name='Условие'),
        ),
        migrations.AddField(
            model_name='spr_discont_tabl_spr_conditions',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.spr_discont', verbose_name='Скидка/Наценка'),
        ),
        migrations.AddField(
            model_name='spr_discont_tabl_spr_conditions',
            name='reg_global',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.reg_global', verbose_name='Global ID'),
        ),
        migrations.AddField(
            model_name='spr_discont_tabl_spr_categories',
            name='categorie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.spr_categories', verbose_name='Категория'),
        ),
        migrations.AddField(
            model_name='spr_discont_tabl_spr_categories',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.spr_discont', verbose_name='Скидка/Наценка'),
        ),
        migrations.AddField(
            model_name='spr_discont_tabl_spr_categories',
            name='reg_global',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.reg_global', verbose_name='Global ID'),
        ),
        migrations.AddField(
            model_name='spr_discont',
            name='reg_global',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.reg_global', verbose_name='Global ID'),
        ),
        migrations.AddField(
            model_name='spr_conditions_tabl_categories',
            name='categorie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.spr_categories', verbose_name='Категория'),
        ),
        migrations.AddField(
            model_name='spr_conditions_tabl_categories',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.spr_conditions', verbose_name='Условия примнения скидок\\наценок'),
        ),
        migrations.AddField(
            model_name='spr_conditions_tabl_categories',
            name='reg_global',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.reg_global', verbose_name='Global ID'),
        ),
        migrations.AddField(
            model_name='spr_conditions',
            name='reg_global',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.reg_global', verbose_name='Global ID'),
        ),
        migrations.AddField(
            model_name='spr_company',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='main.spr_company', verbose_name='Головная организация'),
        ),
        migrations.AddField(
            model_name='spr_company',
            name='reg_global',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.reg_global', verbose_name='Global ID'),
        ),
        migrations.AddField(
            model_name='spr_categories',
            name='reg_global',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.reg_global', verbose_name='Global ID'),
        ),
    ]
