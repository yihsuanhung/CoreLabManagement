# Generated by Django 2.2 on 2019-05-02 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0007_auto_20190502_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pi',
            name='card',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='pi',
            name='culture_room',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='pi',
            name='hazardous_chemicals',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='pi',
            name='toxic_chenicals',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='staff',
            name='card',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='staff',
            name='culture_room',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='staff',
            name='permanent',
            field=models.BooleanField(),
        ),
    ]