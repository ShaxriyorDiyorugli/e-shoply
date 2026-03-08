from django.contrib import admin
from .models import Category, Article


class ArticleAdmin(admin.AdminSite):
    list_display = ('№','title', 'category', 'views', 'created_at', 'publish')
    list_display_links = ('title',)
    list_editable = ('publish',)
    list_filter = ('title', 'created_at')

admin.site.register(Category)
admin.site.register(Article)


