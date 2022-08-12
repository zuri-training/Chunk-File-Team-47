from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


# app_name = "chunkrio"

urlpatterns = [
    path('', views.home, name='home'),
    path('documentation/', views.documentation, name='documentation'),
    path('userprofile/', views.userProfile, name='userprofile'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name="logout"),
    path('password_reset', views.password_reset_request, name="password_reset"),
    path("save_file", views.save_file, name="save_file"),
    path("download/<str:file_id>", views.download, name="download"),
    path('delete/<int:pk>/', views.file_delete, name="delete"),
    path('history/<int:pk>/', views.history, name="history"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),     
]

