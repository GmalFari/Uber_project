from django.contrib import admin
from .models import User
# # Register your models here.

class LogEntryAdmin(admin.ModelAdmin):
    list_display = ['usertype', 'phone']

admin.site.register(User, LogEntryAdmin)