# TP Integrador - Sistema de Gestión de Producción y Manufactura

Proyecto desarrollado en Python y Django, respetando una arquitectura por capas.

## Objetivo

Administrar información relacionada con producción y manufactura:

- productos;
- recursos;
- órdenes de producción;
- estados productivos;
- validaciones;
- trazabilidad;
- respuestas en formato JSON.

## Tecnologías

- Python 3.10 o superior
- Django
- JSON
- VS Code
- Git y GitHub

## Cómo ejecutar

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Abrir:

```text
http://127.0.0.1:8000/products/
```

## Subir a GitHub

```bash
git init
git add .
git commit -m "Primer commit TP Integrador"
git branch -M main
git remote add origin URL_DE_TU_REPOSITORIO
git push -u origin main
```
