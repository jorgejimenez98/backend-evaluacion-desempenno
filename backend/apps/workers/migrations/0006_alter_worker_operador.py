# Generated by Django 3.2.2 on 2021-06-17 00:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0005_worker_operador'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='operador',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='worker', to='workers.operador'),
        ),
    ]