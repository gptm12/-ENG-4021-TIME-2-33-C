"""URLs principais do projeto. Aqui eu incluo as urls do meu app."""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Quando a URL nao for /admin, manda pro app postos
    path('', include('postos.urls')),
]