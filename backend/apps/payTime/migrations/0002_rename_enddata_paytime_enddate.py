# Generated by Django 3.2.2 on 2021-06-22 21:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payTime', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paytime',
            old_name='endData',
            new_name='endDate',
        ),
    ]
