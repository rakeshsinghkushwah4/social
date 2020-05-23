from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render,redirect
from blog.form import createPostform
from blog.models import post,Follow,like,comment
from accounts.models import profile


# Create your views here.
def home(req):
    pl= None
    if req.user.is_authenticated:
        list = Follow.objects.filter(follow_by=req.user)
        print(list)
        pl =[]
        for e in list:
            posts=post.objects.filter(uploaded_by=e.profile)
            pl.append(posts)
            for p in posts:
                p.like = False
                ob = like.objects.filter(post=p,like_by=req.user)
                if ob:
                    p.like = True
                ob = like.objects.filter(post=p)
                p.likecount = ob.count()
    return render(req,'home.html',{'post':pl})

def about(req):
    return render(req,'about.html')

def contect(req):
    return render(req,'contect.html')

@login_required(login_url='/accounts/login')
def createPost(req):
    form = createPostform()
    if req.method=='POST':
        form = createPostform(req.POST,req.FILES)
        if form.is_valid():
            s = form.save(commit=False)
            s.uploaded_by=profile.objects.get(user=req.user)
            s.save()
            return redirect('/blog/postlist')
    return render(req,'createPost.html',{'form':form})

@login_required(login_url='/accounts/login')
def postlist(req):

    list = post.objects.filter(uploaded_by=profile.objects.get(user = req.user))
    print('list',list)
    return render(req,'postlist.html',{'list':list})

@login_required(login_url='/accounts/login')
def postDetail(req,pk):
    postD= post.objects.get(pk=pk)
    return render(req,'postDetail.html',{'post':postD})

@login_required(login_url='/accounts/login')
def postDelete(req,pk):
    a = post.objects.get(pk=pk)
    a.delete()
    return redirect('/blog/postlist/')

@login_required(login_url='/accounts/login')
def profilelist(req):
    p =profile.objects.all()
    for p1 in p:
        p1.follow = False
        ob = Follow.objects.filter(profile = p1, follow_by=req.user)
        if ob:
            p1.follow = True
    return render(req,'profilelist.html',{'proflies':p})

@login_required(login_url='/accounts/login')
def profileDetail(req, pk):
    profileD =profile.objects.get(pk=pk)
    profileD.followed = False
    ob = Follow.objects.filter(profile=profileD, follow_by=req.user)
    if ob:
        profileD.followed = True
    return render(req, 'profileDetail.html',{'p': profileD})

@login_required(login_url='/accounts/login')
def follow(req,pk):
    user = profile.objects.get(pk=pk)
    print('user',user)
    Follow.objects.create(profile=user,follow_by=req.user)
    return redirect('/blog/profilelist')

@login_required(login_url='/accounts/login')
def unfollow(req,pk):
    user = profile.objects.get(pk=pk)
    Follow.objects.filter(profile=user,follow_by=req.user).delete()
    return redirect('/blog/profilelist')

@login_required(login_url='/accounts/login')
def likes(req,pk):
    posts=post.objects.get(pk=pk)
    likes =like.objects.create(post=posts,like_by=req.user)
    return redirect('/blog/home')

@login_required(login_url='/accounts/login')
def unlikes(req,pk):
    posts=post.objects.get(pk=pk)
    likes =like.objects.get(post=posts,like_by=req.user).delete()
    return redirect('/blog/home')

@login_required(login_url='/accounts/login')
def comments(req,pk):
    if req.method=='POST':
        posts = post.objects.get(pk=pk)
        m = req.POST.get('msg')
        comment.objects.create(post=posts,msg = m, comment_by = req.user)
        return redirect('/blog/home')
    else:
        posts = post.objects.get(pk=pk)
        print('post',posts)
        com = comment.objects.filter(post=posts)
        print('comment',com)
        return render(req,'msg.html',{'com':com})







