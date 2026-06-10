"""Rutas principales del proyecto."""

from django.contrib import admin
from django.urls import path
from products.controllers.product_controller import ProductController

controller = ProductController()

urlpatterns = [
    path("admin/", admin.site.urls),
    path("products/", controller.get_products),
]
