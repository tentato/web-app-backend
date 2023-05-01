from django.contrib import admin
from .models import Tab
from .models import Post

class TabAdmin(admin.ModelAdmin):
    list_display = ("name", "description",)

class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "content", "tag", "posting_date",)
  
admin.site.register(Tab, TabAdmin)
admin.site.register(Post, PostAdmin)