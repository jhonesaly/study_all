# Shell Script

Comandos lógicos para script:

- read [options]
    - [-p] prompt: exibe a string prompt como uma mensagem antes de ler a entrada do usuário.
    - [-t] timeout: define um tempo limite timeout em segundos para a entrada do usuário.
    - [-n] nchars: lê somente os nchars primeiros caracteres da linha de entrada.
    - [-s] faz com que a entrada do usuário seja silenciosa, ou seja, os caracteres digitados não são exibidos na tela.
    - [-a] array: lê a entrada do usuário em um array em vez de uma variável.

você pode definir um valor padrão para a variável (ex: ans_a1) usando o operador ':-'. 

    read -n 1 -p "Deseja atualizar servidor? [y/n] " ans_a1
    ans_a1=${ans_a1:-y}


Se a variável ans_a1 estiver vazia, o valor padrão "y" será atribuído a ela. Caso contrário, o valor que o usuário digitou será atribuído a ans_a1. 

- if, else:
    
    if [ "$var" == "value" ]; then
        # comandos
    elif [ "$var" == "value" ]; then
        # comandos
    else
        # comandos
    fi

- while:

    while [ "$exit" != true ]; do
        
        if ...; then
            #
        elif ...; then
            #
            continue
        else
            exir = true
            break
        fi
    done

- for:

    for i in $var; do
        # comandos
    done

- len(var) = ((${#var[@]}))
    - O [@] é uma expansão de parâmetro que diz ao Bash para expandir cada elemento do array var como um item separado, em vez de expandir todo o array como uma única string.
    - O uso de $(()) é uma sintaxe de expressão aritmética do Bash, que permite realizar cálculos com números inteiros.
- range(x) = seq 0 $x

## Diferença entre "$ans_w1" e ${ans_w1}?

Ambas as formas de referenciar a variável ans_w1 são válidas no Bash. No entanto, o uso de aspas duplas ("$ans_w1") tem a vantagem de permitir a expansão de variáveis e caracteres especiais, enquanto ainda mantém a integridade da string.

Por exemplo, se ans_w1 contém um valor com espaços em branco, como "meu repositório", a expansão ${ans_w1} seria interpretada como duas palavras distintas ("meu" e "repositório"), enquanto "$ans_w1" seria interpretada como uma única string ("meu repositório"). Da mesma forma, se ans_w1 contém um caractere especial que precisa ser interpretado pelo Bash, como um asterisco (*), a expansão ${ans_w1} seria interpretada como uma lista de arquivos que correspondem ao padrão, enquanto "$ans_w1" seria interpretada como uma string contendo o próprio asterisco.

Em resumo, o uso de aspas duplas pode ajudar a evitar erros de interpretação de caracteres especiais e garantir que as variáveis sejam expandidas corretamente.


## Funções

Para declarar uma função em shell script, faça como no exemplo:

    function welcome() {
        echo "Bem-vindo ao Ubuntu Server!"
    }

Para usá-la direto no prompt:

    $ source minhas_funcoes.sh
    $ welcome
    Bem-vindo ao Ubuntu Server!

Para usá-la em outro script:

    #!/bin/bash

    # Importa o arquivo com as funções
    . minhas_funcoes.sh

    # Chama a função welcome
    welcome
    
# Baixar e descompactar

renomeação do arquivo durante o download e descompactação, você pode adicionar o nome desejado ao usar o comando wget com a opção -O, e especificar um nome diferente durante a descompactação usando a opção -d do comando unzip. Por exemplo:

    read -p "coloque o endereço do repositório para fazer o download: " ans_w1
    wget "$ans_w1" -O my_app.zip
    unzip my_app.zip -d my_app_folder


# Scipr para atualizar servidor sem usuário

    export DEBIAN_FRONTEND=noninteractive
    apt-get update -y
    apt-get upgrade -y -qq
    systemctl daemon-reexec


# Testes

é possível e recomendado escrever testes para a infraestrutura como código (IaC) escrita em shell script. O objetivo desses testes é garantir que as mudanças feitas na infraestrutura, representadas pelo código, produzam o resultado esperado.

Existem várias ferramentas disponíveis para escrever testes para infraestrutura como código em shell script, como o Bash Automated Testing System (BATS), que é uma estrutura de teste de shell script desenvolvida especificamente para IaC. Ele permite escrever testes para a infraestrutura, verificando se os comandos de shell script funcionam conforme o esperado. O BATS também suporta a execução de testes em paralelo, tornando os testes mais eficientes e rápidos.

Outra opção é usar o shellcheck, que é uma ferramenta de análise estática para scripts de shell script. Ele verifica se o código segue as boas práticas de codificação em shell script e detecta possíveis erros e problemas de segurança.

Os testes para IaC em shell script podem verificar, por exemplo, se um servidor web está respondendo corretamente, se um banco de dados está acessível, se um arquivo de configuração foi criado corretamente, entre outros casos de uso. Os testes podem ser executados automaticamente em um ambiente de CI/CD (Integração Contínua / Entrega Contínua) sempre que houver uma nova alteração no código, garantindo assim a qualidade e consistência da infraestrutura como código.