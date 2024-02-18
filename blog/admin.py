from django.contrib import admin

# File imports
from blog.models import Category, Post

# Register your models here.
# Passing with default configurations is good enough at this moment
class CategroyAdmin(admin.ModelAdmin):
    pass

class PostAdmin(admin.ModelAdmin):
    pass

# Registering the actual models with the Admin class
admin.site.register(Category, CategroyAdmin)
admin.site.register(Post, PostAdmin)