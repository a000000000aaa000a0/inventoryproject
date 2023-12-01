from django.contrib import admin

# Register your models here.
from .models import Category, InventoryPost

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')

class InventoryPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')

admin.site.register(Category, CategoryAdmin)

admin.site.register(InventoryPost, InventoryPostAdmin)