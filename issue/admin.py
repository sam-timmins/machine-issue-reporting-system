from django.contrib import admin
from .models import Machine


@admin.register(Machine)
class MachineAdmin(admin.ModelAdmin):

    search_fields = ['name']
    list_display = ('name', 'slug', 'status')
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('status', 'name')
