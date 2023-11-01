# CSS

CSS (Cascading Style Sheets) é uma linguagem de estilo utilizada para controlar a apresentação e o layout de elementos HTML em uma página da web. Ele desempenha um papel fundamental na criação de páginas da web atraentes e funcionais.

O link entre um arquivo css e o html se dá pela inclusão da tag <link rel="stylesheet" type="text/css" href="file_name.css"> dentro da tag <header> do html.

## Propriedades e Valores
As propriedades CSS determinam como os elementos serão estilizados. Cada propriedade tem um valor associado. Exemplos de propriedades incluem:
- `color`: Define a cor do texto.
- `font-size`: Define o tamanho da fonte.
- `margin`: Define as margens de um elemento.

## Cascata
O "C" em CSS significa "Cascading", o que se refere à hierarquia de regras. As regras CSS podem ser aplicadas de diferentes maneiras, com base na especificidade e na ordem em que são definidas.

## Seletores em CSS

Os seletores são parte fundamental do CSS, pois são usados para direcionar e estilizar elementos HTML específicos em uma página da web. Eles permitem que você especifique quais elementos devem receber as regras de estilo que você define. Aqui estão alguns tipos comuns de seletores e exemplos reais:

### 1. Seletor de Tipo
O seletor de tipo direciona todos os elementos HTML que correspondem a um determinado tipo. Por exemplo:
```css
p {
  font-size: 16px;
  color: blue;
}
```
Este seletor estilizará todos os parágrafos (`<p>`) na página, definindo o tamanho da fonte como 16 pixels e a cor do texto como azul.

### 2. Seletor de Classe
O seletor de classe direciona elementos que têm um atributo `class` específico definido em seu HTML. Por exemplo:
```css
.button {
  background-color: #ff6600;
  color: white;
}
```
Este seletor estilizará todos os elementos que têm a classe "button". Para aplicar essa classe a um elemento HTML, você faria algo assim:
```html
<button class="button">Clique Aqui</button>
```

### 3. Seletor de ID
O seletor de ID direciona um elemento HTML que possui um atributo `id` específico. No entanto, cada `id` deve ser único na página. Por exemplo:
```css
#header {
  font-size: 24px;
  text-align: center;
}
```
Este seletor estilizará o elemento com o `id` "header".

### 4. Seletor de Atributo
O seletor de atributo permite direcionar elementos com base em seus atributos. Por exemplo, você pode selecionar todos os links que têm um atributo `target="_blank"` da seguinte forma:
```css
a[target="_blank"] {
  text-decoration: underline;
}
```
Este seletor estilizará todos os links que abrem em uma nova janela ou guia com uma decoração de texto sublinhada.

### 5. Seletor Universal
O seletor universal (`*`) seleciona todos os elementos na página. É útil quando você deseja aplicar um estilo global a todos os elementos, mas deve ser usado com cuidado, pois pode afetar o desempenho da página.
```css
* {
  margin: 0;
  padding: 0;
}
```
Este seletor remove todas as margens e preenchimentos padrão de todos os elementos na página.

### 6. Seletor de Pseudo-classes e Pseudo-elementos
Além dos seletores básicos, existem pseudo-classes e pseudo-elementos que permitem direcionar elementos com base em estados ou partes específicas de um elemento. Por exemplo:
```css
a:hover {
  color: red;
}
```
Este seletor estilizará links quando o cursor do mouse estiver sobre eles.

Esses são apenas alguns exemplos de seletores em CSS. Dominar o uso eficaz de seletores é fundamental para aplicar estilos de maneira seletiva e precisa em sua página da web. Eles desempenham um papel crucial na estilização de elementos para criar um design coeso e atraente.

## Box Model em CSS

O Box Model é um conceito fundamental em CSS que descreve como os elementos HTML são dimensionados e espaçados na página. Cada elemento HTML é considerado um "caixa" que consiste em quatro partes principais: conteúdo, padding, border e margem.

### 1. Conteúdo (Content)

O conteúdo é a parte interna da caixa e inclui o texto, imagens ou qualquer outro conteúdo que o elemento contenha. É dimensionado usando as propriedades `width` (largura) e `height` (altura).

```css
div {
  width: 200px;
  height: 100px;
  background-color: #f2f2f2;
}
```

No exemplo acima, estamos definindo a largura e altura de uma `<div>` como 200 pixels por 100 pixels.

### 2. Preenchimento (Padding)

O preenchimento é uma área transparente ao redor do conteúdo dentro da caixa. Ele pode ser ajustado usando as propriedades `padding-top`, `padding-right`, `padding-bottom` e `padding-left`.

```css
div {
  padding: 20px; /* Define o mesmo preenchimento para todos os lados */
}
```

