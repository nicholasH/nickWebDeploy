from django.urls import path,re_path

from . import views

urlpatterns = [
    path('<str:steam_id>', views.friendSelector, name="friendSelector"),
    path('', views.matcher, name='matcher'),
]