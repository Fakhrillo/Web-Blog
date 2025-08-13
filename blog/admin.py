from django.contrib import admin
from blog.models import Post, Comment

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author", "status", "publish", "created", "modified")
    list_display_links = list_display
    list_filter = ("status", "publish", "author")
    search_fields = ("title", "content")
    prepopulated_fields = {"slug": ("title",)}
    raw_id_fields = ("author",)
    date_hierarchy = "publish"
    ordering = ("status", "publish")
    show_facets = admin.ShowFacets.ALWAYS  # type:ignore


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "post", "name", "email", "active", "created", "modified")
    list_display_links = list_display
    list_filter = ("active", "created", "modified")
    search_fields = ("name", "email", "content")
