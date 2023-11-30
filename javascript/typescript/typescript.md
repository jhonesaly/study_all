# Typescript

TypeScript é uma linguagem de programação de código aberto desenvolvida pela Microsoft. Ela é uma extensão do JavaScript que adiciona tipos estáticos opcionais ao código. Isso proporciona uma camada adicional de verificação de erros durante o desenvolvimento.

Para mais informações, consulte a [documentação oficial do TypeScript](https://www.typescriptlang.org/).

## Principais Características

- **Tipagem Estática:** Permite a definição de tipos para variáveis, parâmetros de função e retornos, melhorando a detecção de erros em tempo de desenvolvimento. JavaScript também suporta programação orientada a objetos, incluindo classes, herança, polimorfismo e outros conceitos. No entanto, o TypeScript fornece uma camada adicional de tipagem estática, o que significa que você pode definir explicitamente os tipos de dados. Isso pode ajudar a evitar erros comuns durante o desenvolvimento, oferecendo uma experiência mais robusta em termos de orientação a objetos.

- **Compatibilidade:** O código TypeScript é transcompilado para JavaScript, tornando-o compatível com qualquer ambiente que suporte JavaScript.

## Instalação

Para começar a usar TypeScript, você pode instalá-lo via npm (Node Package Manager) usando o seguinte comando:

```bash
npm install -g typescript
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
     idade: number;
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