No exemplo acima, estamos adicionando 20 pixels de preenchimento em todos os lados da `<div>`.

### 3. Borda (Border)

A borda é uma linha ou contorno que envolve o conteúdo e o preenchimento. Você pode definir o estilo, largura e cor da borda usando as propriedades `border-style`, `border-width` e `border-color`.

```css
div {
  border: 2px solid #0077cc; /* Borda sólida de 2 pixels de largura em azul */
}
```

No exemplo acima, estamos adicionando uma borda sólida de 2 pixels de largura à `<div>` com a cor azul.

### 4. Margem (Margin)

A margem é uma área transparente ao redor da borda da caixa. Ela controla o espaço entre elementos na página. Você pode ajustar a margem usando as propriedades `margin-top`, `margin-right`, `margin-bottom` e `margin-left`.

```css
div {
  margin: 10px; /* Define a mesma margem para todos os lados */
}
```

No exemplo acima, estamos adicionando 10 pixels de margem em todos os lados da `<div>`.

### Exemplo Completo

Aqui está um exemplo completo que combina todas as partes do Box Model:

```css
.box {
  width: 200px;
  height: 100px;
  padding: 20px;
  border: 2px solid #0077cc;
  margin: 10px;
  background-color: #f2f2f2;
}
```

Este estilo será aplicado a um elemento HTML com a classe "box", criando uma caixa com conteúdo, preenchimento, borda, margem e fundo colorido.

Dominar o Box Model é essencial para controlar o layout e a aparência dos elementos em uma página da web. Ele permite que você crie designs precisos e responsivos, ajustando o tamanho das caixas e o espaçamento entre elas de acordo com suas necessidades.

## Flexbox em CSS

O Flexbox (abreviação de Flexible Box Layout) é um sistema de layout em CSS projetado para facilitar o posicionamento e a distribuição de elementos em uma página da web. Ele introduz um modelo de caixa unidimensional, onde os elementos são organizados em um único eixo (horizontal ou vertical) de acordo com as relações espaciais entre eles. Aqui está uma explicação mais abrangente e exemplos reais do uso do Flexbox:

### Conceitos-Chave do Flexbox:

#### 1. Eixos Principal e Cruzado:
- Eixo Principal: É o eixo principal de layout, ao longo do qual os itens flex são dispostos. Pode ser horizontal (no caso de `flex-direction: row`) ou vertical (no caso de `flex-direction: column`).
- Eixo Cruzado: É o eixo perpendicular ao eixo principal.

#### 2. Flex Container e Flex Items:
- Flex Container: É o elemento que contém os itens flex e é configurado com a propriedade `display: flex` ou `display: inline-flex`. Ele define o contexto para o layout flexível.
- Flex Items: São os elementos filhos diretos do flex container que se tornam itens flexíveis e são organizados de acordo com as regras do Flexbox.

#### 3. Propriedades Principais do Flex Container:
- `display`: Define se o elemento é um flex container (`flex`) ou um inline flex container (`inline-flex`).
- `flex-direction`: Define a direção principal em que os itens flex são colocados: `row`, `row-reverse`, `column` ou `column-reverse`.
- `justify-content`: Controla o alinhamento dos itens ao longo do eixo principal.
- `align-items`: Controla o alinhamento dos itens ao longo do eixo cruzado.
- `align-content`: Controla o alinhamento de linhas de itens quando há espaço extra no eixo cruzado.

### Exemplos de Uso do Flexbox:

#### Exemplo 1: Alinhar Itens Horizontalmente
```css
.container {
  display: flex;
  justify-content: center;
}

.item {
  width: 100px;
  height: 50px;
  background-color: #0077cc;
}
```
Neste exemplo, os itens dentro do contêiner são centralizados horizontalmente ao longo do eixo principal.

#### Exemplo 2: Criar um Layout de Colunas Flexíveis
```css
.container {
  display: flex;
  flex-direction: column;
}

.column {
  flex: 1;
  background-color: #f2f2f2;
  margin: 10px;
}
```
Neste exemplo, os elementos dentro do contêiner são organizados em uma coluna vertical, e as colunas flexíveis ajustam automaticamente seu tamanho para preencher o espaço disponível.

O Flexbox é uma ferramenta poderosa para criar layouts flexíveis e responsivos em CSS, tornando mais fácil a criação de designs complexos com menos código. Ele é especialmente útil quando se trata de alinhar e distribuir elementos em um único eixo.

## Pseudo-classes em CSS

