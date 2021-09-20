from django.core.exceptions import ValidationError
from rest_framework import serializers
from sorl_thumbnail_serializer.fields import HyperlinkedSorlImageField

from .models import Image, TemporaryUrl

author = serializers.HiddenField(default=serializers.CurrentUserDefault())


class BasicAccountSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(write_only=True)
    author = author

    thumbnail200 = HyperlinkedSorlImageField('200x200', source='image', read_only=True)

    class Meta:
        model = Image
        fields = ['id', 'title', 'author', 'image', 'thumbnail200']


class PremiumAccountSerializer(serializers.ModelSerializer):
    author = author

    thumbnail200 = HyperlinkedSorlImageField('200x200', source='image', read_only=True)
    thumbnail400 = HyperlinkedSorlImageField('400x400', source='image', read_only=True)

    class Meta:
        model = Image
        fields = ['id', 'title', 'image', 'author', 'thumbnail200', 'thumbnail400']


class EnterpriseAccountSerializer(serializers.ModelSerializer):
    author = author

    thumbnail200 = HyperlinkedSorlImageField('200x200', source='image', read_only=True)
    thumbnail400 = HyperlinkedSorlImageField('400x400', source='image', read_only=True)

    class Meta:
        model = Image
        fields = ['id', 'title', 'image', 'author', 'thumbnail200', 'thumbnail400']


class TempUrlViewSerializer(serializers.ModelSerializer):
    image_id = serializers.IntegerField(write_only=True)
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    temp_url = serializers.SerializerMethodField('create_url', read_only=True)
    created = serializers.DateTimeField(read_only=True)
    expires = serializers.IntegerField(write_only=True, required=True)
    is_active = serializers.BooleanField(read_only=True)

    def validate_expires(self, value):
        if value < 300 or value > 3000:
            raise ValidationError('Expiration time must be between 300 and 3000 seconds')
        return value

    class Meta:
        model = TemporaryUrl
        fields = ['id', 'image_id', 'author', 'temp_url', 'created', 'expires', 'is_active']

    def create_url(self, obj):
        request = self.context.get("request")
        image_obj_url = Image.objects.get(pk=obj.image_id).image.url
        return request.build_absolute_uri(image_obj_url)


