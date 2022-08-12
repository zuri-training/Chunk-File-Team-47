from django.shortcuts import render,redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.conf import settings
from . models import File
import pandas as pd
import shutil
import time
import os


# Create your views here.
def home(request):
    return render(request, 'home.html')

def documentation(request):
    return render(request, 'doc.html')

@login_required()
def userProfile(request):
    return render(request, 'profile.html')


@login_required()
def download(request, file_id):
    file = File.objects.filter(id=file_id).first()
    context = {"file":file}
    return render(request, 'dashboard-chunk.html',context)

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



# Reset password
def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "password_reset_email.txt"
					c = {
					"email": [user.email],
					'domain':'127.0.0.1:8000',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'alukoayomide623@gmail.com' , ['alukoayomide623@gmail.com'], fail_silently=False)
					except BadHeaderError:

						return HttpResponse('Invalid header found.')
						
					messages.success(request, 'A message with reset password instructions has been sent to your inbox.')
					return redirect ("login")
			messages.error(request, 'An invalid email has been entered.')
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="password_reset.html", context={"password_reset_form":password_reset_form})

# Split Program
@login_required(login_url="login")
def save_file(request):
    files = File.objects.all().order_by("-id")
    context = {
        'files':files
    }
    if request.method == 'POST':
        name = request.POST.get("name")
        type = request.POST.get("type")
        file_data = request.FILES.get("file")
        #fSize = str(os.path.getsize(file_data))
        #print(fSize)
        file_count = request.POST.get("file_count") or 2
        file_count = int(file_count)
        print(type)
        user = request.user
        file = File.objects.create(file=file_data,chunk_number=file_count,user=user,name=name,file_type=type)
        url = file.file.url
        url = str(settings.BASE_DIR)+url.replace("/","\\")
        if url.split(".")[-1] not in ["json","csv"]:
            messages.error(request, "Please upload csv or json file")
            return redirect(request.META.get("HTTP_REFERER"))

        # ******************* CSV OPTION *****************************
        if url.split(".")[-1] == 'csv':
            df = pd.read_csv(url)
            rows_per_file = df.shape[0] // file_count
            folder_name = str(settings.BASE_DIR) + "\\temp\\" + str(int(time.time()*1000))
            os.makedirs(folder_name)
            for row_start in range(0, df.shape[0], rows_per_file):
                new_file  = df[row_start:row_start+rows_per_file]
                new_file.to_csv(f"{folder_name}/chunk_{row_start}.csv")

            outputfile = str(settings.MEDIA_ROOT) + f"\\processed-files\\{name}"
            shutil.make_archive(outputfile, 'zip', folder_name)
            file.processed_file = f"/processed-files/{name}.zip"
            file.save()
            return redirect("download", file.id)

        # ******************* JSON OPTION *****************************
        if url.split(".")[-1] == 'json':
            df = pd.read_json(url)
            rows_per_file = df.shape[0] // file_count
            folder_name = str(settings.BASE_DIR) + "\\temp\\" + str(int(time.time()*1000))
            os.makedirs(folder_name)
            for row_start in range(0, df.shape[0], rows_per_file):
                new_file  = df[row_start:row_start+rows_per_file]
                new_file.to_json(f"{folder_name}/chunk_{row_start}.json",indent=1,orient='records')

            outputfile = str(settings.MEDIA_ROOT) + f"\\processed-json-files\\folder_name"
            shutil.make_archive(outputfile, 'zip', folder_name)
            file.processed_file = f"/processed-json-files/folder_name.zip"
            file.save()
            return redirect("download", file.id) 
    return render(request,'save_file.html',context)
    
# ******************* DELETE FILES VIEW *****************************
def file_delete(request, pk):
    file = File.objects.get(id=pk)
    if request.method == 'POST':
        file.delete()
        return redirect('save_file')
    context = {
        'file':file
    }
    return render(request, "delete.html",context)

# ******************* HISTORY FILES VIEW *****************************
def history(request, pk):
    file = File.objects.get(id=pk)
    context = {
        'file':file
    }
    return render(request, "history.html",context)
