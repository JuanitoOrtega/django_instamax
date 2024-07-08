from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'realname', 'email', 'location', 'created')
    search_fields = ('user__username', 'realname', 'email', 'location')
    list_filter = ['created']


admin.site.register(Profile, ProfileAdmin)