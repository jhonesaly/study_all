// Exemplo de script JavaScript

// Declaração de variáveis
let numero1 = 10;
let numero2 = 5;
let nome = "Chatty";
let condicao = true;

// Operações aritméticas
let soma = numero1 + numero2;
let subtracao = numero1 - numero2;
let multiplicacao = numero1 * numero2;
let divisao = numero1 / numero2;
let modulo = numero1 % numero2;

console.log(`Soma: ${soma}`);
console.log(`Subtração: ${subtracao}`);
console.log(`Multiplicação: ${multiplicacao}`);
console.log(`Divisão: ${divisao}`);
console.log(`Módulo: ${modulo}`);

// Estrutura condicional
if (condicao) {
  console.log("A condição é verdadeira.");
} else {
  console.log("A condição é falsa.");
}

// Laço de repetição - for
for (let i = 0; i < 5; i++) {
  console.log(`Iteração ${i}`);
}

// Função
function saudacao(nome) {
  console.log(`Olá, ${nome}!`);
}

saudacao(nome);

// Classe
class Pessoa {
  constructor(nome, idade) {
    this.nome = nome;
    this.idade = idade;
  }

  apresentar() {
    console.log(`Meu nome é ${this.nome} e tenho ${this.idade} anos.`);
  }
}

const pessoa1 = new Pessoa("João", 30);
pessoa1.apresentar();
