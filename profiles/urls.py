from django.contrib import admin
from django.urls import path

from profiles import views

urlpatterns = [
    path('', views.profile_list, name='profile_list')
]