As pseudo-classes em CSS são seletores que permitem estilizar elementos com base em estados ou características específicas que não podem ser selecionadas usando apenas seletores simples. Elas são indicadas por um "dois-pontos" (`:`) após o seletor e são usadas para aplicar estilos a elementos em estados específicos. Aqui estão algumas pseudo-classes comuns e exemplos de uso:

### 1. :hover
A pseudo-classe `:hover` é usada para estilizar um elemento quando o cursor do mouse está sobre ele. É frequentemente usada para criar efeitos de destaque em links e botões.

Exemplo:
```css
a:hover {
  color: #0077cc; /* Muda a cor do texto quando o mouse está sobre o link */
}
```

### 2. :active
A pseudo-classe `:active` é usada para estilizar um elemento quando ele está ativamente sendo clicado ou pressionado. É comumente usado para dar feedback visual imediato ao usuário durante uma interação de clique.

Exemplo:
```css
button:active {
  background-color: #ff6600; /* Muda a cor de fundo quando o botão está sendo clicado */
}
```

### 3. :focus
A pseudo-classe `:focus` é usada para estilizar um elemento quando ele está focado, geralmente após ser selecionado com o teclado ou com um dispositivo de entrada alternativo. É útil para melhorar a acessibilidade.

Exemplo:
```css
input:focus {
  border-color: #0077cc; /* Muda a cor da borda quando o campo de entrada está em foco */
}
```

### 4. :nth-child(n)
A pseudo-classe `:nth-child(n)` permite selecionar elementos com base em sua posição em relação aos irmãos. Você pode usar valores inteiros, fórmulas ou palavras-chave como "even" (par) e "odd" (ímpar).

Exemplo:
```css
ul li:nth-child(odd) {
  background-color: #f2f2f2; /* Estiliza as linhas ímpares em uma lista não ordenada */
}
```

## Media Queries em CSS

As Media Queries são uma técnica em CSS que permite aplicar estilos diferentes a um documento HTML com base nas características do dispositivo no qual o conteúdo está sendo exibido, como tamanho da tela, resolução, orientação e muito mais. Isso torna possível criar layouts responsivos que se ajustam automaticamente a diferentes dispositivos e tamanhos de tela. Aqui estão algumas explicações e exemplos de Media Queries:

### Sintaxe Básica de Media Query:

Uma Media Query é definida dentro de um bloco CSS usando a sintaxe `@media`, seguida de uma condição que descreve as características do dispositivo. Se a condição for atendida, as regras CSS dentro da Media Query serão aplicadas.

Exemplo de uma Media Query que aplica estilos a dispositivos com largura de tela menor que 600 pixels:

```css
@media (max-width: 600px) {
  /* Estilos a serem aplicados para telas menores que 600px de largura */
  body {
    font-size: 14px;
  }
}
```

### Principais Características das Media Queries:

- **`max-width` e `min-width`**: São usados para especificar faixas de largura de tela nas quais as regras CSS devem ser aplicadas.
- **`orientation`**: Permite segmentar dispositivos em modo retrato (`portrait`) ou paisagem (`landscape`).
- **`device-pixel-ratio`**: Permite segmentar dispositivos com densidade de pixels específica, útil para imagens de alta resolução (retina).
- **`hover`**: Segmenta dispositivos com capacidade de hover, como dispositivos com mouse.

### Exemplo HTML e CSS:

Aqui está um exemplo de HTML e CSS que usa uma Media Query para alterar o tamanho da fonte em dispositivos com largura de tela menor que 600 pixels:

HTML (entre a tag `<section>`):
```html
<section>
  <h2>Texto Responsivo</h2>
  <p>Este é um exemplo de texto que se ajusta automaticamente em dispositivos de tela pequena.</p>
</section>
```

CSS (dentro de um arquivo .css):
```css
/* Estilos gerais */
body {
  font-family: Arial, sans-serif;
  font-size: 16px;
}

/* Media Query para dispositivos de tela pequena */
@media (max-width: 600px) {
  body {
    font-size: 14px; /* Reduz o tamanho da fonte em telas menores que 600px */
  }
}
```

Neste exemplo, a Media Query verifica se a largura da tela é menor que 600 pixels e, se for verdadeira, aplica um estilo que reduz o tamanho da fonte do corpo (`body`) para tornar o texto mais legível em dispositivos de tela pequena.

Essa é apenas uma das muitas maneiras de usar Media Queries para criar layouts responsivos em CSS, permitindo que o design de um site se adapte de forma eficaz a uma variedade de dispositivos e tamanhos de tela.

## Conclusão

Este panorama fornece uma visão geral dos principais conceitos do CSS. Dominar CSS é essencial para o desenvolvimento web e pode ser especialmente útil ao criar estilos para páginas relacionadas ao concurso da Câmara dos Deputados organizado pela banca FGV.
