from django import forms
from blog.models import post

class createPostform(forms.ModelForm):
    class Meta:
        model = post
        fields = ['subject','msg','image']