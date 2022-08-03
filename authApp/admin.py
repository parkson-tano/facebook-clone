from django.contrib import admin
from .models import *
# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name','gender','birthday')

admin.site.register(UserProfile, UserProfileAdmin) 