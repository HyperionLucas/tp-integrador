"""Capa Controller.

El controller recibe las peticiones HTTP y devuelve respuestas JSON.
"""

import logging
from django.http import JsonResponse
from products.dto.product_dto import ProductDTO
from products.services.product_service import ProductService

logger = logging.getLogger(__name__)


class ProductController:
    """Controller de producción."""

    def __init__(self):
        self.service = ProductService()

    def get_products(self, request):
        """
        Endpoint: GET /products/

        Devuelve las órdenes de producción en formato JSON.
        """
        logger.info("GET /products/ — Consultando órdenes de producción")

        try:
            products = self.service.get_products()
            data = []

            for product in products:
                dto = ProductDTO(
                    product.product_id,
                    product.name,
                    product.quantity,
                    product.status,
                )
                data.append(dto.to_dict())

            logger.info(f"GET /products/ — {len(data)} registros encontrados")
            return JsonResponse(data, safe=False, status=200)

        except Exception as error:
            logger.error(f"Error en get_products: {str(error)}")
            return JsonResponse({"error": "Error interno del servidor"}, status=500)
