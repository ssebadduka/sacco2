# Generated by Django 4.1.6 on 2023-02-04 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ammount_received', models.IntegerField(default=0)),
                ('Date_received', models.CharField(max_length=15)),
                ('Purpose', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=25)),
                ('Gender', models.CharField(max_length=6)),
                ('Age', models.IntegerField(default=18)),
                ('Contact', models.CharField(max_length=15)),
                ('Address', models.CharField(max_length=35)),
                ('Next_of_kin', models.CharField(max_length=35)),
                ('Status', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='savings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ammount_saved', models.IntegerField(default=0)),
                ('Date_saved', models.CharField(max_length=10)),
                ('Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sacco1.members')),
            ],
        ),
        migrations.CreateModel(
            name='loanOfficer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Officer_name', models.CharField(max_length=25)),
                ('Date_of_Acceptance', models.DateField(max_length=15)),
                ('status', models.CharField(max_length=10)),
                ('Loan_data', models.CharField(max_length=255)),
                ('Ammount_received', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sacco1.loan')),
                ('Ammount_saved', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sacco1.savings')),
                ('Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sacco1.members')),
            ],
        ),
        migrations.AddField(
            model_name='loan',
            name='Ammount_saved',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sacco1.savings'),
        ),
        migrations.AddField(
            model_name='loan',
            name='Name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sacco1.members'),
        ),
        migrations.CreateModel(
            name='expenses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ammount_spent', models.IntegerField(default=0)),
                ('Spent_by', models.CharField(max_length=25)),
                ('Spent_for', models.CharField(max_length=100)),
                ('Comment', models.CharField(max_length=200)),
                ('Ammount_saved', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sacco1.savings')),
                ('Loan_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sacco1.loanofficer')),
                ('Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sacco1.members')),
            ],
        ),
    ]
