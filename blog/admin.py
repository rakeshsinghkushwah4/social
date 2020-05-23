from django.contrib import admin
from blog.models import  post,comment,Follow,like

# Register your models here.
admin.site.register(post)
admin.site.register(comment)
admin.site.register(Follow)
admin.site.register(like)

