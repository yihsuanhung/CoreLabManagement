# Generated by Django 2.2 on 2019-05-05 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0011_auto_20190503_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='card_ID',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='card',
            name='receipt',
            field=models.CharField(max_length=9),
        ),
    ]
