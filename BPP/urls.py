from django.contrib import admin
from django.urls import path,include

from BPP import views

urlpatterns = [
    path('apis/v1', views.Home), # https://goddamncoders.pythonanywhere.com/apis/v1/search

]
