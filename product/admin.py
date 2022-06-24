from django.contrib import admin
from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "category", "created"]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "created"]


class SettingsAdmin(admin.ModelAdmin):
    list_display = ["name", "value", "created"]


admin.site.register(Products, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Settings, SettingsAdmin)
# admin.site.register(Order, OrderAdmin)
# Register your models here.
