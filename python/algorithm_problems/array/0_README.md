# Array

## reversal

Este código define uma função chamada "reversal" que recebe uma lista e um número "search" como argumentos. A função reverte os "search" primeiros elementos da lista e retorna a lista modificada.

A primeira linha da função cria uma nova lista "list_reversal" com tamanho "search", preenchida com zeros. Em seguida, um loop for é iniciado para iterar "search" vezes. A cada iteração, o último elemento da lista original é removido com o método "pop" e armazenado em "aux_1". A variável "aux_2" é criada como "search - i - 1" para mapear o índice apropriado em "list_reversal" para o valor de "aux_1". O valor de "aux_1" é então adicionado a "list_reversal" na posição "aux_2".

Finalmente, a lista original é anexada à lista "list_reversal" e a lista completa é retornada como a saída da função. No exemplo dado, a função reverte os dois primeiros elementos da lista [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] e retorna a lista modificada [2, 1, 3, 4, 5, 6, 7, 8, 9, 10].

## find_three

O código find_three define uma função que recebe uma lista de números como argumento e encontra os três maiores valores únicos presentes na lista. A função começa criando uma lista de três zeros (a variável max_three) que servirá para manter o controle dos maiores valores encontrados até o momento. Em seguida, a função itera sobre a lista de entrada e para cada elemento, verifica se é maior que o menor dos valores em max_three. Se for, então este elemento é adicionado na posição do menor valor em max_three. Ao final, a lista max_three é convertida em um conjunto para remover quaisquer valores duplicados, e esse conjunto é retornado como resultado.

No bloco if __name__ == '__main__', é definida uma lista de entrada problem_input com cinco números. Essa lista é passada para a função find_three, cujo resultado é armazenado na variável problem_output. Finalmente, o resultado é exibido na tela por meio do comando print.

### test_find_three

O código apresentado é um teste unitário para a função find_three que foi importada do módulo find_three. Ele define duas funções de teste: test_find_three_equal e test_array_find_three_notequal. O primeiro teste verifica se a saída da função find_three com o test_input é igual a test_answer. O segundo teste verifica se a saída da função find_three com o mesmo test_input é diferente de test_not_answer. O bloco if __name__ == '__main__': permite que o arquivo possa ser executado como um script e chama a função main() do módulo unittest para executar os testes definidos no arquivo.

## reorder

Esta função recebe duas listas de inteiros do mesmo tamanho, "list_val" e "list_index", e reorganiza os elementos em "list_val" de acordo com a ordem definida em "list_index".

O valor em cada posição de "list_index" indica a posição que o elemento correspondente na lista "list_val" deve ser movido.

A função retorna duas listas reorganizadas, "list_val_ordered" e "list_index_ordered". Se as listas de entrada tiverem comprimentos diferentes, a função imprime uma mensagem de erro e retorna duas listas vazias.

Para testar a função, dois exemplos de entrada foram fornecidos no bloco de código principal. A primeira lista, "input_1", contém os valores originais e a segunda lista, "input_2", contém os índices que definem a nova ordem. A função é então chamada com essas duas listas como argumentos e as duas listas reorganizadas são impressas.

### test_reorder

Este é um conjunto de testes unitários para o algoritmo reorder, que espera que o algoritmo reordene elementos em uma lista de acordo com outra lista de índices.

O teste test_reorder_equal verifica se o resultado do algoritmo é igual ao esperado para as entradas test_input_1 e test_input_2, e isso é feito usando as variáveis de resposta test_answer_1 e test_answer_2.

O teste test_reorder_notequal verifica se o resultado do algoritmo é diferente do valor test_not_answer_1 e test_not_answer_2 para as entradas test_input_1 e test_input_2.

O teste test_reorder_same_length verifica se o comprimento da lista test_input_1 é igual ao comprimento da lista test_input_1, que deve ser verdadeiro.

O teste test_reorder_not_same_length verifica se o comprimento da lista test_input_1 é diferente do comprimento da lista test_input_3, que deve ser verdadeiro.

Todos os testes são executados usando a biblioteca de teste unittest do Python.

## positive_negative

O código é uma função em Python chamada "positive_negative" que recebe uma lista de números como entrada. A função tem como objetivo reorganizar a lista de forma que os números positivos ocorram em posições pares (0, 2, 4, ...) e os números negativos ocorram em posições ímpares (1, 3, 5, ...). O código é projetado para funcionar in-place, o que significa que a lista original é modificada e retornada pela função.

O código começa criando duas listas vazias, "num_pos" e "num_neg", para armazenar os números positivos e negativos da lista de entrada, respectivamente. Ele então percorre a lista de entrada e adiciona cada número à lista correspondente com base em se é positivo ou negativo.

Depois disso, o código inverte as duas listas "num_pos" e "num_neg", para que possamos começar a adicioná-las à lista ordenada começando pelo final.

Em seguida, a lista "list_ordered" é criada como uma lista vazia que será preenchida com os números reorganizados.

Depois disso, o código verifica se as listas "num_pos" e "num_neg" têm o mesmo comprimento. Se for esse o caso, ele adiciona números alternados das duas listas "num_pos" e "num_neg" à lista ordenada.

Se as listas tiverem comprimentos diferentes, o código cria um loop que adiciona números alternados das duas listas "num_pos" e "num_neg" à lista ordenada apenas até que uma das listas acabe. Em seguida, ele adiciona os números restantes da lista mais longa à lista ordenada.

Finalmente, a função retorna a lista ordenada.

O código também tem um bloco "if name == "main":" que define uma lista de entrada "input" e chama a função "positive_negative" com essa entrada. Ele compara o resultado retornado pela função com uma lista de resposta esperada "answer" e define uma variável booleana "test" como True se os dois forem iguais e False caso contrário. Ele então imprime a lista ordenada resultante e o valor booleano de "test".

No geral, o código é bem estruturado e cumpre o objetivo de reorganizar a lista de entrada de acordo com os requisitos especificados.

### test_positive_negative

O script de teste tem como objetivo testar as funções definidas no script "positive_negative.py". Ele utiliza a biblioteca "unittest" do Python para definir um conjunto de testes para as funções.

A classe "TestPositiveNegative" é uma subclasse de "unittest.TestCase" e define os métodos de teste "test_positive_negative_equal", "test_more_positive" e "test_more_negative". Cada um desses métodos testa um cenário diferente de entrada para a função "positive_negative", e utiliza o método "self.assertEqual" para verificar se a saída da função é igual à resposta esperada.

Dentro da condição "if name == 'main':" são definidos os cenários de teste para as entradas e saídas esperadas em cada método de teste. Em seguida, é chamado o método "unittest.main()", que executa todos os testes definidos na classe "TestPositiveNegative".

Em resumo, o script de teste executa um conjunto de testes para verificar se a função "positive_negative" está funcionando corretamente para diferentes cenários de entrada.
