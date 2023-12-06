# Next JS

Next.js é um framework de desenvolvimento web em React que visa facilitar a criação de aplicativos React com renderização do lado do servidor (SSR) e geração de páginas estáticas. Ele simplifica a construção de aplicações web, oferecendo uma estrutura que suporta SSR, pré-renderização e roteamento simplificado. Com o Next.js, você pode criar páginas estáticas que são geradas de forma antecipada durante o build ou páginas dinâmicas que são geradas no momento da solicitação do cliente. Isso resulta em melhor desempenho e uma experiência mais rápida para os usuários. Além disso, o Next.js oferece suporte integrado para API routes, facilitando a criação de APIs junto com o desenvolvimento da interface do usuário. Essa abordagem integrada faz do Next.js uma escolha popular para desenvolvedores que buscam eficiência e desempenho em seus projetos web.

A documentação oficial do Next.js é um recurso valioso para aprender mais:

- [Documentação do Next.js](https://nextjs.org/docs/getting-started)

## Principais Funcionalidades

1. **Renderização do Lado do Servidor (SSR):** As páginas são renderizadas no servidor, melhorando o desempenho e a SEO.
2. **Geração de Páginas Estáticas:** Possibilidade de gerar páginas estáticas durante o build.
3. **API Routes:** Crie API endpoints de forma simples.

### Renderização

O Next.js oferece suporte a vários métodos de renderização, incluindo Server-Side Rendering (SSR), Single-Page Application (SPA), e Static Site Generation (SSG). Cada um desses métodos tem suas próprias características e casos de uso. Vamos explorar cada um deles:

1. **Server-Side Rendering (SSR):**
   - **O que é:** SSR envolve a renderização das páginas no servidor, entregando páginas totalmente renderizadas ao cliente.
   - **Como Funciona:** Quando um usuário acessa uma página, o servidor gera a página dinamicamente, incluindo dados específicos do usuário, e envia o HTML resultante para o cliente.
   - **Next.js e SSR:** Next.js facilita o SSR com a pasta `pages`. Páginas em `pages` são automaticamente tratadas como rotas e podem ser renderizadas do lado do servidor.

2. **Single-Page Application (SPA):**
   - **O que é:** SPA carrega uma página inicial e, em seguida, atualiza dinamicamente o conteúdo conforme o usuário interage com a aplicação sem recarregar a página.
   - **Como Funciona:** A aplicação é carregada uma vez, e as transições de página ocorrem no lado do cliente, geralmente usando JavaScript para manipular o DOM.
   - **Next.js e SPA:** Embora Next.js ofereça SSR por padrão, você pode optar por criar páginas que funcionem como SPAs se necessário, mas isso geralmente envolve mais configuração manual.

3. **Static Site Generation (SSG):**
   - **O que é:** SSG envolve a geração de páginas estáticas durante o processo de build, eliminando a necessidade de renderização no servidor ou no cliente durante a solicitação.
   - **Como Funciona:** As páginas são geradas antecipadamente durante o build, tornando-as prontas para serem entregues aos usuários sem a necessidade de processamento adicional no servidor.
   - **Next.js e SSG:** Next.js facilita o SSG com a geração de páginas estáticas durante o build. Páginas em `pages` podem ser configuradas para serem geradas estaticamente com a função `getStaticProps`.

**Relação com Next.js:**
- **SSR com Next.js:** Páginas em `pages` são por padrão renderizadas do lado do servidor, proporcionando SSR.
- **SPA com Next.js:** Embora o Next.js favoreça SSR, você pode optar por carregar dados no lado do cliente para criar páginas que se comportam como SPAs.
- **SSG com Next.js:** Utilizando a função `getStaticProps`, você pode gerar páginas estáticas durante o build, proporcionando benefícios de desempenho.

A escolha entre SSR, SPA e SSG dependerá dos requisitos específicos do seu projeto, considerando fatores como SEO, desempenho, e interatividade. O Next.js fornece uma flexibilidade notável para implementar esses métodos de renderização conforme necessário.

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

## NextAuth

**NextAuth.js - Resumo:**

NextAuth.js é uma biblioteca de autenticação para Next.js que simplifica a implementação de autenticação em aplicativos web. Ela oferece suporte a vários provedores de autenticação, como GitHub, Google, Facebook, entre outros, além de suportar autenticação local.

**Tutorial com Exemplo usando GitHub como Provedor:**

1. **Instalação:**
   - Instale o NextAuth.js e o pacote `@next-auth/github`:

     ```bash
     npm install next-auth @next-auth/github
     ```

2. **Configuração:**
   - Crie um arquivo `pages/api/auth/[...nextauth].js`:

     ```javascript
     import NextAuth from 'next-auth';
     import Providers from 'next-auth/providers';

     export default NextAuth({
       providers: [
         Providers.GitHub({
           clientId: process.env.GITHUB_CLIENT_ID,
           clientSecret: process.env.GITHUB_CLIENT_SECRET,
         }),
       ],
       pages: {
         signIn: '/auth/signin',
       },
     });
     ```

3. **Configuração do GitHub:**
   - Vá para o [GitHub Developer Settings](https://github.com/settings/developers).
   - Crie uma nova aplicação OAuth.
   - Configure a URL de autorização para `http://localhost:3000/api/auth/callback/github`.
   - Obtenha o Client ID e Client Secret e adicione ao seu arquivo de ambiente ou diretamente no código.

4. **Página de Login:**
   - Crie uma página `pages/auth/signin.js`:

     ```javascript
     import { signIn } from 'next-auth/react';

     export default function SignIn() {
       return (
         <div>
           <button onClick={() => signIn('github')}>Sign in with GitHub</button>
         </div>
       );
     }
     ```

5. **Página Protegida:**
   - Crie uma página `pages/protected.js` que requer autenticação:

     ```javascript
     import { useSession } from 'next-auth/react';

     export default function Protected() {
       const { data: session } = useSession();

       if (!session) {
         return <p>Acesso não autorizado. Faça login primeiro.</p>;
       }

       return (
         <div>
           <h1>Página Protegida</h1>
           <p>Bem-vindo, {session.user.name}!</p>
         </div>
       );
     }
     ```

6. **Uso nas Páginas:**
   - Utilize `useSession` para acessar informações de sessão em qualquer página.

Este é um exemplo básico para começar com NextAuth.js usando o GitHub como provedor de autenticação. Certifique-se de ajustar as configurações conforme necessário e consulte a [documentação oficial do NextAuth.js](https://next-auth.js.org/) para informações detalhadas e opções avançadas.
