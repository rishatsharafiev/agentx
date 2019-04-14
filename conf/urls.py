"""Urls"""

from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('geo/', include('apps.geo.urls')),
]
