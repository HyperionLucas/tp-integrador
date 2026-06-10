"""Capa Service.

El service contiene la lógica de negocio.
"""

from products.repositories.product_repository import ProductRepository


class ProductService:
    """Servicio que administra la lógica de producción."""

    def __init__(self):
        self.repository = ProductRepository()

    def get_products(self):
        """Obtiene todas las órdenes de producción."""
        return self.repository.find_all()

    def get_product_by_id(self, product_id):
        """Obtiene una orden de producción por ID."""
        return self.repository.find_by_id(product_id)
