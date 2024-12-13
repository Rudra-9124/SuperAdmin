from django.http import HttpResponse
import csv
from .models import Product

def export_products(request):
    # Create the HTTP response with CSV content type
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="products.csv"'

    # Create a CSV writer
    writer = csv.writer(response)

    # Write the header
    writer.writerow(['ID', 'Name', 'Price', 'Category', 'Stock'])

    # Write product data
    for product in Product.objects.all():
        writer.writerow([product.id, product.name, product.price, product.category, product.stock])

    return response
