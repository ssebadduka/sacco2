# Generated by Django 4.1.7 on 2023-02-25 04:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sacco1', '0007_rename_movie_image_members_m_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='expenses',
            options={'verbose_name': 'expenses', 'verbose_name_plural': 'expenses'},
        ),
        migrations.AlterModelOptions(
            name='loan',
            options={'verbose_name': 'loan', 'verbose_name_plural': 'loan'},
        ),
        migrations.AlterModelOptions(
            name='loanofficer',
            options={'verbose_name': 'loanofficer', 'verbose_name_plural': 'loanofficer'},
        ),
        migrations.AlterModelOptions(
            name='members',
            options={'verbose_name': 'member', 'verbose_name_plural': 'member'},
        ),
        migrations.AlterModelOptions(
            name='savings',
            options={'verbose_name': 'saving', 'verbose_name_plural': 'saving'},
        ),
        migrations.RemoveField(
            model_name='expenses',
            name='Name',
        ),
    ]