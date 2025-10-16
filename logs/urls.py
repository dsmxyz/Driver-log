from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('login/', auth_views.LoginView.as_view(template_name='logs/login.html'), name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('logs/', views.log_list, name='log_list'),
    path('logs/create/', views.log_create, name='log_create'),
    path('logs/<int:pk>/', views.log_detail, name='log_detail'),
    path('logs/<int:pk>/edit/', views.log_update, name='log_update'),
]