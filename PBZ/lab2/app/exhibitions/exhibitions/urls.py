
from django.contrib import admin
from django.urls import path
from django.shortcuts import redirect

from main import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', lambda request: redirect('exhibits/', permanent=False)),
    path("exhibits/", views.exhibits),
    path("exhibition_halls/", views.exhibition_halls),
    path("exhibitions/", views.exhibitions)
]
