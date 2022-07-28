from django.db import models

# Create your models here.
class File(models.Model):
    csv = models.FileField()
    json = models.FileField()


class Meta:
        abstract = True

