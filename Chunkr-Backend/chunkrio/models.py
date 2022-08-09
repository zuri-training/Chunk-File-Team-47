from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class File(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    zipped_file = models.FileField(upload_to="chunked_folder", blank= True)



class UploadedFile(models.Model):
    uploaded_file = models.FileField(upload_to="uploaded")