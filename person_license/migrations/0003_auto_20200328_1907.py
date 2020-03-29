# Generated by Django 3.0.4 on 2020-03-28 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('person_license', '0002_auto_20200328_1856'),
    ]

    operations = [
        migrations.RenameField(
            model_name='license',
            old_name='expiryDate',
            new_name='expiry_date',
        ),
        migrations.RenameField(
            model_name='license',
            old_name='issueDate',
            new_name='issue_date',
        ),
        migrations.RenameField(
            model_name='license',
            old_name='licenseNumber',
            new_name='license_number',
        ),
        migrations.RemoveField(
            model_name='license',
            name='id',
        ),
        migrations.AlterField(
            model_name='license',
            name='person',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='person_license.Person'),
        ),
    ]