from django.contrib import admin
from .models import *

# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "time_create", "is_published"]
    prepopulated_fields = {"slug": ("title",)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
