from django.contrib import admin
from products.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 
                    'title', 
                    'category', 
                    'brand', 
                    'description',
                    'serial_number',
                    'cost_price',
                    'selling_price',
                    'quantity',
                    'created_at',
                    'updated_at')

