# cities/models.py
from django.core.exceptions import ValidationError
from django.db import models
import uuid
from django import forms
from django.db import models
import json
from django.conf import settings
from datetime import datetime
from django.contrib.auth.models import User
class Auth(models.Model):
    auth = models.CharField(max_length=64)

    def __str__(self):
      return self.auth
class UserAuths(models.Model):
    ## should probably define  custom user model
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    authorizations = models.ManyToManyField(Auth)

import os
def update_filename(instance, filename):
    ext = filename
    filename = "%s_%s" % (instance.uuid, ext)
    instance.originalfile = ext
    instance.filename = filename
    instance.status = "NEW"
    return os.path.join('files', filename)

class FileUpload(models.Model):
    filename = models.CharField(max_length=2550)
    originalfile = models.CharField(max_length=2550,default="")
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    status = models.CharField(max_length=20, default="NEW")
    document = models.FileField(null=True, blank=True,upload_to=update_filename)
    
    def __str__(self):
      return self.uuid + "." +  filename  

class AccumuloCluster(models.Model):
     instance = models.CharField(max_length=255)
     zookeeper = models.CharField(max_length=1024)
     user = models.CharField(max_length=255)
     password = models.CharField(max_length=255)
  
     def save(self, *args, **kwargs):
        if not self.pk and AccumuloCluster.objects.exists():
        # if you'll not check for self.pk 
        # then error will also raised in update of exists model
            raise ValidationError('There is can be only one AccumuloCluster instance')
        return super(AccumuloCluster, self).save(*args, **kwargs)

     def __str__(self):
      return self.instance + "@" + self.zookeeper

class Query(models.Model):
    name = models.CharField(max_length=2550)

    class Meta:
      verbose_name_plural = "queries"

    def __str__(self):
      return self.name