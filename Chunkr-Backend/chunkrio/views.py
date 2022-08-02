from django.shortcuts import render,redirect



# Create your views here.
def home(request):
    return render(request, 'home.html')

def documentation(request):
    return render(request, 'doc.html')

def userprofile(request):
    return render(request, 'profile.html')

