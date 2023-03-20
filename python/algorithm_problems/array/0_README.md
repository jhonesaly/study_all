# Array

## find_three

O código find_three define uma função que recebe uma lista de números como argumento e encontra os três maiores valores únicos presentes na lista. A função começa criando uma lista de três zeros (a variável max_three) que servirá para manter o controle dos maiores valores encontrados até o momento. Em seguida, a função itera sobre a lista de entrada e para cada elemento, verifica se é maior que o menor dos valores em max_three. Se for, então este elemento é adicionado na posição do menor valor em max_three. Ao final, a lista max_three é convertida em um conjunto para remover quaisquer valores duplicados, e esse conjunto é retornado como resultado.

No bloco if __name__ == '__main__', é definida uma lista de entrada problem_input com cinco números. Essa lista é passada para a função find_three, cujo resultado é armazenado na variável problem_output. Finalmente, o resultado é exibido na tela por meio do comando print.

## positive_negative

Esta função recebe duas listas de inteiros do mesmo tamanho, "list_val" e "list_index", e reorganiza os elementos em "list_val" de acordo com a ordem definida em "list_index".

O valor em cada posição de "list_index" indica a posição que o elemento correspondente na lista "list_val" deve ser movido.

A função retorna duas listas reorganizadas, "list_val_ordered" e "list_index_ordered". Se as listas de entrada tiverem comprimentos diferentes, a função imprime uma mensagem de erro e retorna duas listas vazias.

Para testar a função, dois exemplos de entrada foram fornecidos no bloco de código principal. A primeira lista, "input_1", contém os valores originais e a segunda lista, "input_2", contém os índices que definem a nova ordem. A função é então chamada com essas duas listas como argumentos e as duas listas reorganizadas são impressas.

### test_positive_negative

Este é um conjunto de testes unitários para o algoritmo positive_negative, que espera que o algoritmo reordene elementos em uma lista de acordo com outra lista de índices.

O teste test_positive_negative_equal verifica se o resultado do algoritmo é igual ao esperado para as entradas test_input_1 e test_input_2, e isso é feito usando as variáveis de resposta test_answer_1 e test_answer_2.

O teste test_positive_negative_notequal verifica se o resultado do algoritmo é diferente do valor test_not_answer_1 e test_not_answer_2 para as entradas test_input_1 e test_input_2.

O teste test_positive_negative_same_length verifica se o comprimento da lista test_input_1 é igual ao comprimento da lista test_input_1, que deve ser verdadeiro.

O teste test_positive_negative_not_same_length verifica se o comprimento da lista test_input_1 é diferente do comprimento da lista test_input_3, que deve ser verdadeiro.

Todos os testes são executados usando a biblioteca de teste unittest do Python.
