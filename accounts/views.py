from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from accounts.decorator import login_register_check
from accounts.models import profile
from django.contrib.auth import forms,login as authenticate,logout as deauthenticate

from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from accounts.form import userForm, userLogin, profileUpdate


# Create your views here.
@login_register_check(url = "/accounts/login/")
def register(req):
    if req.method=='POST':
        form = userForm(req.POST,req.FILES)
        if form.is_valid():
            print('form is valid')
            user = User.objects.create_user(username=req.POST['username'], password=req.POST['password'],
                                            first_name=req.POST['name'])
            user.profile.name = req.POST['name']
            user.profile.age = req.POST['age']
            user.profile.address = req.POST['address']
            user.profile.phone_no = req.POST['phone_no']
            user.profile.gender = req.POST['gender']
            user.profile.dp = req.FILES['dp']
            user.save()
            return  redirect('/accounts/login')
    else:
        form = userForm()
        print('errors',form.errors)
    return render(req,'singup.html',{'form':form})

@login_register_check(url = "/accounts/login")
def login(req):
    form = userLogin()
    if req.method=='POST':
        form=userLogin(req.POST)
        if form.is_valid():
            user = forms.authenticate(username=req.POST['username'], password=req.POST['password'])
            print('rakesh',user)
            if user is None:
                messages.info(req, 'username or password is not Validate')
                return redirect('/accounts/login')
            else:
                authenticate(req,user)
                return redirect('/blog/home')
    return render(req,'login.html',{'form':form})

@login_required(login_url='/accounts/login/')
def logout(req):
    if req.user.is_authenticated:
        deauthenticate(req)
        return redirect('/blog/home')


@login_required(login_url='/accounts/login')
def pro(req):
    print('profile',req.user)
    pro = profile.objects.get(user=req.user)
    return render(req,'profile.html',{'pro':pro})

@login_required(login_url='/accounts/login')
def edit(req, pk):
    # dictionary for initial data with
    # field names as keys
    context = {}
    # fetch the object related to passed id
    obj = get_object_or_404(profile, pk=pk)
    if req.method=='POST':
    # pass the object as instance in form
        form = profileUpdate(req.POST,req.FILES,instance=obj)
        # save the data from the form and
        # redirect to detail_view
        if form.is_valid():
            form.save()
            return redirect("/accounts/profile")
    else:
        form = profileUpdate(instance=obj)
        # add form dictionary to context
    context["profile"] = form
    return render(req,'profileUpdate.html',context)


