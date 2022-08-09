from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import UploadedFile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ChunkForm(forms.Form):
    # the chunk size is to determine how the file is going to be chunked
    file = forms.FileField()
    chunk_size = forms.IntegerField()


class UploadFileForm(forms.Form):
    # title = forms.CharField(max_length=50)
    class Meta:
        model = UploadedFile