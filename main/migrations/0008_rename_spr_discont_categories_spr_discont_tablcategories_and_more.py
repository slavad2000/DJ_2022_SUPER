# Generated by Django 4.0.3 on 2022-04-03 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('main', '0007_spr_conditions_spr_discont_alter_spr_menu_imagefile_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='spr_discont_categories',
            new_name='spr_discont_tablcategories',
        ),
        migrations.RenameModel(
            old_name='spr_discont_conditions',
            new_name='spr_discont_tablconditions',
        ),
        migrations.RenameModel(
            old_name='spr_discont_object',
            new_name='spr_discont_tablobject',
        ),
    ]
