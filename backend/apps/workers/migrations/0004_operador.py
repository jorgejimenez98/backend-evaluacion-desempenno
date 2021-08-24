# Generated by Django 3.2.2 on 2021-06-15 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0003_auto_20210615_0153'),
    ]

    operations = [
        migrations.CreateModel(
            name='Operador',
            fields=[
                ('id_oper', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30, unique=True)),
                ('descripcion', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
