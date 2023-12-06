# Next JS

Next.js é um framework de desenvolvimento web em React que visa facilitar a criação de aplicativos React com renderização do lado do servidor (SSR) e geração de páginas estáticas. Ele simplifica a construção de aplicações web, oferecendo uma estrutura que suporta SSR, pré-renderização e roteamento simplificado. Com o Next.js, você pode criar páginas estáticas que são geradas de forma antecipada durante o build ou páginas dinâmicas que são geradas no momento da solicitação do cliente. Isso resulta em melhor desempenho e uma experiência mais rápida para os usuários. Além disso, o Next.js oferece suporte integrado para API routes, facilitando a criação de APIs junto com o desenvolvimento da interface do usuário. Essa abordagem integrada faz do Next.js uma escolha popular para desenvolvedores que buscam eficiência e desempenho em seus projetos web.

## Principais Funcionalidades

1. **Renderização do Lado do Servidor (SSR):** As páginas são renderizadas no servidor, melhorando o desempenho e a SEO.
2. **Geração de Páginas Estáticas:** Possibilidade de gerar páginas estáticas durante o build.
3. **API Routes:** Crie API endpoints de forma simples.


## Configuração

**Instalação do Next.js com npm:**

1. Abra o terminal e navegue até o diretório do seu projeto.
2. Execute o seguinte comando para criar um novo projeto Next.js:

```bash
npx create-next-app nome-do-seu-projeto
```

3. Entre no diretório do projeto:

```bash
cd nome-do-seu-projeto
```

**Estrutura básica do projeto:**

O Next.js segue uma estrutura de pastas organizada. Os principais diretórios incluem:

- **`pages`**: Contém arquivos que definem as rotas da sua aplicação.
- **`public`**: Armazena arquivos estáticos como imagens.
- **`styles`**: Contém arquivos de estilo (CSS, SCSS, etc.).

**Desenvolvimento local:**

1. Inicie o servidor de desenvolvimento:

```bash
npm run dev
```

2. Acesse `http://localhost:3000` no seu navegador para ver a aplicação em execução.

## Páginas

### Criação

1. Crie um novo arquivo na pasta `pages`, por exemplo, `pagina.js`.
2. Adicione o conteúdo da página no arquivo.

```jsx
// Exemplo de conteúdo em pagina.js
import React from 'react';

function Pagina() {
  return (
    <div>
      <h1>Minha Nova Página</h1>
      <p>Bem-vindo ao Next.js!</p>
    </div>
  );
}

export default Pagina;
```

### Navegação

O Next.js facilita a navegação entre páginas usando o componente `Link`:

```jsx
import Link from 'next/link';

function Navegacao() {
  return (
    <div>
      <Link href="/pagina">
        <a>Ir para Minha Nova Página</a>
      </Link>
    </div>
  );
}

export default Navegacao;
```

## Documentação

A documentação oficial do Next.js é um recurso valioso para aprender mais:

- [Documentação do Next.js](https://nextjs.org/docs/getting-started)
