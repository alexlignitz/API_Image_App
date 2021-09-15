from django.db import models
from django.contrib.auth.models import User
from sorl.thumbnail import ImageField


class Image(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = ImageField(upload_to='media')

