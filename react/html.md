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

Para criar as tags automaticamente, comece o arquivo digitando "html:5" e o cabeçalho será criado.

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

- `<details>` e `<summary>`: Usadas para criar elementos de detalhes expansíveis e contráteis, úteis para exibir informações adicionais de forma condensada.

- `<progress>`: Usada para criar barras de progresso, indicando o progresso de uma tarefa.

- `<meter>`: Usada para representar uma medida escalar em uma faixa conhecida, como uma avaliação de 0 a 10.

Essas são algumas das tags HTML comuns e importantes, agrupadas por funcionalidade e área de atuação em uma aplicação web. Cada uma delas desempenha um papel fundamental na estruturação e apresentação de conteúdo na web.

Para aprofundar seus conhecimentos em HTML, você pode consultar recursos adicionais, tutoriais e a [documentação oficial do HTML](https://developer.mozilla.org/pt-BR/docs/Web/HTML) e seus [tutoriais](https://www.w3schools.com/html/).

## Meta Tags

1. `<meta charset="UTF-8">`: Define o conjunto de caracteres utilizado na página, geralmente como UTF-8 para suportar caracteres especiais e idiomas diversos.

2. `<meta name="viewport" content="width=device-width, initial-scale=1.0">`: Controla a exibição e dimensionamento da página em dispositivos móveis, garantindo uma experiência responsiva.

3. `<meta name="description" content="Descrição da página">`: Fornece uma breve descrição da página para os motores de busca, exibida nos resultados da pesquisa.

4. `<meta name="keywords" content="palavras-chave, relacionadas, à, página">`: Anteriormente usado para listar palavras-chave associadas à página, mas atualmente não é muito relevante para SEO.

5. `<meta name="author" content="Nome do Autor">`: Indica o autor da página.

6. `<meta name="robots" content="index, follow">`: Controla como os motores de busca rastreiam e indexam a página. "index" permite a indexação, e "follow" permite o rastreamento de links na página.

7. `<meta http-equiv="refresh" content="5;url=redirecionamento.html">`: Redireciona automaticamente para outra página após um determinado tempo (neste caso, 5 segundos).

8. `<meta http-equiv="content-language" content="pt-BR">`: Define o idioma principal do conteúdo da página, o que pode afetar como os motores de busca interpretam o idioma do conteúdo.

9.  `<meta http-equiv="refresh" content="5;url=redirecionamento.html">`: Já mencionado anteriormente, esta meta tag redireciona automaticamente para outra página após um determinado tempo.

10. `<meta http-equiv="cache-control" content="no-cache">`: Controla as instruções de cache para a página, informando aos navegadores que eles não devem armazenar em cache a página.

11. `<meta http-equiv="pragma" content="no-cache">`: Semelhante ao exemplo anterior, informa aos navegadores para não armazenar em cache a página.

12. `<meta http-equiv="expires" content="0">`: Define uma data de expiração imediata para a página, o que também pode evitar o armazenamento em cache.

13. `<meta http-equiv="refresh" content="5;url=redirecionamento.html">`: Esta meta tag já mencionada redireciona automaticamente para outra página após um determinado tempo.

14. `<meta http-equiv="x-ua-compatible" content="IE=edge">`: Informa aos navegadores Internet Explorer para renderizar a página no modo de última geração (Edge).

15. `<meta http-equiv="x-ua-compatible" content="IE=7">`: Pode ser usada para forçar o Internet Explorer a renderizar a página em um modo de compatibilidade específico (por exemplo, IE7).

16. `<meta name="og:title" content="Título Open Graph">`: Define o título a ser exibido ao compartilhar a página em redes sociais (Open Graph).

17. `<meta name="og:description" content="Descrição Open Graph">`: Define a descrição a ser exibida ao compartilhar a página em redes sociais (Open Graph).

18. `<meta name="og:image" content="url-da-imagem.jpg">`: Especifica uma imagem a ser exibida ao compartilhar a página em redes sociais (Open Graph).

19. `<meta name="og:url" content="URL-da-Página">`: Define a URL da página ao compartilhar em redes sociais (Open Graph).

20. `<meta name="og:type" content="website">`: Indica o tipo de conteúdo, geralmente "website" para páginas web.

21. `<meta name="og:site_name" content="Nome do Site">`: Especifica o nome do site ao compartilhar em redes sociais (Open Graph).

22. `<meta name="twitter:card" content="summary_large_image">`: Define o tipo de cartão do Twitter a ser exibido ao compartilhar a página no Twitter.

23. `<meta name="twitter:site" content="@nome-do-site">`: Especifica a conta do Twitter associada à página.

Essas são algumas das principais meta tags em HTML que são usadas para controlar e melhorar a apresentação e o compartilhamento de páginas na web. Cada uma delas desempenha um papel importante em aspectos como SEO, compatibilidade móvel e compartilhamento em redes sociais.

## Listas e Navegação:

- `<ul>`: Usada para criar listas não ordenadas (com marcadores).

- `<ol>`: Usada para criar listas ordenadas (com números ou letras).

- `<li>`: Usada para definir itens de lista dentro de `<ul>` ou `<ol>`.

- `<nav>`: Usada para definir uma seção de navegação, geralmente contendo links para outras páginas ou seções do site.

Os exemplos em HTML para cada uma das tags está no respectico arquivo html.

No exemplo, `<ul>` é usado para criar uma lista não ordenada e `<li>` é usado para definir itens de lista. Isso resultará em uma lista com marcadores, geralmente pontos, como:

- Item 1
- Item 2
- Item 3

Em seguida, `<ol>` é usado para criar uma lista ordenada e `<li>` é usado para definir itens de lista. Isso resultará em uma lista numerada, como:

1. Primeiro item
2. Segundo item
3. Terceiro item

Por último, `<nav>` é usado para criar uma seção de navegação que contém links para diferentes páginas ou seções do site. Cada item de lista `<li>` contém um link `<a>` para uma página específica. Observe que os URLs dentro de `href` (# neste caso) são fictícios e devem ser substituídos pelos URLs reais do seu site.

## Tabelas com HTML

Principais tags HTML usadas para tabelas:

1. `<table>`: A tag `<table>` é usada para criar uma tabela HTML. Ela é o elemento contêiner principal para a estrutura da tabela.

2. `<tr>`: A tag `<tr>` é usada para definir uma linha em uma tabela. Dentro de uma tabela, você pode ter várias linhas, e cada linha contém células.

3. `<th>`: A tag `<th>` é usada para definir células de cabeçalho em uma tabela. O conteúdo das células de cabeçalho geralmente contém títulos ou rótulos para as colunas.

4. `<td>`: A tag `<td>` é usada para definir células de dados em uma tabela. O conteúdo das células de dados contém informações ou dados específicos.

5. `<thead>`: A tag `<thead>` é usada para agrupar as linhas que representam o cabeçalho da tabela. Geralmente contém uma ou mais linhas com células de cabeçalho `<th>`.

6. `<tbody>`: A tag `<tbody>` é usada para agrupar as linhas que representam o corpo principal da tabela. Ele contém uma ou mais linhas com células de dados `<td>`.

7. `<tfoot>`: A tag `<tfoot>` é usada para agrupar as linhas que representam o rodapé da tabela. Normalmente, ele contém uma ou mais linhas com células de rodapé `<td>`.

Essas tags são essenciais para criar tabelas estruturadas em HTML. O uso de `<th>` para células de cabeçalho ajuda a identificar as colunas de forma semântica, enquanto `<td>` é usado para células de dados que contêm informações reais. `<thead>`, `<tbody>`, e `<tfoot>` ajudam a organizar a tabela em partes distintas, como cabeçalho, corpo e rodapé. O exemplo segue no respectivo arquivo html.

Quando quiser que uma célula ocupe mais de uma coluna, use "colspan="x"", em que x é o número de colunas. (ex:<th colspan="2">Produto</th>)

Quando quiser que uma célula ocupe mais de uma linha, use "rowspan="x"", em que x é o número de linhas. (ex:<td rowspan="2">Camiseta</td>)

## Conclusão

O HTML é a espinha dorsal da web e é fundamental para a criação de páginas da web. Ele fornece uma estrutura básica que permite a criação de conteúdo e sua formatação. Além dos elementos mencionados aqui, o HTML possui uma ampla gama de tags e atributos que permitem a personalização e a criação de páginas da web interativas.

Para aprofundar seus conhecimentos em HTML, você pode consultar recursos adicionais, tutoriais e a [documentação oficial do HTML](https://developer.mozilla.org/pt-BR/docs/Web/HTML).