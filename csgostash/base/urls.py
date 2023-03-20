from django.urls import path
from . import views 


urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),

    path('', views.home, name="home"),
    path('rifles/', views.rifles, name="rifles"),
    path('knives/', views.knives, name="knives"),
    path('pistols/', views.pistols, name="pistols"),
    path('smg/', views.smg, name="smg"),
    path('cases/', views.cases, name="cases"),
    path('stickers/', views.stickers, name="stickers"),
    path('heavy/', views.heavy, name="heavy"),
    path('gloves/', views.gloves, name="gloves"),
    path('rifles/<str:weapon>/', views.existing_skins, name="existing_skins"),
    path('rifles/<str:weapon>/<int:pk>', views.current_rifle, name="current_rifle"),
    path('sell-item/', views.sell_item, name='sell-item'),
    path('update-item/<int:pk>', views.update_item, name='update-item'),
    path('delete-item/<int:pk>', views.delete_item, name='delete-item'),
    
]
