# Código Limpo em Python

Aqui estão algumas dicas gerais para manter um código limpo:

- Utilize nomes descritivos para variáveis e funções.
- Mantenha seu código formatado de forma consistente.
- Escreva comentários para explicar o que seu código está fazendo.
- Evite código duplicado e refatore-o quando necessário.
- Mantenha suas funções curtas e fáceis de ler.
- Teste seu código rigorosamente.
- Documente sua API e código interno.
- Mantenha uma boa estrutura de arquivos e diretórios.
- Utilize boas práticas de versionamento de código (ex: Git).
- Continuamente melhore e limpe seu código ao longo do tempo.

A PEP 8 (Python Enhancement Proposal 8) é uma guia de estilo de código para o Python. Ela define diretrizes e convenções para escrever código Python de maneira consistente e legível. A PEP 8 abrange questões como formatação de código, nomes de variáveis, funções, classes, espaçamento, comentários, entre outros. Seguir a PEP 8 ajuda a garantir que o código Python seja escrito de maneira consistente e legível para todos os programadores envolvidos no projeto. Embora não seja obrigatório seguir a PEP 8, é amplamente seguida na comunidade Python como uma boa prática.

Regras gerais:

- Nomes de variáveis devem ser descritivos e significativos.
- Não comece o nome de uma variável com um número ou um caractere especial.
- Não utilize palavras reservadas do Python para nomes de variáveis.
- Utilize abreviações com moderação, evite nomes de variáveis com mais de trinta caracteres.

Recomenda-se o uso de nomes em "lowercase" (letras minúsculas) com palavras separadas por "underline" (travessão "_"), conhecido como "snake_case".

Para classes de objetos e seus métodos, a convenção é usar o "CamelCase", ou seja, começar com a primeira letra de cada palavra em maiúsculo.

A primeira letra de uma palavra composta por CamelCase pode ou não ser capitalizada, não há consenso sobre a maneira certa de sua utilização. Existem duas formas de classificá-la: a primeira é conhecida como UpperCamelCase (de letra inicial maiúscula, também conhecida como PascalCase) e a segunda lowerCamelCase (de letra inicial minúscula).

Ex:

    class Produto:
        def __init__(self, nome, preco):
            self.nome = nome
            self.preco = preco

        def calcularDesconto(self, porcentagem):
            desconto = self.preco * (porcentagem / 100)
            return self.preco - desconto
    
    produto = Produto("Televisão", 1999.99)
    preco_final = produto.calcularDesconto(10)

    def calcular_preco_final(produto, percentual_desconto):
        preco_final = produto.calcularDesconto(percentual_desconto)
        return preco_final

Se o nome de uma variável ficar grande demais, isso pode ser um indicativo de que a variável está sendo usada para armazenar **informações demais** ou que o nome não é descritivo o suficiente. Nesse caso, uma boa prática é refatorar o código para usar **mais de uma variável**, cada uma com um nome mais descritivo, ao invés de usar uma única variável com um nome longo.

Em geral, o uso de várias variáveis em vez de uma única variável grande não afeta significativamente a velocidade de um programa. A maior preocupação é a legibilidade e a manutenibilidade do código. Além disso, o interpretador ou compilador moderno são projetados para lidar com muitas variáveis sem prejudicar significativamente o desempenho.

onvenções que determinam o acesso e o escopo de variáveis. Aqui estão algumas delas:

'_var': uma variável com um único sublinhado antes do nome é considerada como uma convenção para indicar que a variável é privada e deve ser tratada como tal. No entanto, ela ainda pode ser acessada por outros objetos, já que não há restrições fortes no Python quanto a variáveis privadas.

'__var': uma variável com dois sublinhados antes do nome é considerada uma "name mangling" (ou ofuscamento de nome), o que significa que seu nome será alterado de forma a torná-lo mais difícil de ser acessado de fora da classe. Por exemplo, se você tiver uma variável __var, ela será renomeada para _classe__var internamente.

'__var__' (dunder line = double underline): uma variável com dois sublinhados antes e depois do nome é reservada para variáveis com um significado especial, como, por exemplo, para representar métodos especiais (como __init__ e __str__). Não é recomendável usar esse padrão para suas próprias variáveis.

Em projetos usando o Django, a convenção é nomear arquivos, pastas e códigos de maneira que sejam fáceis de serem localizados e entendidos em com snake_case.