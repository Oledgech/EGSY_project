from django.urls import path

from . import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="index"),
    path("export/", views.export, name="export"),
    path("search/", views.search, name="search"),
    path("full/", views.full, name="full"),
    path("year/", views.year, name="year"),
]