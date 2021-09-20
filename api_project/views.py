import datetime

import pytz
from django.utils.timezone import now, utc
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import DjangoModelPermissions

from api_project.models import Image, TemporaryUrl
from api_project.serializers import BasicAccountSerializer, PremiumAccountSerializer, EnterpriseAccountSerializer, \
    TempUrlViewSerializer


class ImageViewSet(viewsets.ModelViewSet):
    """"
        Provides access to image list/upload/update/deletion depending on the user account type (see get_serializer_class).
    """

    def get_queryset(self):
        author = self.request.user
        if author.is_superuser:
            images = Image.objects.all()
        else:
            images = Image.objects.filter(author=author)
        return images

    def get_serializer_class(self):
        user = self.request.user

        if user.groups.filter(name='Basic').exists():
            return BasicAccountSerializer
        elif user.groups.filter(name='Premium').exists():
            return PremiumAccountSerializer
        elif user.groups.filter(name='Enterprise').exists() or user.is_superuser:
            return EnterpriseAccountSerializer

    serializer_class = get_serializer_class
    queryset = get_queryset
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [DjangoModelPermissions]


class TempUrlViewSet(viewsets.ModelViewSet):
    """"
        Provides access to temporary links list/upload/deletion depending on the user account type (see get_serializer_class).
    """

    def get_author_links(self):
        author = self.request.user
        if author.is_superuser:
            links = TemporaryUrl.objects.all()
            return links
        else:
            links = TemporaryUrl.objects.filter(author=author)
            return links

    def get_queryset(self):
        queryset = self.get_author_links()
        for link in queryset:
            exp_sec = link.created.replace(tzinfo=pytz.UTC)
            exp_date = exp_sec + datetime.timedelta(seconds=link.expires)
            time_now = now()
            if exp_date <= time_now:
                link.delete()
        return queryset.filter(is_active=True)

    def get_serializer_class(self):
        user = self.request.user
        if user.groups.filter(name='Enterprise').exists() or user.is_superuser:
            return TempUrlViewSerializer
        else:
            raise PermissionError('Access denied')

    serializer_class = get_serializer_class
    queryset = get_queryset
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [DjangoModelPermissions]
