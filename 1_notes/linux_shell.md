# Shell Script

Comandos lógicos para script:

- read [options]
    - [-p] prompt: exibe a string prompt como uma mensagem antes de ler a entrada do usuário.
    - [-t] timeout: define um tempo limite timeout em segundos para a entrada do usuário.
    - [-n] nchars: lê somente os nchars primeiros caracteres da linha de entrada.
    - [-s] faz com que a entrada do usuário seja silenciosa, ou seja, os caracteres digitados não são exibidos na tela.
    - [-a] array: lê a entrada do usuário em um array em vez de uma variável.

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

# Testes

é possível e recomendado escrever testes para a infraestrutura como código (IaC) escrita em shell script. O objetivo desses testes é garantir que as mudanças feitas na infraestrutura, representadas pelo código, produzam o resultado esperado.

Existem várias ferramentas disponíveis para escrever testes para infraestrutura como código em shell script, como o Bash Automated Testing System (BATS), que é uma estrutura de teste de shell script desenvolvida especificamente para IaC. Ele permite escrever testes para a infraestrutura, verificando se os comandos de shell script funcionam conforme o esperado. O BATS também suporta a execução de testes em paralelo, tornando os testes mais eficientes e rápidos.

Outra opção é usar o shellcheck, que é uma ferramenta de análise estática para scripts de shell script. Ele verifica se o código segue as boas práticas de codificação em shell script e detecta possíveis erros e problemas de segurança.

Os testes para IaC em shell script podem verificar, por exemplo, se um servidor web está respondendo corretamente, se um banco de dados está acessível, se um arquivo de configuração foi criado corretamente, entre outros casos de uso. Os testes podem ser executados automaticamente em um ambiente de CI/CD (Integração Contínua / Entrega Contínua) sempre que houver uma nova alteração no código, garantindo assim a qualidade e consistência da infraestrutura como código.