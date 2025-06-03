from django.contrib import admin

# Register your models here.

from .models import Statuses, Email

admin.site.site_header = "ПОЧТА"

@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    pass

@admin.register(Statuses)
class StatusesAdmin(admin.ModelAdmin):
    pass