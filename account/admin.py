from django.contrib import admin
from django.contrib.admin.decorators import register

from .models import CustomUser, ProfileModel
# Register your models here.

admin.site.register(ProfileModel)

@admin.register(CustomUser)
class AdminCustomUser(admin.ModelAdmin):

    list_display = ['username', 'phone_number', 'email', 'is_admin']
    