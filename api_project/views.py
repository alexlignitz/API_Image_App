from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import DjangoModelPermissions

from api_project.models import Image
from api_project.serializers import BasicAccountSerializer, PremiumAccountSerializer, EnterpriseAccountSerializer


class ImageViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        author = self.request.user
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





