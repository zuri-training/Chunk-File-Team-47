from django.db import models
from datetime import datetime
from django.contrib.auth import get_user_model
User = get_user_model()

class File(models.Model):
    name = models.CharField(max_length=150, null=True)
    file = models.FileField(upload_to="uploads/user-files")
    processed_file = models.FileField(upload_to="uploads/processed-files",null=True,blank=True, default='SOME STRING')
    file_type = models.CharField(max_length=50, null=True)
    file_size = models.CharField(max_length=50, null=True)
    chunk_number = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now, blank=True)
