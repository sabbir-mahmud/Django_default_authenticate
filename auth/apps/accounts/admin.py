# imports
from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'email', 'user', 'verify'
    )
    list_display_links = (
        'id', 'name', 'email', 'user', 'verify'
    )
