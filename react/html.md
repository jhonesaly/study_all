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

- `<h1>`, `<h2>`, `<h3>`, `<h4>`, `<h5>`, `<h6>`: São usados para criar títulos de diferentes níveis de importância.

- `<header>`: Indicar cabeçalho

- `<p>`: É usado para criar parágrafos de texto.

- `<a>`: É usado para criar links para outras páginas da web ou recursos.

- `<img>`: É usado para inserir imagens na página.

- `<ul>` e `<ol>`: São usados para criar listas não ordenadas (com marcadores) e listas ordenadas (com números ou letras), respectivamente.

- `<li>`: É usado para definir itens de lista dentro de `<ul>` ou `<ol>`.

- `<div>`: É um elemento de divisão usado para agrupar e estruturar conteúdo.

- `<strong>` e `<em>`: Usadas para enfatizar texto, onde `<strong>` geralmente indica ênfase forte (geralmente exibido em negrito) e `<em>` indica ênfase enfática (geralmente exibido em itálico).

- `<a>` (com o atributo `target="_blank"`): Ao adicionar `target="_blank"` a um link `<a>`, você pode fazer com que o link seja aberto em uma nova janela ou guia do navegador.

- `<br>`: Usado para criar uma quebra de linha dentro de um texto ou parágrafo.

- `<hr>`: É uma linha horizontal que é frequentemente usada para separar conteúdo em uma página.

- `<span>`: Semelhante ao `<div>`, o `<span>` é usado para agrupar elementos inline e aplicar estilos ou manipulações de script a eles.

- `<table>`, `<tr>`, `<td>`: São usados para criar tabelas e suas células. Embora tabelas tenham sido amplamente usadas para layout no passado, elas ainda são valiosas para exibir dados tabulares.

- `<figure>` e `<figcaption>`: Usados para agrupar imagens e fornecer uma legenda associada à imagem usando o `<figcaption>`.

- `<abbr>`: Usado para definir uma abreviação ou acrônimo, e você pode usar o atributo `title` para fornecer uma explicação completa.

- `<cite>`: Usado para marcar títulos de obras, como livros, filmes ou artigos, que você está citando em seu conteúdo.

- `<q>`: Usado para citar o texto dentro das aspas, indicando que é uma citação. Pode ser usado para fins de formatação.

- `<del>` e `<ins>`: Usados para marcar texto deletado ou inserido, úteis em revisões de texto ou documentos.

- `<time>`: Usado para representar datas e horários, fornecendo informações semânticas para os motores de busca e leitores de tela.

- `<mark>`: Usado para destacar partes de texto dentro de um conteúdo.

- `<details>` e `<summary>`: Usados para criar elementos de detalhes expansíveis e contráteis, úteis para exibir informações adicionais de forma condensada.

- `<progress>`: Usado para criar barras de progresso, indicando o progresso de uma tarefa.

- `<meter>`: Usado para representar uma medida escalar em uma faixa conhecida, como uma avaliação de 0 a 10.

Essas são algumas das tags menos usadas, mas que podem ser valiosas em cenários específicos. A escolha das tags depende do contexto e dos requisitos do seu projeto. Certifique-se de consultar a documentação oficial do HTML ou recursos adicionais para obter informações detalhadas sobre essas tags e como usá-las de maneira apropriada.

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