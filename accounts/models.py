from django.contrib.auth.models import User
from django.db import models
from django.core import validators

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core import validators
from accounts.validator import validator


class profile(models.Model):
    user = models.OneToOneField(to=User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200,validators=[validator.name])
    age =  models.IntegerField(default=18, validators=[validators.MinValueValidator(18),validators.MaxValueValidator(60)])
    address = models.CharField(max_length=200)
    gender = models.CharField(max_length=20,default='Female',choices=(('Male','Male'),('Female','Female')))
    phone_no = models.CharField(max_length=15,validators=[validators.RegexValidator('^0?[5-9]{1}\d{9}$')])
    dp = models.ImageField(upload_to='image/')

    def __str__(self):
        return self.name

@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        if instance.is_superuser:
            pass
        else:
            profile.objects.create(user=instance)

@receiver(post_save,sender = User)
def save_user_profile(sender,instance,**kwargs):
    if instance.is_superuser:
        pass
    else:
        instance.profile.save()