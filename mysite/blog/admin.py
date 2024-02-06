from django.contrib import admin
from .models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status']  # поля для показа на админской панели
    list_filter = ['status', 'created', 'publish', 'author']
    search_fields = ['title', 'body']  # строка поиска - по каким полям искать
    prepopulated_fields = {'slug': ('title',)}
    # raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']

