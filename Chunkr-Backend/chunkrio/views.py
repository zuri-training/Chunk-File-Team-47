from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def documentation(request):
    return render(request, 'doc.html')

def userprofile(request):
    return render(request, 'profile.html')