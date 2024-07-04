from django.contrib import admin
from .models import *


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')
    search_fields = ('title', 'body')
    list_filter = ('created',)


admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
