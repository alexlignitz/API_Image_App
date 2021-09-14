from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import DjangoModelPermissions

from api_project.models import Image
from api_project.serializers import ImageSerializer


# class ImageViewSet(viewsets.ViewSet):
#     authentication_classes = [SessionAuthentication, BasicAuthentication]
#     permission_classes = [DjangoModelPermissions]
#     queryset = Image.objects.all()
#     serializer_class = ImageSerializer
#
#     def list(self, request):
#         images = Image.objects.filter(author=request.user)
#         serializer = ImageSerializer(images, many=True)
#         return Response(serializer.data)
#
#     def create(self, request):
#         serializer = ImageSerializer(data=request.data)
#
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def retrieve(self, request, pk=None):
#         queryset = Image.objects.filter(author=request.user)
#         images = get_object_or_404(queryset)
#         serializer = ImageSerializer(images)
#         return Response(serializer.data)
#
#     def update(self, request, pk=None):
#         image = Image.objects.get(pk=pk)
#         serializer = ImageSerializer(image, data=request.data)
#
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk=None):
#         image = Image.objects.get(pk=pk)
#         image.delete()
#
#         images = Image.objects.filter(author=request.user)
#         serializer = ImageSerializer(images, many=True)
#         return Response(serializer.data)

class ImageViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        author = self.request.user
        images = Image.objects.filter(author=author)
        return images

    serializer_class = ImageSerializer
    queryset = get_queryset
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [DjangoModelPermissions]
