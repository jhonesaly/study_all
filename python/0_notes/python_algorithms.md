# Algoritmos

## Gerando números aleatórios em Python

Você pode gerar números aleatórios usando a biblioteca "random" do Python.

    import random

Número inteiro aleatório entre uma faixa específica:

    random.randint(a, b)

> Onde `a` é o limite inferior e `b` é o limite superior da faixa de números.

número flutuante aleatório entre 0 e 1:

    random.random()

Escolhendo aleatoriamente um item de uma lista:

    random.choice(lista)

> onde lista é a lista de itens de onde você deseja escolher.

Para gerar listas de números aleatórios, você pode usar:

    random_list = random.sample(range(list_range), list_size)

> range(list_range) é a fonte de dados para os números aleatórios. Nesse caso, é um intervalo de números inteiros de 0 ao valor em list-range.
> list_size é o número de elementos aleatórios que queremos na lista.


## Ordenando lista em python

Usando o método sorted() ou o método sort() dos objetos lista. Aqui estão 

    lista_ordenada = sorted(lista)

    ou

    lista.sort()

> onde lista é a lista que você deseja ordenar e lista_ordenada é a lista ordenada.
> O sorted() retorna uma nova lista ordenada, enquanto o sort() ordena a lista original in-place.

Por padrão, ambos os métodos ordenam a lista em ordem crescente. Se você deseja ordenar em ordem decrescente, pode adicionar o argumento reverse=True:

    lista_ordenada = sorted(lista, reverse=True)

    ou

    lista.sort(reverse=True)

## Fazendo variáveis em funções serem globais

Para tornar mais de uma variável global, basta usar a palavra-chave "global" antes de cada variável. Por exemplo:

    x = 10
    y = 20

    def foo():
    global x, y
    x += 1
    y += 1

    foo()
    print(x)  # Output: 11

## Separando String maior

Você pode separar a string em uma lista de caracteres usando o método "list" e a função "list comprehensions". Aqui está um exemplo:

    string_gigante = "Minha string gigante"
    lista_de_letras = [letra for letra in string_gigante]

Agora, a variável "lista_de_letras" contém uma lista de caracteres como elementos, separados da string original.

# Modularização

Para fazer a modularização de um código em Python, você pode dividi-lo em módulos (arquivos .py) e importá-los em seu código principal. Cada módulo pode conter funções, classes ou variáveis úteis para o seu programa. Para importar um módulo, basta usar a instrução:

    import nome_do_modulo

Além disso, é possível importar apenas uma função ou classe específica de um módulo usando a sintaxe:

    from nome_do_modulo import nome_da_funcao

o Python permite que você importe módulos de qualquer lugar, desde que o caminho para o arquivo do módulo esteja incluído na lista de diretórios de pesquisa do Python (sys.path). Por padrão, a lista inclui o diretório atual e os diretórios incluídos na variável de ambiente PYTHONPATH.

Se você criar uma pasta no diretório atual para centralizar os módulos, o Python achará os arquivos automaticamente, sem a necessidade de adicionar a pasta ao Pythonpath. Por exemplo, se você criou uma pasta chamada "modulos" no diretório atual, e dentro dessa pasta tem um arquivo chamado "nome_do_modulo.py", você pode importar esse módulo usando a seguinte sintaxe: 

    import modulos.nome_do_modulo

Se o módulo que você deseja importar estiver em um diretório diferente, você pode adicioná-lo à lista de diretórios de pesquisa usando a instrução

    .> sys.path.append(caminho_para_diretorio)
    
Para importar todas as funções de um módulo sem precisar colocar o nome do módulo na frente, você pode usar a seguinte sintaxe: 

    from nome_do_modulo import * 

Isso fará com que todas as funções, classes e variáveis definidas no módulo sejam importadas para o seu código, e você poderá usá-las diretamente, sem precisar incluir o nome do módulo na frente.

Se você deseja usar um apelido para o módulo importado, pode fazer isso adicionando "as apelido" ao final da instrução de importação. Por exemplo:

    import nome_do_modulo as apelido