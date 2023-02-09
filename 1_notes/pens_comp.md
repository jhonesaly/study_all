# Pensamento computacional

Definição: Processo de pensamento envolvido na expressão de soluções em passos computacionais ou algoritmos que podem ser implementados no computador.

Pilares:

- Decomposição: Dividir um problema complexo em subproblemas
- Reconhecimento de padrões: Identificar padrões ou tendências
- Abstração: Extrapolar o conceito do problema para um forma generalista
- Design de algoritmos: Definir passo a passo a solução do problema.

Habilidades necessárias:

- Raciocínio lógico
- Aperfeiçoamento

**Raciocínio Lógico**: é uma forma de pensamento estruturado, ou raciocínio, que permite encontrar a conclusão ou determinar a resolução de um problema.

Classificação:

- Inferência
    - Sintética
        - Indução: observação -> generalização
        - Abdução: conclusão -> premissa
    - Analítica
        - Dedução: leis e teorias -> previsão


**Aperfeiçoamento**: A partir de uma solução, determinar pontos de melhora e refinamento

Processo:

- Encontrar solução eficiente
- Otimizar processos
- Simplificar linhas de códigos
- Funções bem definidas

## Decomposição

Primeiro passo da resolução de problemas dentro do conceito de pensamento computacional

Passos:

- Análise: processo de quebrar e determinar partes menores e gerenciáveis
- Síntese: Combinar os elementos recompondo o problema original
- Estratégia: Ordem de execução de tarefas menores
    - Sequencial
    - Paralelo

## Padrões

Modelo que possui uma estrutura que é repetida. Isso possibilita a generalização

Reconhecimento:

- Similaridades
- Diferenças

## Abstração

Observar, um ou mais elementos, analisando suas características separadamente da realidade, tornando-as mais gerais e amplas.

## Algoritmos

Processo de resolução de problemas "step by step". Necessário para que o computador possa ser utilizado.

----
# Lógica de Programação

Problema: é uma questão que foge a uma determinada regra ou um desvio de percurso, o qual impede de atingir um objetivo com eficiência e eficácia.

Lógica: parte da filosofia que trata das formas do pensamento em geral e das operações intelectuais que visam à determinação do que é verdadeiro ou não.

Lógica de programação: organização e planejamento das instruções assertivas em um algoritmo, a fim de viabilizar a implementação de um programa.

Técnicas:

- Linear: execução sequenciada de uma série de operações, com recursos limitados e uma única dimensão.
- Estruturada: organização, disposição e ordem dos elementos essenciais que compõem um corpo. A diferença é que determinadas estruturas possuem mais de uma possibilidade (seria o "if else")
- Modular: partes independentes que são controladas por um conjunto de regras específicas.

----
# Algoritmos

## Variáveis

Pode assumir qualquer um dos valores de um determinado conjunto de valores.

Tipos:

- Numéricos (int e float)
- Caracteres (string)
- Lógicos (bool)

Papéis:

- Ação: Modifica estado do programa
- Controle: informa que algo mudou ou problema
- Constante: não é alterada (pi)

Boas práticas:

- nome tenha sentido prático (não utilizar incógnitas como "x", "y", "z")
- não usar palavras reservadas


## Instruções

São linguagens de palavras-chave (vocabulário) de uma determinada linguagem de programação que tem por finalidade comandar um computador que irá tratar os dados.

Operadores primitivos:

- binário: + - / * ** %
- unário: + e - (sinal de um número, não operação)

Estruturas condicionais:

- igual ==
- diferente !=
- maior >
- menor <
- lógicos:
    - e
    - ou 
    - not

Estruturas de repetição:

- while
- for

## Funções 

são blocos de instruções que realizam tarefas específicas, identificados por nomes e parâmetros

elementos de função:

- Definição
- Nome
- Invocação
- Variável local 

## Estrutura da dados

vetores: caracterizado por uma variável dimensionada com tamanho pré-fixado

matriz: é uma tabela organizada em linhas e colunas no formato m x n, onde m representa o número de linha e n o de colunas.

------
# Linguagens de programação

Linguagem de programação: método padronizado composto por um conjunto de regras sintáticas e semânticas de implementação de um código fonte.

Primeira linguagem: Assembly (linguagem de máquina)

Paradigmas

Problemas computacionais:

- Decisão
- Busca
- Otimização

Estrutura da operação:

- Programa fonte: software escrito em linguagem de alto nível.
- Compilador: executa análise do programa e transforma em um programa objeto.
- Programa objeto: software escrito em linguagem de baixo nível, como assembly.

Tipos de linguagem:

- Tradução: processo de transformar um programa fonte em um programa objeto. (ex: C++)
- Interpretação: processo de leitura direta do programa fonte. Faz a linguagem mais lenta, porém mais flexível. (ex: python, ruby, JavaScript)
- Transpilação: processo de transformar um programa fonte em uma linguagem de alto nível para uma linguagem também de alto nível, porém menor. (ex: typescript)

Diretrizes de desenvolvimento:

- Legibilidade: facilidade de leitura e coerente.
- Redigibilidade: facilidade de escrita e reuso.
- Confiabilidade: faz o que foi programado para fazer.
- Custo: análise de impacto de recursos.
- Disponibilidade de ferramentas
- Comunidade ativa
- Adoção pelo mercado
- Atualizações

## Compilador

Tipos de análise do compilador:

- Lexical
- Syntax
- Semantic

Etapas análise léxica:

- Particionar: separar o código fontes em elementos relevantes, chamados tokens.
- Classificar: identifica os tokens em palavras reservadas, funções, etc.
- Eliminar: comentários, trechos em branco e outros elementos que são mais para a compreensão do desenvolvedor

Análise sintática: componente do sistema linguístico que interligam os constituintes da sentença, atribuindo-lhe uma estrutura, conferindo a correção do programa.

Análise semântica: é o estudo do significado. Incide sobre a relação entre significantes, como: palavras, frases, sinais e símbolos. Verifica a lógica do programa.

## Paradigmas de programação

Forma de resolução de problemas com diretrizes e limitações específicas utilizando linguagem de programação

**Estruturado**: estrutura de blocos aninhados, com ênfase na sequência para atacar diretamente problemas. (C++, C, JavaScript, Java)

**Orientação à objetos**: tenta reproduzir o mundo real, representando objetos e suas interações, facilitando o reuso de código (Python, lua, C++, Java)

> objeto: descrito por características específicas (Atributos), comportamentos (Métodos) e circunstâncias (Estados)

Pilares da orientação à objeto:

- Herança: classe filha recebe as características da classe mãe (mais geral)
- Encapsulamento: 
- Polimorfismo: 
- Abstração: 

Outros paradigmas:

- Computação distribuída: funções executadas de forma independente. (Ada)
- Lógico
- Procedural: chamada sucessiva e procedimentos separados. (Fortran, lua)
- Funcional: instruções são baseadas em funções (lua, JavaScript, Java, Python)