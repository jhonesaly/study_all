# Typescript

TypeScript é uma linguagem de programação de código aberto desenvolvida pela Microsoft. Ela é uma extensão do JavaScript que adiciona tipos estáticos opcionais ao código. Isso proporciona uma camada adicional de verificação de erros durante o desenvolvimento.

Para mais informações, consulte a [documentação oficial do TypeScript](https://www.typescriptlang.org/).

## Principais Características

- **Tipagem Estática:** Permite a definição de tipos para variáveis, parâmetros de função e retornos, melhorando a detecção de erros em tempo de desenvolvimento. JavaScript também suporta programação orientada a objetos, incluindo classes, herança, polimorfismo e outros conceitos. No entanto, o TypeScript fornece uma camada adicional de tipagem estática, o que significa que você pode definir explicitamente os tipos de dados. Isso pode ajudar a evitar erros comuns durante o desenvolvimento, oferecendo uma experiência mais robusta em termos de orientação a objetos.

- **Compatibilidade:** O código TypeScript é transcompilado para JavaScript, tornando-o compatível com qualquer ambiente que suporte JavaScript.

## Instalação

Para começar a usar TypeScript, você pode instalá-lo via npm (Node Package Manager) usando o seguinte comando:

```bash
npm install typescript  -D
```

A tag '-D' indica que é um pacote de desenvolvimento pois código em typescript não vai para produção e tudo que é produzido é transpilado para javascript.

Após a instalação, dê o seguinte comando na pasta do projeto:

```bash
npx tsc --init
```

Dependendo do que for usar no projeto, instale as dependências específicas:

```bash
npm install @types/node @types/react @types/react-dom @types/jest @types/styled-components -D
```

## Compilação e Execução

Após escrever seu código TypeScript (arquivos com extensão `.ts`), você pode compilá-lo para JavaScript usando o comando:

```bash
tsc nome-do-arquivo.ts
```

O código JavaScript resultante pode ser executado em um ambiente que suporte JavaScript.

## Exemplo

   ```typescript
   // Definindo um tipo
   type Pessoa = {
     nome: string;
     idade?: number; //? indica que é opcional
   };

   // Função que recebe um parâmetro do tipo Pessoa
   function saudacao(pessoa: Pessoa): string {
     return `Olá, ${pessoa.nome}! Você tem ${pessoa.idade} anos.`;
   }

   // Exemplo de utilização
   const pessoaExemplo: Pessoa = { nome: "João", idade: 25 };
   console.log(saudacao(pessoaExemplo));
   ```

   Neste exemplo, a função `saudacao` espera um parâmetro do tipo `Pessoa` e retorna uma saudação personalizada.

## Tipo Global

Para criar um tipo global em TypeScript, você pode criar um arquivo de declaração de tipo (arquivo `.d.ts`) e colocá-lo em uma pasta chamada `@types` na raiz do seu projeto. Essa pasta `@types` é especial no TypeScript e será automaticamente reconhecida.

Aqui estão os passos básicos para criar um tipo global:

1. **Crie um arquivo de declaração de tipo:**
   - Por exemplo, você pode criar um arquivo chamado `global.d.ts`. Este arquivo conterá suas declarações de tipo global.

2. **Defina seus tipos globais:**
   - No arquivo `global.d.ts`, você pode declarar os tipos globais que deseja adicionar. Por exemplo:

     ```typescript
     // global.d.ts

     declare interface MeuTipoGlobal {
       nome: string;
       idade: number;
     }
     ```

3. **Coloque o arquivo na pasta `@types`:**
   - Mova o arquivo `global.d.ts` para uma pasta chamada `@types` na raiz do seu projeto.

     ```
     projeto/
     ├── @types/
     │   └── global.d.ts
     └── outros-arquivos...
     ```

Após seguir esses passos, o TypeScript automaticamente reconhecerá os tipos definidos em `global.d.ts` como tipos globais no seu projeto. Agora você pode usar `MeuTipoGlobal` em qualquer lugar do seu código TypeScript sem a necessidade de importação.

Lembre-se de que, ao criar tipos globais, é uma boa prática garantir que esses tipos não entrem em conflito com os existentes no ecossistema do TypeScript. Se você estiver criando tipos para bibliotecas de terceiros, considere verificar se já existem tipos disponíveis ou contribuir para definições de tipos existentes.
