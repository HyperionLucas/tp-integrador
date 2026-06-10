#!/usr/bin/env python
"""Archivo principal para ejecutar comandos de Django."""

import os
import sys


def main():
    """Ejecuta las tareas administrativas de Django."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

    try:
        from django.core.management import execute_from_command_line
    except ImportError as error:
        raise ImportError("No se pudo importar Django. Verificar instalación.") from error

    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
