# Generated by Django 4.1.4 on 2023-01-02 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('iop_app', '0005_errorcount_remove_worker_error_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='errors',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='iop_app.errorcount'),
        ),
    ]
