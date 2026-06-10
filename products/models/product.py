"""Modelo del sistema.

En esta primera versión, el modelo NO hereda de django.db.models.Model.
Se usa una clase simple de Python para que el código sea más fácil de entender.
"""


class Product:
    """Representa una orden de producción."""

    def __init__(self, product_id, name, quantity, status):
        self.product_id = product_id
        self.name = name
        self.quantity = quantity
        self.status = status

    def __repr__(self):
        """Devuelve una representación legible del objeto."""
        return (
            f"Product(id={self.product_id}, "
            f"name={self.name}, "
            f"quantity={self.quantity}, "
            f"status={self.status})"
        )
