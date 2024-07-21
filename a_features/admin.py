from django.contrib import admin
from .models import Feature


class FeatureAdmin(admin.ModelAdmin):
    list_display = ('name', 'developer', 'staging_enabled', 'production_enabled', 'created')
    list_filter = ('staging_enabled', 'production_enabled', 'created')
    search_fields = ('name', 'developer')
    ordering = ['-created']


admin.site.register(Feature, FeatureAdmin)