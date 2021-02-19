from django.contrib import admin

from . import models


@admin.register(models.Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email']
    search_fields = ['name', 'phone']


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(models.Silo)
class SiloAdmin(admin.ModelAdmin):
    list_display = ['name', 'size']
    search_fields = ['name']
    list_filter = ['size']


@admin.register(models.Storage)
class StorageAdmin(admin.ModelAdmin):
    list_display = [
        'get_silo_name',
        'get_client_name',
        'get_product_name',
        'current_cost',
        'total_cost',
        'quantity',
        'entry_date',
        'withdrawal_date',
        'status',
    ]
    search_fields = ['silo__name', 'client__name', 'product__name']
    list_filter = ['entry_date', 'withdrawal_date', 'status']

    def get_silo_name(self, obj):
        return obj.silo.name

    def get_client_name(self, obj):
        return obj.client.name

    def get_product_name(self, obj):
        return obj.product.name

    get_silo_name.short_description = 'Silo'
    get_client_name.short_description = 'Client'
    get_product_name.short_description = 'Product'
