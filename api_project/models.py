from django.db import models
from django.contrib.auth.models import User


class Image(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/images')


