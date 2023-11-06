# React

O React é uma biblioteca JavaScript de código aberto amplamente utilizada para a criação de interfaces de usuário interativas e dinâmicas. Desenvolvido e mantido pelo Facebook, o React se destaca por sua abordagem baseada em componentes e sua capacidade de construir aplicativos da web eficientes e reativos.

## Principais Características

- **Componentização**: O React permite que você divida a interface do usuário em componentes reutilizáveis e independentes. Cada componente representa uma parte específica da interface e pode ser facilmente composto para criar interfaces complexas.

- **Virtual DOM**: O React utiliza um Virtual DOM para otimizar as atualizações de interface. Ele compara o estado atual da interface com o estado anterior e faz as atualizações necessárias apenas nas partes que mudaram, melhorando significativamente o desempenho.

- **Unidirecionalidade de Dados**: O React segue o princípio de fluxo unidirecional de dados. Os dados fluem de pais para filhos por meio de props, tornando o rastreamento de dados e o depuramento mais previsíveis.

- **JSX**: O React introduz o JSX (JavaScript XML), uma extensão do JavaScript que permite a criação de elementos de interface de forma declarativa e intuitiva.

- **Ecosistema Rico**: O React possui um ecossistema robusto de bibliotecas e ferramentas, incluindo o React Router para gerenciamento de rotas, o Redux para gerenciamento de estado global e muitos outros recursos.

## Vantagens

- Alta performance devido ao Virtual DOM.
- Facilidade de teste de componentes isolados.
- Comunidade ativa e vasta documentação.
- Reutilização de componentes acelera o desenvolvimento.

## Desvantagens

- Curva de aprendizado inicial, especialmente para iniciantes em JavaScript.
- Pode exigir configuração adicional usando ferramentas como o Create React App.
- Gerenciamento de estado em aplicativos maiores pode ser complexo.

## Tutorial


### Iniciando o React

Para começar um projeto em react, use no terminal:

```
npx create-react-app nome_do_app
```

em que nome_do_app é o nome do projeto e será o nome da pasta criada, que ficará inicialmente assim:

![Projeto inicial](images/react_app_inicial.png)

Então, mude o terminal para a pasta criada:

```
cd nome_do_app
```

E para rodar o react, use:

```
npm run start
```
### Criando componente

Os componentes devem ser criados separadamente dentro da pasta /components dentro da pasta /src.

![Components](images/react_components.png)

Veja o conteúdo do BotaoContador.js:

```
import React, { useState } from 'react';

function BotaoContador() {
    const [contador, setContador] = useState(0);
  
    const aumentarContador = () => {
      setContador(contador + 1);
    };
  
    const diminuirContador = () => {
      setContador(contador - 1);
    };
  
    return (
      <div>
        <h1>Contador: {contador}</h1>
        <button onClick={aumentarContador}>Aumentar</button>
        <button onClick={diminuirContador}>Diminuir</button>
      </div>
    );
  }
  export default BotaoContador;
```

Com isso, o componente pode ser importado pelo index.js na raiz do projeto assim:


```
...
import BotaoContador from './components/BotaoContador';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
    <BotaoContador />
  </React.StrictMode>
);
...

```

Para facilitar a integração com arquivo css posterior, o arquivo pode ser criado dentro de uma pasta (ex: Button) e dentro dela o arquivo index.js de modo que, quando a pasta for indicada, o .js será usado automaticamente como em:

```
import Button from './components/Button'
```

### Usando fonte especial

**Passo 1: Preparando sua Fonte**

Certifique-se de ter a fonte que deseja adicionar ao seu projeto no formato correto (normalmente .ttf ou .otf). Você deve ter a fonte pronta para uso.

**Passo 2: Organizando a Estrutura do Projeto**

Em seu projeto React, crie uma pasta chamada "fonts" na raiz do projeto. Esta pasta conterá seus arquivos de fonte.

**Passo 3: Adicionando a fonte ao Projeto**

No arquivo global.js, em que são configurados os estilos globais, Siga os seguintes passos:

a. **Importe a Fonte:** No arquivo de estilos do seu componente (geralmente um arquivo .js ou .css), importe a fonte.

```javascript
import { createGlobalStyle } from 'styled-components'
import SuaFonte from './fonts/SuaFonte.ttf';
```

b. **Defina o `@font-face`:** Dentro das definições de estilo do seu componente, crie uma regra `@font-face` para a sua fonte.

```javascript
`...
  @font-face {
    font-family: 'SuaFonte';
    src: url(${SuaFonte}) format('truetype');
  }
`
```

**Passo 3: Importando a Fonte no Estilo do Componente**

No componente onde deseja usar a fonte, use a fonte normalmente:

```javascript
  font-family: 'LEDCalculator';
```

## Biblioteca styled-components

A biblioteca "styled-components" é popular para estilização de componentes em aplicações React. Ela permite que você defina estilos CSS diretamente em seus componentes React usando uma sintaxe similar ao CSS-in-JS. Com "styled-components", você pode criar componentes estilizados reutilizáveis que encapsulam seu estilo e lógica, tornando seu código mais modular e legível.

Comece instalando o pacote:

```
npm install styled-components
```

Na pasta do componenete, crie um arquivo chamado styles.js e importe o pacote:

```
import styled from 'styled-components';
```

nesse arquivo, crie a estilização para o componenete:

```
export const StyledButton = styled.button`
  background-color: #007bff;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;

  &:hover {
    background-color: #0056b3;
  }
`;

```

Agora, no arquivo com a lógica do componenete (index.js), importe a estilização:

