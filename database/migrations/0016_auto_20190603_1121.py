# Generated by Django 2.2 on 2019-06-03 03:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0015_auto_20190603_1121'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staff',
            old_name='PI',
            new_name='pi',
        ),
    ]
