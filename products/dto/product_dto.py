"""Capa DTO.

DTO significa Data Transfer Object.
Sirve para definir qué datos se envían como respuesta al cliente.
"""


class ProductDTO:
    """DTO para devolver órdenes de producción en formato JSON."""

    def __init__(self, product_id, name, quantity, status):
        self.product_id = product_id
        self.name = name
        self.quantity = quantity
        self.status = status

    def to_dict(self):
        """Convierte el DTO en un diccionario compatible con JSON."""
        return {
            "id": self.product_id,
            "name": self.name,
            "quantity": self.quantity,
            "status": self.status,
        }
