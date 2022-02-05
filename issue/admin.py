from django.contrib import admin
from .models import Machine, Issue


@admin.register(Machine)
class MachineAdmin(admin.ModelAdmin):
    """
    Admin class for Machine modal
    """
    search_fields = ['name']
    list_display = ('name', 'slug', 'status')
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('status', 'name')


@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    """
    Admin class for Issue modal
    """
    search_fields = ['machine', 'user']
    list_display = ('machine', 'created_at', 'rectified')
    list_filter = ('machine', 'created_at', 'rectified')

    def resolve_issue(self, request, queryset):
        queryset.update(issue_resolved=True)
