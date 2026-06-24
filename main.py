"""Archivo principal de FastAPI."""

from fastapi import FastAPI

app = FastAPI(
    title="TP Integrador - Producción y Manufactura",
    description="API REST del sistema de producción.",
    version="1.0.0",
)


@app.get("/")
def home():
    return {
        "message": "Sistema de Gestión de Producción y Manufactura funcionando"
    }


@app.get("/api/products/")
def get_products():
    return [
        {
            "id": 1,
            "name": "Mesa de madera",
            "quantity": 10,
            "status": "PLANIFICADA",
        },
        {
            "id": 2,
            "name": "Silla industrial",
            "quantity": 25,
            "status": "EN_PROCESO",
        },
        {
            "id": 3,
            "name": "Estantería metálica",
            "quantity": 5,
            "status": "FINALIZADA",
        },
    ]