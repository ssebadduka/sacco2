# Generated by Django 4.1.7 on 2023-02-22 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sacco1', '0004_rename_name_members_full_name_remove_members_age_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='members',
            old_name='Next_of_kin',
            new_name='Next_of_kin_Contact',
        ),
    ]
