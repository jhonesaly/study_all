# Structural Pattern Matching

Structural Pattern Matching (SPM) em Python é uma funcionalidade introduzida na versão 3.10 que permite a correspondência de padrões em valores de dados complexos, como tuplas, listas, dicionários, entre outros.

A correspondência de padrões é uma técnica de programação que permite selecionar o código a ser executado com base no valor de entrada. Em vez de usar vários if-else ou switch-case aninhados, o structural pattern matching permite que você combine diferentes padrões em uma única expressão.

A correspondência de padrões em Python oferece algumas vantagens em relação ao uso de estruturas condicionais tradicionais como if, elif, else.

Aqui estão alguns motivos pelos quais você pode querer usar a correspondência de padrões:

- É mais legível: Quando você tem vários casos para verificar, o uso de if, elif, else pode levar a um código mais confuso e difícil de ler. A correspondência de padrões pode tornar o código mais claro e fácil de entender.
- Tratamento de valores padrão: A correspondência de padrões permite definir um valor padrão para tratar qualquer caso que não corresponda a nenhum padrão específico. Isso pode tornar o código mais limpo e evitar a necessidade de escrever uma cláusula else genérica.
- Verificação de padrões complexos: Em alguns casos, a verificação de padrões pode ser mais expressiva e concisa do que escrever uma condição mais complexa usando if, elif, else. A correspondência de padrões permite que você verifique padrões mais complexos, como combinações de valores, tipos de dados e estruturas de dados.
- Mais segurança na refatoração: A correspondência de padrões também pode ser útil ao fazer refatorações em seu código. Se você adicionar um novo padrão em uma estrutura match, o interpretador Python pode alertá-lo se houver algum lugar onde o novo padrão não esteja sendo verificado.
- Obviamente, você não precisa usar a correspondência de padrões em todos os casos. Para casos simples, onde há apenas uma ou duas condições para verificar, o uso de if, elif, else é provavelmente mais adequado e mais fácil de entender. No entanto, para casos mais complexos, a correspondência de padrões pode ser uma ferramenta útil para tornar o código mais legível e mais seguro.

## matching

Vamos começar comparando a correspondência de padrões com as estruturas condicionais IF-ELIF-ELSE:

    match num:
        case 1:
            print("um")
        case 2:
            print("dois")
        case _:
            print("outro número")

Observe que o caractere "underscore" (_) é usado como um padrão "coringa" para capturar qualquer valor que não corresponda a nenhum dos casos.

A correspondência de padrões também pode ser usada para fazer a correspondência de padrões em listas:

    lista = [1, _]
    match lista:
        case [1, _]:
            print("um e algum outro valor")

Nesse exemplo, o primeiro padrão corresponde à lista contendo os valores 1 e 2, o segundo padrão corresponde à lista contendo o valor 3 seguido de qualquer outro valor, e o último padrão corresponde a qualquer outra lista.

## Or SPM

O operador lógico OR pode ser usado para fazer a correspondência de padrões múltiplos:

    valor = "b"

    match valor:
        case "a" | "b":
            print("valor é 'a' ou 'b'")

## Case Guard (if no case)

Você também pode usar uma cláusula de "guarda" (guard clause) para adicionar uma condição extra à correspondência de padrões. É como um if dentro de um caso:

    valor = 7

    match valor:
        case x if x < 5:
            print("valor é menor que 5")
        case x if x > 10:
            print("valor é maior que 10")
        case _:
            print("valor é entre 5 e 10, inclusive")

Nesse exemplo, o primeiro padrão corresponde a valores menores que 5, o segundo padrão corresponde a valores maiores que 10 e o último padrão corresponde a valores entre 5 e 10, inclusive.
