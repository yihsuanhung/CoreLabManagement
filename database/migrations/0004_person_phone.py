# Generated by Django 2.2 on 2019-05-02 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0003_remove_person_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='phone',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
