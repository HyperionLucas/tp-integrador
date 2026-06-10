"""Excepciones personalizadas del módulo products."""


class ProductException(Exception):
    """Excepción general para errores del sistema de producción."""

    def __init__(self, message, status_code=400):
        super().__init__(message)
        self.message = message
        self.status_code = status_code


class ProductNotFoundException(ProductException):
    """Se usa cuando no se encuentra una orden de producción."""

    def __init__(self, product_id):
        super().__init__(
            message=f"No se encontró la orden de producción con ID {product_id}.",
            status_code=404,
        )
