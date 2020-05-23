from django import forms
from accounts.models import profile
from django.core import validators
from accounts.validator import  validator

class userForm(forms.ModelForm):
    username = forms.CharField(max_length=100,validators=[validator.username],widget=forms.TextInput(attrs={'class':'input-text','placeholder':'Enter Email'}))
    name = forms.CharField(max_length=100,validators=[validator.name],widget=forms.TextInput(attrs={'class':'input-text','placeholder':'Enter your name'}))
    password = forms.CharField(max_length=26,widget=forms.PasswordInput(attrs={'class':'input-text','placeholder':'Enter Password'}))
    confirm_password = forms.CharField(max_length=26,widget=forms.PasswordInput(attrs={'class':'input-text','placeholder':'Enter Confirm-Password'}))
    class Meta:
        model = profile
        fields = ['name','username','password','confirm_password','age','address','gender','phone_no','dp']
        widgets = {
            'age': forms.TextInput(attrs={'class': 'input-text', 'placeholder': 'Enter Age'}),
            'address': forms.TextInput(attrs={'class': 'input-text', 'placeholder': 'Address'}),
            'gender': forms.Select(attrs={'class': 'selectpicker search-fields'}),
            'phone_no':forms.TextInput(attrs={'class':'input-text','placeholder':'Enter mobile number'})
        }
    def clean(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password == confirm_password:
            if not len(password)>=6:
                raise validators.ValidationError('Password length is less then 6')
            return self.cleaned_data
        else:

            raise validators.ValidationError('Password and confirm_password does not match')



class userLogin( forms.ModelForm):
    username = forms.CharField(max_length=100,validators=[validator.username],widget=forms.TextInput(attrs={'class':'input-text','placeholder':'Enter Email'}))
    password = forms.CharField(max_length=26,widget=forms.PasswordInput(attrs={'class':'input-text','placeholder':'Enter Password'}))
    class Meta:
        model = profile
        fields = ['username','password']

    def clean(self):
        password = self.cleaned_data.get('password')
        if not len(password)>=6:
            raise validators.ValidationError('Password length is less then 6')
        return self.cleaned_data

class profileUpdate(forms.ModelForm):
    class Meta:
        model = profile
        fields = ['id','name','age', 'address', 'gender', 'phone_no', 'dp']
        widgets = {
            'age': forms.TextInput(attrs={'class': 'input-text', 'placeholder': 'Enter Age'}),
            'address': forms.TextInput(attrs={'class': 'input-text', 'placeholder': 'Address'}),
            'gender': forms.Select(attrs={'class': 'selectpicker search-fields'}),
            'phone_no': forms.TextInput(attrs={'class': 'input-text', 'placeholder': 'Enter mobile number'})
        }




