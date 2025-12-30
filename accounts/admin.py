from django.contrib import admin
from .models import AppUser, Profile

class ProfileAdmin(admin.ModelAdmin):
    pass

# Register your models here.
admin.site.register(AppUser)
admin.site.register(Profile)