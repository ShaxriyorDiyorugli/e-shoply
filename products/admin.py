from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class AdminProduct(admin.ModelAdmin):
    list_display = ('pk','title', 'created_at')
    list_display_links = ('title', 'pk')

@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ('pk', 'title','price', 'created_at', 'is_published',)
    list_display_links = ('title',)
    list_editable = ('is_published',)
    search_fields = ('title','price')