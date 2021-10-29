from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import user, Post

admin.site.register(user, UserAdmin)
admin.site.register(Post)
