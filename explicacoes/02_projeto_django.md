# Explicacao do projeto Django (Sprint 5)

Nessa sprint o professor pediu pra gente comecar a transformar o projeto em
Django. A diferenca pra parte anterior e que agora o HTML nao fica solto: ele e
servido pelo Python a partir de uma "view", que e ligada a uma URL.

## Estrutura de pastas

```
abasteceai-django/
  manage.py              -> script pra rodar comandos do Django
  abasteceai/            -> configuracoes do projeto
    settings.py
    urls.py
    wsgi.py
  postos/                -> meu app, onde fica a logica
    models.py
    views.py
    urls.py
    admin.py
    migrations/
  templates/             -> arquivos HTML
  static/css/style.css   -> CSS compartilhado
```

Criei a estrutura usando `django-admin startproject abasteceai .` e depois
`python manage.py startapp postos`. Movi os HTML pra pasta `templates/` e o CSS
pra `static/css/` (tarefa de mudar a rota dos arquivos estaticos).

## manage.py

E um arquivo que ja vem pronto com o Django. Ele so serve pra rodar comandos:
`runserver`, `makemigrations`, `migrate`, `createsuperuser`, etc. A linha mais
importante e a que define `DJANGO_SETTINGS_MODULE`, que diz pro Django onde
achar as configuracoes do projeto.

## abasteceai/settings.py

Aqui fica TUDO sobre o projeto. Os pontos que eu mexi/precisei entender:

- `BASE_DIR`: caminho da pasta raiz, usado em varios lugares (banco,
  templates, static).
- `INSTALLED_APPS`: adicionei `'postos'` no final pro Django reconhecer meu
  app e rodar as migracoes dele.
- `TEMPLATES`: coloquei `BASE_DIR / 'templates'` em `DIRS` pra ele procurar
  os HTML na pasta `templates/` do projeto, e nao so dentro de cada app.
- `DATABASES`: deixei o SQLite (vem por padrao). E um arquivo unico
  `db.sqlite3` no disco, mais facil pra desenvolver.
- `LANGUAGE_CODE = 'pt-br'` e `TIME_ZONE = 'America/Sao_Paulo'` pra deixar
  mensagens e datas em portugues.
- `STATIC_URL = '/static/'` e `STATICFILES_DIRS = [BASE_DIR / 'static']`:
  essa parte resolve a tarefa "mudar rota para acessar os CSS na pasta
  static". E com isso que o `{% static 'css/style.css' %}` funciona nos
  templates.

## abasteceai/urls.py

E o roteador principal. Usei `include('postos.urls')` pra delegar todas as
URLs (que nao sejam `/admin`) pro meu app. Assim cada app cuida das suas
proprias rotas, ficando mais organizado.

## postos/urls.py

Aqui defino cada rota apontando pra uma view:

- `''` -> `login_view` (pagina inicial)
- `'home/'` -> `home_view`
- `'posto/<int:posto_id>/'` -> `detalhes_view` (`<int:posto_id>` captura o
  numero da URL e passa pra view como parametro)
- `'perfil/'` -> `perfil_view`

O `name='...'` em cada path e o que me deixa usar `{% url 'home' %}` nos
templates em vez de escrever o caminho na mao. Se eu mudar a URL depois, nao
preciso sair caçando link nenhum no HTML.

## postos/views.py

Cada funcao recebe um `request` e devolve uma pagina renderizada com
`render(request, 'arquivo.html', contexto)`. O `contexto` e um dicionario com
as variaveis que o template pode usar.

- `login_view`: so renderiza o HTML, ainda nao validei login de verdade.
- `home_view`: faz `Posto.objects.all()` pra buscar todos os postos do banco
  e passa pra `home.html`.
- `detalhes_view`: usa `get_object_or_404` pra buscar o posto pelo id; se
  nao achar, ja retorna erro 404 (mais seguro do que dar crash).
- `perfil_view`: por enquanto so abre o template.

## postos/models.py

Aqui fica a modelagem do banco. Cada classe vira uma tabela. Resolve a
tarefa "criar models.py com base na modelagem de dados".

- `Posto`: tem nome, bandeira, endereco, avaliacao (DecimalField pra aceitar
  notas tipo 4.5) e a data de criacao automatica (`auto_now_add=True`).
- `Preco`: tem uma `ForeignKey` apontando pro Posto. Isso cria o
  relacionamento "um posto tem varios precos". O `related_name='precos'` me
  permite escrever `posto.precos.all()` no template. Uso `choices=TIPOS` pra
  limitar os tipos de combustivel.
- `Comodidade`: mesma logica do preco, mas pra conveniencia, farmacia, etc.

O `__str__` so muda o jeito que o registro aparece no painel admin.

## postos/migrations/0001_initial.py

Gerei rodando `python manage.py makemigrations postos`. Ele leu meu
`models.py` e criou esse arquivo descrevendo as tabelas. Depois rodei
`python manage.py migrate` pra aplicar de verdade no banco SQLite.

## postos/admin.py

Registrei os tres models com `admin.site.register(...)` pra eles aparecerem
no `/admin`. Assim consigo cadastrar posto, preco e comodidade pela
interface administrativa sem precisar de codigo.

## Templates (HTML)

Sao os mesmos HTML da sprint passada, mas adaptados pro Django:

- No comeco de cada arquivo coloquei `{% load static %}` pra poder usar a
  tag `{% static 'css/style.css' %}` no `<link>`. Essa tag gera o caminho
  correto do CSS dentro de `/static/`.
- Os links viraram `{% url 'nome_da_rota' %}` em vez de `home.html`
  hardcoded. Assim o Django monta a URL certinha mesmo que eu mude depois.
- Nos `<form>` adicionei `{% csrf_token %}` logo apos a abertura. O Django
  exige isso por seguranca (protege contra ataque CSRF).
- Na `home.html` troquei os 3 cards repetidos por um `{% for posto in
  postos %}` que monta um card pra cada posto vindo do banco. O `{% empty
  %}` mostra uma mensagem caso a lista esteja vazia.
- Na `detalhes.html` uso `{{ posto.nome }}`, `{{ posto.endereco }}` etc. pra
  acessar os campos. Pra listar precos e comodidades faço `{% for preco in
  posto.precos.all %}` aproveitando o `related_name` do model. O
  `get_tipo_display` mostra o nome bonito do `choices` (ex: "Gasolina
  Comum") em vez do valor cru ("gasolina").

## Static (CSS)

E o mesmo `style.css` da sprint passada, so que agora ele fica em
`static/css/style.css`. O Django serve esse arquivo automaticamente em modo
DEBUG. Em producao seria necessario rodar `collectstatic`, mas pra trabalho
da faculdade isso ja basta.

---

## Como rodar

```
pip install django
python manage.py migrate
python manage.py createsuperuser   # opcional, pra acessar /admin
python manage.py runserver
```

Depois e so abrir `http://127.0.0.1:8000/` no navegador.