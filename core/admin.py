from django.contrib import admin
from core.models import Post, Comment

# Register your models here.
admin.site.register([Post, Comment])
# admin.site.register(Comment)
