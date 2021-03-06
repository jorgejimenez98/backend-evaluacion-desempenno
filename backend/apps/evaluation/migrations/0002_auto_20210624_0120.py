# Generated by Django 3.2.2 on 2021-06-23 23:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payTime', '0002_rename_enddata_paytime_enddate'),
        ('workers', '0006_alter_worker_operador'),
        ('evaluation', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='monthlyevaluation',
            unique_together={('payTime', 'evaluateWorker')},
        ),
        migrations.AlterIndexTogether(
            name='monthlyevaluation',
            index_together={('payTime', 'evaluateWorker')},
        ),
    ]
