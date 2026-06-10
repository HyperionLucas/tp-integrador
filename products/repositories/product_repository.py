"""Capa Repository.

El repository se encarga de acceder a los datos.
En esta etapa se simula una base de datos usando una lista en memoria.
"""

from products.models.product import Product


class ProductRepository:
    """Repositorio de órdenes de producción."""

    products = [
        Product(1, "Mesa de madera", 10, "PLANIFICADA"),
        Product(2, "Silla industrial", 25, "EN_PROCESO"),
        Product(3, "Estantería metálica", 5, "FINALIZADA"),
    ]

    def find_all(self):
        """Devuelve todas las órdenes de producción."""
        return self.products

    def find_by_id(self, product_id):
        """Busca una orden por ID. Si no existe, devuelve None."""
        for product in self.products:
            if product.product_id == product_id:
                return product
        return None
