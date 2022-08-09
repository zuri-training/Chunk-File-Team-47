# from pickle import FALSE
# from django.http import HttpResponseRedirect
# from django.contrib.auth.forms import UserCreationForm
# from django.urls import reverse
# from zipfile import  ZipFile
# import pandas as pd
# import os
# from django.db.models import Q



from . import chunk_csv
from django.shortcuts import render,redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request, 'home.html')

def documentation(request):
    return render(request, 'doc.html')

@login_required()
def userProfile(request):
    return render(request, 'profile.html')

# @login_required()
def chunkForm(request):
    return render(request, 'chunk-form.html')


# User registration views
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account was created successfully, Sign in to your account')
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'register.html', {'form': form})


# Split Program

# def chunk_program(request):
#     if request.method == "POST":
#         file = request.FILES.get('file')
#         ouput_name = request.POST['file_name']
#         chunk_size = request.POST['chunk_size']
#         user = request.user
#         if chunk_size == '' or file == None:
#             messages.error(request, 'fields cannot be blank!')
#             return redirect('/')
       
#         if  file.name.endswith('csv'):
#             if output_name == '':
#                 output_name = file.name
    
#             chunk_size = int(chunk_size)
#             batch_no = 1
#             for chunk in pd.read_csv(file, chunksize=chunk_size):
#                 with ZipFile(f'media/{user}{output_name}-.zip', 'a') as zip_file:
#                     file_name = f"{output_name}-" + str(batch_no) + ".csv"
#                     zip_file.write(file_name,chunk.to_csv(file_name, index=False))
#                 os.remove(file_name)
#                 batch_no += 1
                
                
#             csv_obj = File.objects.create(user=user, file=f'{user}{ouput_name}-.zip')
#             csv_obj.save()
            
#             messages.info(request, 'Split completed!')
#             return redirect('/new_chunk')
        
#         messages.error(request, 'invalid file format')
#         return redirect('/split_form')
    
#     return render(request, 'chunk-form.html')


