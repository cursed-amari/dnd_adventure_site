from django.contrib import admin
from .models import Adventure


@admin.register(Adventure)
class Adventure(admin.ModelAdmin):
    list_display = ('adventure_type', 'title', 'time_update', 'user')
    prepopulated_fields = {'slug': ('title',)}
