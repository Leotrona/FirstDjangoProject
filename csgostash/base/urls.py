from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('home/csgo/ak47/', views.ak47, name="ak47"),
]