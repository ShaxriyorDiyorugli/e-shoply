from django.contrib import admin
from .models import Category, Article

class AdminProduct(admin.ModelAdmin):
    list_display = ('pk', 'title', 'created_at', 'is_publish')
    list_display_links = ('title', 'pk')
    list_editable = ('is_publish',)


admin.site.register(Category)
admin.site.register(Article, AdminProduct)