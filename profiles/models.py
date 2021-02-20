from django.db import models
from django.conf import settings
from django.db.models.signals import post_save



User = settings.AUTH_USER_MODEL


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    ref_code = models.CharField(max_length=20)
    image = models.ImageField(upload_to ='media',default='media/unnamed.png')  

    def __str__(self):
        return self.user.username
# get data from user class using singnals
def user_did_save(sender,instance,created,*args,**kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)
post_save.connect(user_did_save,sender=User)


