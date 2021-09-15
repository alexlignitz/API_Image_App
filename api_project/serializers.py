from rest_framework import serializers
from sorl_thumbnail_serializer.fields import HyperlinkedSorlImageField

from .models import Image


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

# def get_thumbnail200(self, obj):
#     groups = Group.objects.all()
#     if self.author in groups:
#         thumbnail200 = get_thumbnail(self.thumbnail200, '200x200', source='image', read_only=True)
#         return thumbnail200
#     else:
#         return PermissionError
#
# def get_thumbnail400(self, obj):
#     premium = Group.objects.filter(name="Premium")
#     enterprise = Group.objects.filter(name="Enterprise")
#     if self.author in premium or self.author in enterprise:
#         thumbnail400 = HyperlinkedSorlImageField('400x400', source='image', read_only=True)
#         return thumbnail400
#     else:
#         return PermissionError
