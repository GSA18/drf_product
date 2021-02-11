from django.contrib import admin

from .models import Product, Color, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'altura', 'largura', 'peso')


class ColorAdmin(admin.ModelAdmin):
    list_display = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Color, ColorAdmin)
admin.site.register(Category, CategoryAdmin)
