# CSS

CSS (Cascading Style Sheets) é uma linguagem de estilo utilizada para controlar a apresentação e o layout de elementos HTML em uma página da web. Ele desempenha um papel fundamental na criação de páginas da web atraentes e funcionais. Aqui estão alguns conceitos essenciais sobre CSS:

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

## Propriedades e Valores
As propriedades CSS determinam como os elementos serão estilizados. Cada propriedade tem um valor associado. Exemplos de propriedades incluem:
- `color`: Define a cor do texto.
- `font-size`: Define o tamanho da fonte.
- `margin`: Define as margens de um elemento.

## Cascata
O "C" em CSS significa "Cascading", o que se refere à hierarquia de regras. As regras CSS podem ser aplicadas de diferentes maneiras, com base na especificidade e na ordem em que são definidas.

## Box Model
O modelo de caixa é fundamental no CSS e descreve como os elementos HTML são dimensionados e espaçados. Ele inclui propriedades como `width`, `height`, `margin`, `padding` e `border`.

## Flexbox e Grid
Flexbox e Grid são sistemas de layout avançados que simplificam a criação de layouts complexos e responsivos.

## Media Queries
As media queries permitem que você aplique estilos diferentes com base nas características do dispositivo, como tamanho da tela, orientação e resolução.

## Transições e Animações
CSS permite criar transições suaves e animações para elementos, tornando as páginas da web mais interativas.

Este panorama fornece uma visão geral dos principais conceitos do CSS. Dominar CSS é essencial para o desenvolvimento web e pode ser especialmente útil ao criar estilos para páginas relacionadas ao concurso da Câmara dos Deputados organizado pela banca FGV.
