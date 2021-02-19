from django.db import models
from django.conf import settings



class Service(models.Model):
    image = models.ImageField(upload_to = 'media')
    title = models.CharField(max_length=100)
    price = models.FloatField()
    short_dis = models.TextField(null=True, blank=True)
    discription = models.TextField()
    documents  = models.TextField(null=True,blank=True)
    time = models.CharField(max_length=20)



class UserDetail(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=12)
    message = models.TextField()
    ref_code = models.CharField(max_length=20,null=True,blank=True)