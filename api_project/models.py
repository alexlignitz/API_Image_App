from django.db import models
from django.contrib.auth.models import User
from django.db.models import Model
from sorl.thumbnail import ImageField


def nameFile(instance, filename):
    return '/'.join(['media', str(instance.title), filename])


class Image(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = ImageField(upload_to=nameFile)
