from typing import Tuple
from django.db import models
from django.conf import settings
from django.utils import tree

User = settings.AUTH_USER_MODEL


class Service(models.Model):
    image = models.ImageField(upload_to = 'media')
    title = models.CharField(max_length=100)
    price = models.FloatField()
    short_dis = models.TextField(null=True, blank=True)
    discription = models.TextField()
    documents  = models.TextField(null=True,blank=True)
    time = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class UserDetail(models.Model):
    user = models.ForeignKey(User ,on_delete=models.SET_NULL,blank=True,null=True)
    username = models.CharField(max_length=20)
    email = models.EmailField(blank=True,null=True)
    mobile_number = models.CharField(max_length=12)
    message = models.TextField(null=True,blank=True)
    work = models.ManyToManyField(Service)
    ref_code = models.CharField(max_length=20,null=True,blank=True)
    timestamp = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    def __str__(self):
        return self.username