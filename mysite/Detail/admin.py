from django.contrib import admin
from .models import Detail
# Register your models here.
@admin.register(Detail)
class detailAdmin(admin.ModelAdmin):
    list_display=('id','name','address')