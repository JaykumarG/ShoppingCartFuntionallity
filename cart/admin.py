from django.contrib import admin
from cart.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display= ('product_name', 'category', 'subcategory','price', 'desc')

# Register your models here.
admin.site.register(Product, ProductAdmin)
