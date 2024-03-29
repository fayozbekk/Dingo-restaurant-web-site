# Generated by Django 4.2.5 on 2023-10-03 08:10

import dingoapp.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dingoapp', '0003_chefmodel_alter_foodmodel_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookingModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Name')),
                ('email', models.EmailField(blank=True, max_length=250, null=True, verbose_name='Email')),
                ('num_of_g', models.IntegerField(verbose_name='Number of guests')),
                ('phone_number', models.CharField(max_length=15, verbose_name='Phone number')),
                ('date', models.DateField(validators=[dingoapp.models.past_date_validator], verbose_name='Date')),
                ('time', models.TimeField(verbose_name='Time')),
                ('note', models.TextField(blank=True, null=True, verbose_name='Note')),
            ],
        ),
        migrations.CreateModel(
            name='ChefLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ch_level', models.CharField(max_length=70, verbose_name='Chef level')),
            ],
        ),
        migrations.CreateModel(
            name='Chefs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255, verbose_name='Full name')),
                ('picture', models.ImageField(upload_to='chef/', verbose_name='Picture')),
                ('facebook', models.URLField(blank=True, default='#', null=True, verbose_name='Facebook')),
                ('x_twitter', models.URLField(blank=True, default='#', null=True, verbose_name='X')),
                ('instagram', models.URLField(blank=True, default='#', null=True, verbose_name='Instagram')),
                ('skype', models.URLField(blank=True, default='#', null=True, verbose_name='Skype')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dingoapp.cheflevel')),
            ],
            options={
                'verbose_name': 'Chef',
                'verbose_name_plural': 'Chefs',
            },
        ),
        migrations.DeleteModel(
            name='ChefModel',
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['created'], 'verbose_name': 'Category', 'verbose_name_plural': 'CCategories'},
        ),
        migrations.AlterField(
            model_name='foodmodel',
            name='picture',
            field=models.ImageField(upload_to='food/'),
        ),
    ]
