# Generated by Django 2.2 on 2019-06-20 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0039_auto_20190620_1517'),
    ]

    operations = [
        migrations.RenameField(
            model_name='card',
            old_name='card_return_date',
            new_name='return_date',
        ),
    ]
