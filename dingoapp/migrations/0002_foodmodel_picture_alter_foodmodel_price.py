# Generated by Django 4.2.5 on 2023-09-22 09:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dingoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodmodel',
            name='picture',
            field=models.ImageField(default='static/img/Quote.png', upload_to='food/'),
        ),
        migrations.AlterField(
            model_name='foodmodel',
            name='price',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(999)], verbose_name='Price'),
        ),
    ]
