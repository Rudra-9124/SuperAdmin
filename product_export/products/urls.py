from django.urls import path
from products import views

urlpatterns = [
    path('export-products/', views.export_products, name='export_products'),
]
