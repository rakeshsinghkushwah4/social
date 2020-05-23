"""social URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView

from blog import views

urlpatterns = [
    # path(' ',RedirectView.as_view())
    path('home/',views.home),
    path('about/',views.about),
    path('contect/',views.contect),
    path('createPost/',views.createPost),
    path('postlist/',views.postlist),
    path('postDelete/<int:pk>',views.postDelete),
    path('postDetail/<int:pk>',views.postDetail),
    path('profilelist/',views.profilelist),
    path('profileDetail/<int:pk>',views.profileDetail),
    path('profileDetail/follow/<int:pk>',views.follow),
    path('profileDetail/unfollow/<int:pk>',views.unfollow),
    path('post/like/<int:pk>',views.likes),
    path('post/unlike/<int:pk>',views.unlikes),
    path('post/comment/<int:pk>',views.comments),
    path('',RedirectView.as_view(url='home/')),

]
