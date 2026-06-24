# TP Integrador - Sistema de Gestión de Producción y Manufactura

Proyecto desarrollado en Python utilizando Django, FastAPI, PostgreSQL y Docker, siguiendo una arquitectura por capas.

## Objetivo

Administrar información relacionada con producción y manufactura:

* Productos
* Recursos
* Órdenes de producción
* Estados productivos
* Validaciones
* Trazabilidad
* Respuestas en formato JSON

## Tecnologías

* Python 3.10 o superior
* Django
* FastAPI
* PostgreSQL
* Docker
* Docker Compose
* JSON
* VS Code
* Git y GitHub

## Arquitectura

El proyecto implementa una arquitectura por capas:

* Controller
* Service
* Repository
* DTO
* Validator
* Exception

Esta estructura permite separar responsabilidades y facilita el mantenimiento del sistema.

## Cómo ejecutar

### Ejecución local

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Ejecución con Docker

```bash
docker compose up --build -d
```

## Acceso a la aplicación

### Django

```text
http://127.0.0.1:8000/products/
```

### FastAPI

```text
http://127.0.0.1:8000/
```

### Documentación Swagger de FastAPI

```text
http://127.0.0.1:8000/docs
```

## Repositorio GitHub

```text
https://github.com/HyperionLucas/tp-integrador
```

## Autor

Lucas Laborde

Trabajo Práctico Integrador - Equipo Alpha