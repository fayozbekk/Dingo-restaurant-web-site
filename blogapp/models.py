from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class User(AbstractUser):
    avatar = models.ImageField(upload_to='users/avatar')

    def __str__(self):
        return self.username


class Category(models.Model):
    category_name = models.CharField(max_length=155)

    def __str__(self):
        return self.category_name


class Comments(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    message = models.TextField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    best_comment = models.BooleanField(default=False)

    def __str__(self):
        return self.message[:10]


class Post(models.Model):
    title = models.CharField(max_length=215)
    content = models.TextField()
    category = models.ManyToManyField(Category)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    image = models.ImageField(upload_to='blog/')
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolut_url(self) -> str:
        return f'block/{self.id}'
