# Generated by Django 2.2 on 2019-06-10 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0022_auto_20190610_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='alt_mail',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='employee_ID',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
