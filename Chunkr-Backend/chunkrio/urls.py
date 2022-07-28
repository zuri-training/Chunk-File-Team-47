from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='chunkrio-home'),
    path('documentation/', views.documentation, name='chunkr-documentation'),
    path('userprofile/', views.userprofile, name='chunkr-userprofile'),
]