# Generated by Django 4.0.4 on 2022-10-30 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iop_app', '0003_alter_counterrors_parcel_machine'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CountErrors',
        ),
    ]