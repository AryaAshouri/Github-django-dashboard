from django.contrib import admin
from .models import *

class ThemeAdmin(admin.ModelAdmin):
    list_display = ("theme",)
    list_filter = ("theme",)
    search_fields = ("theme",)
    ordering = ("theme",)
admin.site.register(Theme, ThemeAdmin)
