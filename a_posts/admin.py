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


admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment)
admin.site.register(LikedComment)
admin.site.register(Reply)
admin.site.register(LikedReply)
