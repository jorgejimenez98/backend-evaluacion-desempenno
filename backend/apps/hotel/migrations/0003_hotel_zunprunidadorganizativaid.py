# Generated by Django 3.2.2 on 2021-06-14 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0002_alter_hotel_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='zunPrUnidadOrganizativaId',
            field=models.IntegerField(default=0),
        ),
    ]