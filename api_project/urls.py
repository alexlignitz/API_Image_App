from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api_project.views import ImageViewSet

router = DefaultRouter()
router.register('image', ImageViewSet, basename='image')

urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
]