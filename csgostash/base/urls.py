from django.urls import path
from . import views 


urlpatterns = [
    path('', views.home, name="home"),
    path('rifles/', views.rifles, name="rifles"),
    path('knives/', views.knives, name="knives"),
    path('pistols/', views.pistols, name="pistols"),
    path('smg/', views.smg, name="smg"),
    path('cases/', views.cases, name="cases"),
    path('stickers/', views.stickers, name="stickers"),
    path('heavy/', views.heavy, name="heavy"),
    path('gloves/', views.gloves, name="gloves"),
    path('rifles/ak47', views.ak47, name="ak47"),
    path('rifle/ak47/<int:id', views.current_rifle, name="current_rifle"),

]
