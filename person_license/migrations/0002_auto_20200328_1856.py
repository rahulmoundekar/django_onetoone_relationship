# Generated by Django 3.0.4 on 2020-03-28 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('person_license', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='license',
            table='license',
        ),
        migrations.AlterModelTable(
            name='person',
            table='person',
        ),
    ]