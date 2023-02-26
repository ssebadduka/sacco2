# Generated by Django 4.1.7 on 2023-02-22 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sacco1', '0003_remove_members_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='members',
            old_name='Name',
            new_name='Full_Name',
        ),
        migrations.RemoveField(
            model_name='members',
            name='Age',
        ),
        migrations.RemoveField(
            model_name='members',
            name='Gender',
        ),
        migrations.AlterField(
            model_name='members',
            name='National_id',
            field=models.CharField(blank=True, max_length=14, null=True),
        ),
    ]
