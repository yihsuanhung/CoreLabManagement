# Generated by Django 2.2 on 2019-06-20 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0041_auto_20190620_1519'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='receive_date',
        ),
        migrations.RemoveField(
            model_name='card',
            name='return_date',
        ),
        migrations.AlterField(
            model_name='card',
            name='receipt',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
