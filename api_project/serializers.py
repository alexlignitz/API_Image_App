import datetime

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
    expires = serializers.IntegerField(write_only=True)
    exp_date = serializers.SerializerMethodField('get_exp_date', read_only=True)

    class Meta:
        model = TemporaryUrl
        fields = ['image_id', 'author', 'temp_url', 'created', 'expires', 'exp_date']

    def create_url(self, obj):
        request = self.context.get("request")
        image_obj_url = Image.objects.get(pk=obj.image_id).image.url
        return request.build_absolute_uri(image_obj_url)

    def get_exp_date(self, obj):
        exp_sec = obj.created.replace(tzinfo=None)
        exp_date = exp_sec + datetime.timedelta(hours=2, seconds=obj.expires)
        return exp_date
