# HTML

HTML (HyperText Markup Language) é a linguagem padrão para a criação de páginas da web. Ele fornece uma estrutura básica que permite a criação de conteúdo hipertextual e a formatação desse conteúdo em uma página da web. HTML é uma linguagem de marcação, o que significa que você usa tags para marcar elementos na página e definir sua estrutura.

## Estrutura Básica de um Documento HTML

Um documento HTML básico é composto por várias partes essenciais:

1. `<!DOCTYPE html>`: Esta declaração define a versão do HTML que está sendo usada (por exemplo, HTML5).

2. `<html>`: O elemento `<html>` é o contêiner raiz de todo o documento HTML.

3. `<head>`: O elemento `<head>` contém informações sobre o documento, como o título da página, meta informações e links para estilos e scripts.

4. `<meta charset="UTF-8">`: Esta tag define o conjunto de caracteres (UTF-8 é amplamente utilizado para suportar caracteres especiais e diferentes idiomas).

5. `<title>`: O elemento `<title>` define o título da página, que é exibido na guia do navegador ou na barra de título.

6. `<body>`: O elemento `<body>` contém o conteúdo visível da página, como texto, imagens, links e outros elementos.

## Tags HTML

**Estrutura de Página e Conteúdo:**

- `<header>`: Usada para indicar o cabeçalho de uma seção ou página web.

- `<footer>`: Usada para indicar o rodapé de uma seção ou página web.

- `<section>`: Usada para definir uma seção temática ou conteúdo agrupado em uma página.

- `<article>`: Usada para definir um conteúdo autônomo e autocontido, como uma postagem de blog, notícia ou artigo.

- `<aside>`: Usada para representar conteúdo relacionado ou complementar ao conteúdo principal de uma página.

**Texto e Formatação:**

- `<h1>`, `<h2>`, `<h3>`, `<h4>`, `<h5>`, `<h6>`: Usadas para criar títulos de diferentes níveis de importância.

- `<p>`: Usada para criar parágrafos de texto.

- `<strong>` e `<em>`: Usadas para enfatizar texto, onde `<strong>` geralmente indica ênfase forte (geralmente exibido em negrito) e `<em>` indica ênfase enfática (geralmente exibido em itálico).

- `<abbr>`: Usada para definir uma abreviação ou acrônimo, com o atributo `title` para fornecer uma explicação completa.

- `<cite>`: Usada para marcar títulos de obras, como livros, filmes ou artigos, que você está citando em seu conteúdo.

- `<q>`: Usada para citar o texto dentro das aspas, indicando que é uma citação.

- `<del>` e `<ins>`: Usadas para marcar texto deletado ou inserido, úteis em revisões de texto ou documentos.

- `<time>`: Usada para representar datas e horários com informações semânticas.

- `<mark>`: Usada para destacar partes de texto dentro de um conteúdo.

**Listas e Navegação:**

- `<ul>`: Usada para criar listas não ordenadas (com marcadores).

- `<ol>`: Usada para criar listas ordenadas (com números ou letras).

- `<li>`: Usada para definir itens de lista dentro de `<ul>` ou `<ol>`.

- `<nav>`: Usada para definir uma seção de navegação, geralmente contendo links para outras páginas ou seções do site.

**Imagens e Multimídia:**

- `<img>`: Usada para inserir imagens na página.

- `<figure>` e `<figcaption>`: Usadas para agrupar imagens e fornecer uma legenda associada à imagem usando `<figcaption>`.

- `<iframe>`: Usada para incorporar conteúdo de outra página web, como vídeos ou mapas.

**Formulários e Entrada de Dados:**

- `<form>`: Usada para criar um formulário em uma página web, onde os usuários podem inserir e enviar dados.

- `<input>`: Usada dentro de um formulário para criar campos de entrada, como caixas de texto, botões de rádio, caixas de seleção e mais.

- `<textarea>`: Usada em formulários para criar uma área de texto expansível onde os usuários podem inserir várias linhas de texto.

- `<button>`: Usada para criar botões clicáveis em formulários ou para ações interativas.

**Outras Tags Importantes:**

- `<div>`: Usada como um elemento de divisão para agrupar e estruturar conteúdo.

- `<span>`: Usada para agrupar elementos inline e aplicar estilos ou manipulações de script a eles.

- `<br>`: Usada para criar uma quebra de linha dentro de um texto ou parágrafo.

- `<hr>`: Usada para criar uma linha horizontal, frequentemente usada para separar conteúdo em uma página.

- `<table>`, `<tr>`, `<td>`: Usadas para criar tabelas e suas células, úteis para exibir dados tabulares.

- `<details>` e `<summary>`: Usadas para criar elementos de detalhes expansíveis e contráteis, úteis para exibir informações adicionais de forma condensada.

- `<progress>`: Usada para criar barras de progresso, indicando o progresso de uma tarefa.

- `<meter>`: Usada para representar uma medida escalar em uma faixa conhecida, como uma avaliação de 0 a 10.

Essas são algumas das tags HTML comuns e importantes, agrupadas por funcionalidade e área de atuação em uma aplicação web. Cada uma delas desempenha um papel fundamental na estruturação e apresentação de conteúdo na web.

Para aprofundar seus conhecimentos em HTML, você pode consultar recursos adicionais, tutoriais e a [documentação oficial do HTML](https://developer.mozilla.org/pt-BR/docs/Web/HTML) e seus [tutoriais](https://www.w3schools.com/html/).

## Exemplo de Uso

Aqui está um exemplo simples de um documento HTML que exibe um título, um parágrafo e uma imagem:

Comece o arquivo digitando "html:5" e o cabeçalho será criado.

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Exemplo HTML</title>
</head>
<body>
    <h1>Meu Primeiro Documento HTML</h1>
    <p>Este é um parágrafo de exemplo.</p>
    <img src="imagem.jpg" alt="Imagem de Exemplo">
</body>
</html>
```

## Conclusão

O HTML é a espinha dorsal da web e é fundamental para a criação de páginas da web. Ele fornece uma estrutura básica que permite a criação de conteúdo e sua formatação. Além dos elementos mencionados aqui, o HTML possui uma ampla gama de tags e atributos que permitem a personalização e a criação de páginas da web interativas.

Para aprofundar seus conhecimentos em HTML, você pode consultar recursos adicionais, tutoriais e a [documentação oficial do HTML](https://developer.mozilla.org/pt-BR/docs/Web/HTML).