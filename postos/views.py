"""Views do app postos. Cada funcao recebe um request e devolve uma pagina."""
from django.shortcuts import render, get_object_or_404
from .models import Posto


def login_view(request):
    # Pagina inicial: tela de login
    return render(request, 'login.html')


def home_view(request):
    # Busca todos os postos do banco para listar na home
    postos = Posto.objects.all()
    return render(request, 'home.html', {'postos': postos})


def detalhes_view(request, posto_id):
    # Pega o posto pelo id ou mostra erro 404
    posto = get_object_or_404(Posto, id=posto_id)
    return render(request, 'detalhes.html', {'posto': posto})


def perfil_view(request):
    # Por enquanto so renderiza a tela com dados fixos no HTML
    return render(request, 'perfil.html')