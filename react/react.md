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

## Conseguindo componentes

Sim, você pode encontrar componentes prontos de React em diversos lugares. Aqui estão algumas opções populares:

1. **npm (Node Package Manager):** O npm é o repositório de pacotes JavaScript mais utilizado. Você pode procurar por componentes React prontos, bibliotecas e pacotes relacionados ao seu projeto. Para instalar um pacote, você pode usar o comando `npm install`.

2. **GitHub:** O GitHub é uma plataforma de hospedagem de código fonte que contém muitos projetos open source. Você pode procurar por repositórios de componentes React e baixar o código-fonte ou instalar as bibliotecas diretamente em seu projeto.

3. **npmjs.com:** O site do npm, npmjs.com, possui uma interface de busca amigável para encontrar pacotes JavaScript, incluindo componentes React.

4. **React Components Websites:** Existem sites dedicados a listar e compartilhar componentes React. Alguns exemplos incluem "React Awesome" (https://github.com/enaqx/awesome-react) e "React Components" (https://reactjs.org/community/ui-components.html).

5. **Material-UI, Ant Design, Bootstrap, etc.:** Muitas bibliotecas populares de design e UI, como Material-UI, Ant Design e Bootstrap, oferecem componentes React prontos para uso. Você pode encontrar essas bibliotecas em seus respectivos sites e documentações.

6. **Plataformas de Componentes:** Algumas plataformas online oferecem componentes React personalizáveis e prontos para uso, como Bit (https://bit.dev/), Storybook (https://storybook.js.org/), e mais.

Lembre-se sempre de verificar a documentação e as instruções de instalação de qualquer componente que você escolher para entender como usá-lo em seu projeto. Certifique-se de que os componentes escolhidos são compatíveis com a versão do React que você está usando.

Além disso, ao usar componentes de terceiros, considere verificar sua popularidade, manutenção ativa e compatibilidade com seu projeto, para garantir uma integração suave e um desenvolvimento eficiente.

## Conclusão

O React é uma escolha popular para o desenvolvimento de aplicativos da web modernos devido à sua eficiência, flexibilidade e comunidade ativa. Com sua abordagem baseada em componentes e recursos avançados, ele continua a ser uma ferramenta poderosa para construir interfaces de usuário dinâmicas e interativas.

Para saber mais sobre o React, consulte a [documentação oficial](https://reactjs.org/).