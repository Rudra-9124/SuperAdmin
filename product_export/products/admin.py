from django.contrib import admin
from django.http import HttpResponse
import csv
from .models import Product

def export_products(modeladmin, request, queryset):
    
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="products.csv"'

    writer = csv.writer(response)

    writer.writerow(['ID', 'Name', 'Price', 'Category', 'Stock'])

    for product in queryset:
        writer.writerow([product.id, product.name, product.price, product.category, product.stock])

    return response


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'stock')
    actions = [export_products]

admin.site.register(Product, ProductAdmin)
