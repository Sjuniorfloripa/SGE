from django.contrib import admin
from inflows.models import Inflow


@admin.register(Inflow)
class InflowAdmin(admin.ModelAdmin):
    list_display = ('id', 'supplier', 'product', 'quantity', 'description', 'created_at', 'updated_at')
