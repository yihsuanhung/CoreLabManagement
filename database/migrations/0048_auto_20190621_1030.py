# Generated by Django 2.2 on 2019-06-21 02:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0047_card_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='uid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.Person'),
        ),
    ]
