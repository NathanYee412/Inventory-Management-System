from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Desktop, Laptop, Mobile, Equipment)
class ViewAdmin(admin.ModelAdmin):
    pass
