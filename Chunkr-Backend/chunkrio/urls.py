from django.urls import path
from . import views

app_name = "chunkrio"

urlpatterns = [
    path('', views.home, name='chunkrio-home'),
    path('documentation/', views.documentation, name='chunkr-documentation'),
    path('userprofile/', views.userprofile, name='chunkr-userprofile'),
]