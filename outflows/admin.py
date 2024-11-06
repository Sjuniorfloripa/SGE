from django.contrib import admin
from outflows.models import Outflow


@admin.register(Outflow)
class OutflowAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'quantity', 'description', 'created_at', 'updated_at')
