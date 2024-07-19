from django.contrib import admin
from .models import InboxMessage, Conversation


class InboxMessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'conversation', 'created')
    list_filter = ('sender', 'conversation', 'created')
    search_fields = ('sender', 'conversation', 'created')
    readonly_fields = ('sender', 'conversation', 'body')
    ordering = ('-created',)


class ConversationAdmin(admin.ModelAdmin):
    list_display = ('id', 'lastmessage_created', 'is_seen')
    list_filter = ('id', 'lastmessage_created', 'is_seen')
    search_fields = ('id', 'lastmessage_created', 'is_seen')
    ordering = ('-lastmessage_created',)


admin.site.register(InboxMessage, InboxMessageAdmin)
admin.site.register(Conversation, ConversationAdmin)