#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mapauesc.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Nao foi possivel importar Django. Verifique se esta instalado e se o ambiente virtual esta ativo."
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
