# Generated by Django 2.2 on 2019-05-07 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0012_auto_20190505_2323'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pi',
            name='card',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='card',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='card_PI',
        ),
        migrations.AddField(
            model_name='card',
            name='card_PI',
            field=models.CharField(default='tsai', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='access_card',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
