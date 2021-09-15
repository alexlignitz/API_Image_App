from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from sorl_thumbnail_serializer.fields import HyperlinkedSorlImageField

from .models import Image


class ImageSerializer(ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    thumbnail200 = HyperlinkedSorlImageField('200x200', source='image',
                                             read_only=True)
    thumbnail400 = HyperlinkedSorlImageField('400x400', source='image',
                                             read_only=True)

    class Meta:
        model = Image
        fields = ['id', 'title', 'image', 'author', 'thumbnail200', 'thumbnail400']
