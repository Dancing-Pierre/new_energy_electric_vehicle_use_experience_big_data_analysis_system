# Generated by Django 3.2.13 on 2023-03-19 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_car', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newenergycar',
            name='max_price',
            field=models.FloatField(blank=True, max_length=200, null=True, verbose_name='最高价格'),
        ),
        migrations.AlterField(
            model_name='newenergycar',
            name='min_price',
            field=models.FloatField(blank=True, max_length=200, null=True, verbose_name='最低价格'),
        ),
    ]
