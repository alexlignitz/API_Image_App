from django.contrib.auth.models import User
from rest_framework import serializers
from sorl_thumbnail_serializer.fields import HyperlinkedSorlImageField

from .models import Image, TemporaryUrl


class BasicAccountSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(write_only=True)
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    thumbnail200 = HyperlinkedSorlImageField('200x200', source='image', read_only=True)

    class Meta:
        model = Image
        fields = ['id', 'title', 'author', 'image', 'thumbnail200']


class PremiumAccountSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    thumbnail200 = HyperlinkedSorlImageField('200x200', source='image', read_only=True)
    thumbnail400 = HyperlinkedSorlImageField('400x400', source='image', read_only=True)

    class Meta:
        model = Image
        fields = ['id', 'title', 'image', 'author', 'thumbnail200', 'thumbnail400']


class EnterpriseAccountSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    thumbnail200 = HyperlinkedSorlImageField('200x200', source='image', read_only=True)
    thumbnail400 = HyperlinkedSorlImageField('400x400', source='image', read_only=True)

    class Meta:
        model = Image
        fields = ['id', 'title', 'image', 'author', 'thumbnail200', 'thumbnail400']


class TempUrlViewSerializer(serializers.ModelSerializer):
    image = serializers.IntegerField()
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    temp_url = serializers.HiddenField(default=None)
    expires = serializers.IntegerField()

    class Meta:
        model = TemporaryUrl
        fields = ['image', 'author', 'temp_url', 'expires']