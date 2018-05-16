from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import businessCard

class bisnessCardAdmin(admin.ModelAdmin):
    list_display = ('email','contact_name','date')

admin.site.register(businessCard,bisnessCardAdmin)