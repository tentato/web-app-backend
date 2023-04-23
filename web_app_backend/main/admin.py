from django.contrib import admin
from .models import Tab

class TabAdmin(admin.ModelAdmin):
    list_display = ("name", "description",)
  
admin.site.register(Tab, TabAdmin)