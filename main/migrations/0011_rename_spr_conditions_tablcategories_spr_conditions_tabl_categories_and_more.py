# Generated by Django 4.0.3 on 2022-04-03 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('main', '0010_spr_conditions_tablcategories'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='spr_conditions_tablcategories',
            new_name='spr_conditions_tabl_categories',
        ),
        migrations.RenameModel(
            old_name='spr_discont_tablcategories',
            new_name='spr_discont_tabl_categories',
        ),
        migrations.RenameModel(
            old_name='spr_discont_tablconditions',
            new_name='spr_discont_tabl_conditions',
        ),
        migrations.RenameModel(
            old_name='spr_discont_tablobject',
            new_name='spr_discont_tabl_object',
        ),
    ]
