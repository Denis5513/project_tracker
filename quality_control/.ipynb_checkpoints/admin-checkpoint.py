from django.contrib import admin
from .models import BugReport, FeatureRequest

@admin.register(BugReport)
class BugReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'project', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'priority')
    search_fields = ('title', 'description')
    list_editable = ('status',)
    ordering = ('created_at',)
    date_hierarchy = 'created_at'
    fieldsets = [
        (
            None,
            {
                'fields': ['title', 'description', 'status', 'priority', 'project', 'task']
            }
        )
    ]

@admin.register(FeatureRequest)
class FeatureRequestAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'project', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'priority')
    search_fields = ('title', 'description')
    list_editable = ('status',)
    ordering = ('created_at',)
    date_hierarchy = 'created_at'
    fieldsets = [
        (
            None,
            {
                'fields': ['title', 'description', 'status', 'priority', 'project', 'task']
            }
        )
    ]




