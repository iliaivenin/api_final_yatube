from django.contrib import admin

from .models import Comment, Follow, Group, Post


class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "text", "pub_date", "author", "group")
    search_fields = ("text",)
    list_filter = ("pub_date",)
    empty_value_display = "-пусто-"


class GroupAdmin(admin.ModelAdmin):
    # list_display = ("id", "slug", "title", "description")
    list_display = ("id", "title")
    search_fields = ("title",)
    # prepopulated_fields = {"slug": ("title",)}


class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "text", "created", "author", "post")
    search_fields = ("text", "author",)


class FollowAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "following")
    search_fields = ("user", "following",)


admin.site.register(Group, GroupAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Follow, FollowAdmin)
