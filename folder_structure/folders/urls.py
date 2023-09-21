from django.urls import path
from . import views

urlpatterns = [
    path('folders', views.folder_list, name='folder_list'),    
    path('',views.register_page, name='register'),
    path('login',views.login_page, name='login'),
    path('create/', views.folder_create, name='folder_create'),
    path('create/<int:parent_id>/', views.folder_create, name='subfolder_create'),
]
