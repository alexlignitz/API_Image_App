from django.db import models
from django.contrib.auth.models import User
from django.db.models import Model
from rest_framework.exceptions import ValidationError
from sorl.thumbnail import ImageField


def nameFile(instance, filename):
    return '/'.join(['media', str(instance.title), filename])


class Image(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = ImageField(upload_to=nameFile)


class TemporaryUrl(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    temp_url = models.CharField(blank=False, max_length=32)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    expires = models.IntegerField()

    def clean(self):
        if self.expires < 300 or self.expires > 3000:
            raise ValidationError('Expiration time must be between 300 and 3000 seconds')
