from django.contrib import admin

# Register your models here.
from .models import Selfcare

class Selfcareadmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'post')

admin.site.register(Selfcare, Selfcareadmin)
