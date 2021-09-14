from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Image


class ImageSerializer(ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Image
        fields = ['id', 'title', 'image', 'author']
