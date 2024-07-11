from django.contrib import admin
from .models import *


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'artist', 'created')
    search_fields = ('title', 'body')
    list_filter = ('created',)


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'order')
    search_fields = ('name', 'slug')
    list_filter = ['order']
    
    
class LikedCommentAdmin(admin.ModelAdmin):
    list_display = ['comment', 'user', 'created']
    search_fields = ['comment', 'user']
    list_filter = ['created']


class LikedReplyAdmin(admin.ModelAdmin):
    list_display = ['reply', 'user', 'created']
    search_fields = ['reply', 'user']
    list_filter = ['created']


class LikedPostAdmin(admin.ModelAdmin):
    list_display = ['post', 'user', 'created']
    search_fields = ['post', 'user']
    list_filter = ['created']


admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment)
admin.site.register(LikedComment, LikedCommentAdmin)
admin.site.register(Reply)
admin.site.register(LikedReply, LikedReplyAdmin)
admin.site.register(LikedPost, LikedPostAdmin)