from django.urls import path
from . import views
from django.contrib.auth import views as auth_view


# app_name = "chunkrio"

urlpatterns = [
    path('', views.home, name='home'),
    path('documentation/', views.documentation, name='documentation'),
    path('userprofile/', views.userProfile, name='userprofile'),
    path('register/', views.register, name='register'),
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name="login"),
    path('logout/', auth_view.LogoutView.as_view(template_name='logout.html'), name="logout"),
]

