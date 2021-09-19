from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api_project.views import ImageViewSet, TempUrlViewSet

from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register('image', ImageViewSet, basename='image')
router.register(r'temp_url', TempUrlViewSet, basename='temp_url')

urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
    path('viewset/<int:pk>/<int:exp>/', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)