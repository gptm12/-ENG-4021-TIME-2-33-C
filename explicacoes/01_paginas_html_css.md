# Explicacao das paginas HTML e CSS (Sprint anterior)

Nessa primeira parte eu fiz 4 telas em HTML puro e um arquivo CSS compartilhado
entre elas. A ideia era treinar a estrutura de uma pagina e a estilizacao basica
antes de partir pro Django.

## style.css (compartilhado)

Comecei zerando as margens e paddings padroes do navegador usando o seletor `*`,
e coloquei `box-sizing: border-box` pra largura/altura ja considerarem a borda
e o padding (achei mais facil de calcular o tamanho dos elementos assim).

Defini uma `.container` com `max-width: 500px` e `margin: 0 auto` pra centralizar
o conteudo na tela e dar um visual de aplicativo mobile, ja que o projeto e um
PWA.

O `header` ficou com a cor laranja (`#ff6b00`) que e a cor principal do
AbasteceAi. O texto fica branco pra ter contraste.

Criei uma classe `.botao` que reaproveito em varias telas (login, voltar,
ver detalhes). Tem `padding`, `border-radius` arredondado e o `:hover` deixa um
pouco mais escuro pra dar feedback ao usuario quando passa o mouse.

A classe `.botao-secundario` herda do `.botao` mas inverte as cores (fundo
branco e texto laranja) pra usar como acao secundaria, tipo "Criar conta" ou
"Voltar".

O `.form-grupo` agrupa o `label` em cima e o `input` embaixo, com margem entre
os campos pra nao ficar tudo grudado.

Os `.card` sao os blocos onde mostro cada posto. Eles tem borda fina, cantos
arredondados e um espacamento interno (`padding: 15px`). Dentro deles a classe
`.preco` deixa o valor em verde e negrito pra chamar atencao.

Por fim a `.lista-precos` usa `display: flex` com `justify-content:
space-between` pra jogar o nome do combustivel pra esquerda e o valor pra
direita na mesma linha.

## login.html

Comeco com `<!DOCTYPE html>` que avisa ao navegador que e HTML5, e defino
`lang="pt-br"` pra acessibilidade. No `<head>` coloco o `charset UTF-8` pra
aceitar acentos e linko o `style.css`.

Dentro do `<body>` uso a `.container` pra centralizar tudo, um `<header>` com o
nome do app e um `<form>` com dois campos (e-mail e senha). O input de senha tem
`type="password"` pra esconder os caracteres. O botao de entrar tem
`type="submit"` e o "Criar conta" e um link estilizado de botao que leva pra
home.

## home.html

Aqui tem um campo de busca (so visual por enquanto) e tres `.card` repetindo a
mesma estrutura: nome do posto, endereco, avaliacao e preco. Cada card tem um
botao "Ver detalhes" que aponta pra `detalhes.html`. Repeti a estrutura na mao
porque ainda estou em HTML puro (sem template engine).

## detalhes.html

Mostra um card com os dados do posto, uma `<ul class="lista-precos">` listando
os combustiveis com seus precos, e outra lista com os comercios do posto. No
final tem dois botoes: um primario "Como chegar" e um secundario "Voltar".

## perfil.html

E uma tela de perfil simples. Tem um card com os dados ja preenchidos
(simulando o usuario logado) e um formulario com `value=""` ja preenchido em
cada input pra permitir editar. O botao de salvar usa `type="submit"`.

---

Resumindo: o foco foi treinar marcacao semantica (header, form, ul/li),
reaproveitamento de CSS via classes (`.botao`, `.card`, `.form-grupo`) e
pensar a navegacao entre telas usando `<a href>`.