#!/usr/bin/env python
"""Arquivo padrao do Django para rodar comandos como runserver, migrate, etc."""
import os
import sys


def main():
    # Diz para o Django onde estao as configuracoes do projeto
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'abasteceai.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Nao consegui importar o Django. Voce instalou ele? (pip install django)"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()