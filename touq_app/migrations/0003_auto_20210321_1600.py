# Generated by Django 3.1.7 on 2021-03-21 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('touq_app', '0002_auto_20210321_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employment',
            name='userEmail',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='employment',
            name='userName',
            field=models.CharField(max_length=50),
        ),
    ]