"""Capa Validator.

Los validators permiten verificar datos antes de procesarlos.
"""


class ProductValidator:
    """Validador básico para datos de producción."""

    def validate_name(self, name):
        """Valida que el nombre tenga al menos 3 caracteres."""
        if not name or len(name.strip()) < 3:
            raise ValueError("El nombre debe tener al menos 3 caracteres.")

    def validate_quantity(self, quantity):
        """Valida que la cantidad sea un número mayor a cero."""
        if not isinstance(quantity, (int, float)) or quantity <= 0:
            raise ValueError("La cantidad debe ser mayor a cero.")
