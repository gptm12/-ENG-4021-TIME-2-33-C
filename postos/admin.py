from django.contrib import admin
from .models import Posto, Preco, Comodidade

# Registro meus models pra aparecerem no painel /admin do Django
admin.site.register(Posto)
admin.site.register(Preco)
admin.site.register(Comodidade)