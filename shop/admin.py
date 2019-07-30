from django.contrib import admin

# Register your models here.
from shop.models import Category, Product, ProductHasImage


class ProductHasImageInline(admin.TabularInline):
    model = ProductHasImage


class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductHasImageInline,
    ]


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
