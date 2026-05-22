"""Arquivo WSGI gerado pelo Django para servir o projeto."""
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'abasteceai.settings')
application = get_wsgi_application()