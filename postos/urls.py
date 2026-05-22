"""URLs do app postos. Cada path liga uma URL a uma view."""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('home/', views.home_view, name='home'),
    path('posto/<int:posto_id>/', views.detalhes_view, name='detalhes'),
    path('perfil/', views.perfil_view, name='perfil'),
]