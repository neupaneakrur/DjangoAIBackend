from django.contrib import admin
from .models import AICompletion

@admin.register(AICompletion)
class AICompletionAdmin(admin.ModelAdmin):
    list_display = ['id', 'prompt_preview', 'response_preview', 'model_used', 'tokens_used', 'processing_time', 'ip_address', 'created_at']
    list_filter = ['model_used', 'created_at', 'ip_address']
    search_fields = ['prompt', 'response']
    readonly_fields = ['created_at', 'updated_at']
    list_per_page = 25
    
    fieldsets = (
        ('Request Information', {
            'fields': ('prompt', 'model_used', 'temperature')
        }),
        ('Response Information', {
            'fields': ('response', 'tokens_used', 'processing_time')
        }),
        ('Request Metadata', {
            'fields': ('ip_address', 'user_agent'),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def has_add_permission(self, request):
        """Disable manual addition of completions through admin"""
        return False
