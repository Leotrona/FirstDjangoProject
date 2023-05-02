from django.urls import path
from . import views 


urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),

    path('', views.home, name="home"),
    path('sell-item/', views.sell_item, name='sell-item'),
    path('<str:type>/', views.weapons, name="type"),
    path('<str:type>/<str:weapon>/', views.existing_skins, name="existing_skins"),
    path('<str:type>/<str:weapon>/<int:pk>', views.current_rifle, name="current_rifle"),
    path('update-item/<int:pk>', views.update_item, name='update-item'),
    path('delete-item/<int:pk>', views.delete_item, name='delete-item'),
    
]
