from django.contrib import admin

from . import models


@admin.register(models.Client)
class ClientAdmin(admin.ModelAdmin):
    search_fields = ['name', 'phone']


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ['name']


@admin.register(models.Silo)
class SiloAdmin(admin.ModelAdmin):
    search_fields = ['name', 'size']
    list_filter = ['size']


@admin.register(models.Storage)
class StorageAdmin(admin.ModelAdmin):
    search_fields = ['silo__name', 'client__name', 'product__name']
    list_filter = ['entry_date', 'withdrawal_date', 'status']
