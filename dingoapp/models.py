from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
import datetime


class TagModel(models.Model):
    tag = models.CharField('Tag', max_length=100)

    def __str__(self):
        return self.tag


class FoodModel(models.Model):
    title = models.CharField(verbose_name='Title', max_length=155)
    about = models.TextField(verbose_name='About')
    exclusive = models.BooleanField(verbose_name='Exclusive', default=False)
    price = models.FloatField(verbose_name='Price',
                              validators=(
                                  MinValueValidator(0),
                                  MaxValueValidator(999)
                              ))
    picture = models.ImageField(upload_to='food/')
    created = models.DateTimeField(verbose_name='Created', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Updated', auto_now=True)
    category = models.ManyToManyField('Category', verbose_name='Category')
    tags = models.ManyToManyField(TagModel, verbose_name='Tags', blank=True)


class Category(models.Model):
    category_name = models.CharField('Category name', max_length=150)
    created = models.DateTimeField(verbose_name='Created', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Updated', auto_now=True)

    def __str__(self):
        return self.category_name

    class Meta:
        ordering = ['created']
        verbose_name = 'Category'
        verbose_name_plural = 'CCategories'


class ChefLevel(models.Model):
    ch_level = models.CharField(verbose_name='Chef level', max_length=70)

    def __str__(self):
        return self.ch_level


class Chefs(models.Model):
    full_name = models.CharField('Full name', max_length=255)
    picture = models.ImageField(verbose_name='Picture', upload_to='chef/')
    level = models.ForeignKey(to=ChefLevel, on_delete=models.CASCADE)
    facebook = models.URLField(verbose_name="Facebook", blank=True, null=True, default='#')
    x_twitter = models.URLField(verbose_name="X", blank=True, null=True, default='#')
    instagram = models.URLField(verbose_name="Instagram", blank=True, null=True, default='#')
    skype = models.URLField(verbose_name="Skype", blank=True, null=True, default='#')

    class Meta:
        verbose_name = "Chef"
        verbose_name_plural = "Chefs"


def past_date_validator(value):
    if value < datetime.date.today():
        raise ValidationError('The date cannot be in the past.')
    return value


def past_time_validator(value):
    current_time = datetime.datetime.now()

    if value.hour < current_time.hour and current_time.date() == datetime.date.today():
        raise ValidationError('The date cannot be in the past.')
    return str(value.hour)


class BookingModel(models.Model):
    name = models.CharField(verbose_name='Name', max_length=250)
    email = models.EmailField(verbose_name='Email', max_length=250, blank=True, null=True)
    num_of_g = models.IntegerField(verbose_name='Number of guests')
    phone_number = models.CharField(verbose_name='Phone number', max_length=15)
    date = models.DateField(verbose_name='Date', validators=[past_date_validator])
    time = models.TimeField(verbose_name='Time', validators=[past_time_validator])
    note = models.TextField(verbose_name='Note', blank=True, null=True)

    def __str__(self):
        return self.name
