from django.contrib import admin
from .models import HomePagePost


@admin.register(HomePagePost)
class HomePagePostAdmin(admin.ModelAdmin):
    list_display = ('title', 'context')
