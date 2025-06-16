from django.contrib import admin

from app.models import Email, Task, Status, Recipient


@admin.register(Email)
class SupplierAdmin(admin.ModelAdmin):
    pass

@admin.register(Task)
class SupplierAdmin(admin.ModelAdmin):
    pass

@admin.register(Status)
class SupplierAdmin(admin.ModelAdmin):
    pass

@admin.register(Recipient)
class SupplierAdmin(admin.ModelAdmin):
    pass