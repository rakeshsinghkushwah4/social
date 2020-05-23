from django.contrib.auth.models import User
from django.db import models
from accounts.models import profile

# Create your models here.

class post(models.Model):
    subject = models.CharField(max_length=250)
    msg = models.TextField()
    cr_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='image/',null=True ,blank=True)
    uploaded_by =models.ForeignKey(to=profile, on_delete=models.CASCADE)
    def __str__(self):
        return self.subject

class comment(models.Model):
    post = models.ForeignKey(to=post,on_delete=models.CASCADE)
    msg  = models.CharField(max_length=250)
    comment_by  = models.ForeignKey(to=User,on_delete=models.CASCADE)
    cr_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.msg

class like(models.Model):
    post = models.ForeignKey(to=post,on_delete=models.CASCADE)
    like_by = models.ForeignKey(to=User,on_delete=models.CASCADE)
    cr_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.like_by)

class Follow(models.Model):
    profile = models.ForeignKey(to=profile,on_delete=models.CASCADE,related_name='profile')
    follow_by = models.ForeignKey(to=User,on_delete=models.CASCADE,related_name='follows_by')
    print(profile)
    def __str__(self):
        return str(self.profile)




