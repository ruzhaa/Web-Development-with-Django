from django.contrib import admin
from .models import BlogPost, Tags


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'created_date', 'updated_date')
    search_fields = ('title', )


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ('tag', )
