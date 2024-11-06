from django.contrib import admin
from suppliers.models import Supplier


@admin.register(Supplier)
class SuplierAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'created_at', 'updated_at')
