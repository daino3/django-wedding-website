from __future__ import unicode_literals

from django.db import models
from django.core.files.storage import FileSystemStorage

# Create your models here.

class Photo(models.Model):
    description = models.CharField(max_length=500, null=True)
    name = models.CharField(max_length=250, null=False)

    photo = models.ImageField(upload_to='photos', max_length=200, storage=FileSystemStorage())
    # timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

