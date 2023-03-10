# Structural Pattern Matching

Structural Pattern Matching (SPM) em Python é uma funcionalidade introduzida na versão 3.10 que permite a correspondência de padrões em valores de dados complexos, como tuplas, listas, dicionários, entre outros.

A correspondência de padrões é uma técnica de programação que permite selecionar o código a ser executado com base no valor de entrada. Em vez de usar vários if-else ou switch-case aninhados, o structural pattern matching permite que você combine diferentes padrões em uma única expressão.

## if-else

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
