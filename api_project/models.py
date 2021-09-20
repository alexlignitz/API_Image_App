from datetime import timedelta
from django.utils.timezone import now

from django.db import models
from django.contrib.auth.models import User
from django.db.models import Model
from django.http import HttpResponse
from rest_framework.exceptions import ValidationError
from sorl.thumbnail import ImageField


def nameFile(instance, filename):
    return '/'.join(['media', str(instance.title), filename])


class Image(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Author')
    title = models.CharField(max_length=100, verbose_name='Image title')
    image = ImageField(upload_to=nameFile, verbose_name='Original image')


class TemporaryUrl(models.Model):
    image_id = models.IntegerField(verbose_name='Image ID')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Author')
    temp_url = models.URLField(max_length=100, null=True, verbose_name='Temporary Link')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')
    expires = models.IntegerField(verbose_name='Seconds to expire')

    def clean(self):
        if self.expires < 300 or self.expires > 3000:
            raise ValidationError('Expiration time must be between 300 and 3000 seconds')

    def calculate_exp_date(self):
        time = self.created.replace(tzinfo=None)
        exp_date = time + timedelta(hours=2, seconds=self.expires)
        return exp_date

    @property
    def delete_when_expired(self):
        query = TemporaryUrl.objects.get(pk=self.id)
        exp_date = self.calculate_exp_date
        while True:
            if exp_date >= now():
                query.delete()
                return HttpResponse('Link expired')

