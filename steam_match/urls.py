from django.urls import path

from . import views

urlpatterns = [
    path('', views.matcher, name='matcher'),
]