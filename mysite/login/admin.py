from django.contrib import admin
from .models import login

# Register your models here.
@admin.register(login)
class loginAdmin(admin.ModelAdmin):
    list_display=('name','email','password')

