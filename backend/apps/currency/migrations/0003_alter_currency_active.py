# Generated by Django 3.2.2 on 2021-06-14 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0002_alter_currency_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='active',
            field=models.BooleanField(),
        ),
    ]