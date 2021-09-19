from django.contrib import admin

from api_project.models import Image, TemporaryUrl

admin.site.register([Image, TemporaryUrl])