```
import { ButtonContainer } from './styles';

const Button = ({label, onClick}) => {
    return (
      <ButtonContainer onClick={onClick} type="button">
       {label}
      </ButtonContainer>
    );
  }
  
  export default Button;
```

Nessa lógida, o componenete Button terá o css definido em ButtonContainer.

Também é possível criar styles globalmente oi meio de um arquivo global.js na raiz do projeto:

```
import { createGlobalStyle } from 'styled-components'

export default createGlobalStyle`
  *, body {
    margin: 0;
    padding: 0;
  }
`
```

Depois importando no index.js da raiz do projeto:

```
import GlobalStyles from './global';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <GlobalStyles />
    <App />
  </React.StrictMode>
);
```

## Conseguindo componentes

1. **npm (Node Package Manager):** O npm é o repositório de pacotes JavaScript mais utilizado. Você pode procurar por componentes React prontos, bibliotecas e pacotes relacionados ao seu projeto. Para instalar um pacote, você pode usar o comando `npm install`.

2. **GitHub:** O GitHub é uma plataforma de hospedagem de código fonte que contém muitos projetos open source. Você pode procurar por repositórios de componentes React e baixar o código-fonte ou instalar as bibliotecas diretamente em seu projeto.

3. **npmjs.com:** O site do npm, npmjs.com, possui uma interface de busca amigável para encontrar pacotes JavaScript, incluindo componentes React.

4. **React Components Websites:** Existem sites dedicados a listar e compartilhar componentes React. Alguns exemplos incluem "React Awesome" (https://github.com/enaqx/awesome-react) e "React Components" (https://reactjs.org/community/ui-components.html).

5. **Material-UI, Ant Design, Bootstrap, etc.:** Muitas bibliotecas populares de design e UI, como Material-UI, Ant Design e Bootstrap, oferecem componentes React prontos para uso. Você pode encontrar essas bibliotecas em seus respectivos sites e documentações.

6. **Plataformas de Componentes:** Algumas plataformas online oferecem componentes React personalizáveis e prontos para uso, como Bit (https://bit.dev/), Storybook (https://storybook.js.org/), e mais.

Lembre-se sempre de verificar a documentação e as instruções de instalação de qualquer componente que você escolher para entender como usá-lo em seu projeto. Certifique-se de que os componentes escolhidos são compatíveis com a versão do React que você está usando.

Além disso, ao usar componentes de terceiros, considere verificar sua popularidade, manutenção ativa e compatibilidade com seu projeto, para garantir uma integração suave e um desenvolvimento eficiente.

## Ciclo dos componenetes

O ciclo de vida de um componente em uma aplicação React é uma série de eventos que ocorrem durante a vida útil desse componente, desde sua criação até sua remoção. Esses eventos permitem que você controle o comportamento e a interação do componente com o DOM e com os dados. Aqui está um resumo dos principais estágios do ciclo de vida de um componente React:

1. **Montagem (Mounting):**
   - `constructor()`: É chamado quando um componente é inicializado. Você pode configurar o estado inicial e vincular métodos aqui.
   - `static getDerivedStateFromProps()`: Chamado antes da renderização quando as props são recebidas. Raramente usado, geralmente para computar um novo estado com base nas props.
   - `render()`: Obrigatório. Renderiza o componente e seus elementos filhos no DOM virtual.
   - `componentDidMount()`: Chamado após o componente ser inserido no DOM real. É o lugar apropriado para carregar dados externos ou executar operações que dependem do DOM.

2. **Atualização (Updating):**
   - `static getDerivedStateFromProps()`: Novamente, pode ser usado para atualizar o estado com base nas novas props.
   - `shouldComponentUpdate()`: Permite otimizar o desempenho decidindo se a atualização e a renderização devem ocorrer. Pode retornar `true` ou `false`.
   - `render()`: Re-renderiza o componente se `shouldComponentUpdate` retornar `true`.
   - `getSnapshotBeforeUpdate()`: Pode ser usado para capturar informações do DOM antes de sofrer atualizações.
   - `componentDidUpdate()`: Chamado após a renderização e atualização do componente. Útil para ações pós-atualização, como chamadas de API.

3. **Desmontagem (Unmounting):**
   - `componentWillUnmount()`: Chamado antes do componente ser removido do DOM. Útil para limpar recursos, cancelar assinaturas, etc.

4. **Manejo de Erros (Error Handling):**
   - `static getDerivedStateFromError()`: Usado para atualizar o estado quando ocorre um erro em qualquer componente filho.
   - `componentDidCatch()`: Usado para lidar com erros em componentes filhos. Geralmente usado para registro de erros.

É importante notar que com a introdução dos Hooks (a partir do React 16.8), como `useState`, `useEffect`, `useContext`, etc., o ciclo de vida dos componentes baseados em classe não é mais a única maneira de gerenciar o estado e os efeitos em componentes React. Hooks oferecem uma abordagem mais simples e funcional para alcançar os mesmos resultados, tornando o código mais legível e fácil de manter.

Portanto, ao desenvolver em React, você pode escolher entre componentes baseados em classe com o ciclo de vida tradicional ou componentes funcionais com Hooks, dependendo das suas preferências e necessidades. Os Hooks têm se tornado a abordagem mais comum devido à sua simplicidade e flexibilidade.

## Conclusão

O React é uma escolha popular para o desenvolvimento de aplicativos da web modernos devido à sua eficiência, flexibilidade e comunidade ativa. Com sua abordagem baseada em componentes e recursos avançados, ele continua a ser uma ferramenta poderosa para construir interfaces de usuário dinâmicas e interativas.

Para saber mais sobre o React, consulte a [documentação oficial](https://reactjs.org/).