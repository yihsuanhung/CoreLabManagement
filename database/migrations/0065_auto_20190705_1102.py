# Generated by Django 2.2 on 2019-07-05 03:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0064_staff_card'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='card_pi',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='card_pi_name',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='pi',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='pi_name',
        ),
    ]
