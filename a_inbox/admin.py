from django.contrib import admin
from .models import InboxMessage, Conversation


class InboxMessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'conversation', 'created')
    list_filter = ('sender', 'conversation', 'created')
    search_fields = ('sender', 'conversation', 'created')
    date_hierarchy = 'created'
    ordering = ('-created',)


class ConversationAdmin(admin.ModelAdmin):
    list_display = ('id', 'lastmessage_created', 'is_seen')
    list_filter = ('id', 'lastmessage_created', 'is_seen')
    search_fields = ('id', 'lastmessage_created', 'is_seen')
    date_hierarchy = 'lastmessage_created'
    ordering = ('-lastmessage_created',)


admin.site.register(InboxMessage, InboxMessageAdmin)
admin.site.register(Conversation, ConversationAdmin)