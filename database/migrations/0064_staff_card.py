# Generated by Django 2.2 on 2019-07-04 03:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0063_auto_20190704_1057'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='card',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='card_RAs', to='database.PI', verbose_name='門禁PI'),
        ),
    ]