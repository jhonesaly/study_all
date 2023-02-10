# Definição

Infraestrutura como código (IaC) é o **gerenciamento** e provisionamento da infraestrutura por meio de **códigos**, em vez de processos manuais.

Com a IaC, são criados **arquivos de configuração** que incluem as especificações da sua infraestrutura, facilitando a edição e a distribuição de configurações. Ela também assegura o provisionamento do mesmo ambiente todas as vezes. 

Ao automatizar o provisionamento da infraestrutura com a IaC, os desenvolvedores não precisam provisionar e gerenciar manualmente servidores, sistemas operacionais, armazenamento e outros componentes de infraestrutura sempre que criam ou implantam uma aplicação.

# Requisitos

Diretórios:

- /publico
- /adm
- /ven
- /sec

Grupos (explicação):

- 1: GRP_ADM (administrativo)
- 2: GRP_VEN (vendas)
- 3: GRP_SEC (secretariado)

Usuários (grupo):

- carlos (1)
- maria (1)
- joao (1)
- debora (2)
- sebastiana (2)
- roberto (2)
- josefina (3)
- amanda (3)
- rogerio (3)

Operações:

- Excluir diretórios, arquivos, grupos e usuários criados anteriormente;
- Todo provisionamento deve ser feito em um arquivo do tipo Bash Script;
- O dono de todos os diretórios criados será o usuário root;
- Todos os usuários terão permissão total dentro do diretório publico;
- Os usuários de cada grupo terão permissão total dentro de seu respectivo diretório;
- Os usuários não poderão ter permissão de leitura, escrita e execução em diretórios de departamentos que eles não pertencem;
- Subir arquivo de script criado para a sua conta no GitHub.

# Explicando o script

REESCREVER!###########################################

O script "new_iac.sh" é um shell script que é utilizado para automatizar a criação de diretórios, grupos e usuários em um sistema operacional baseado em Unix.

Ele começa com a definição do arquivo de configuração, que deve estar na mesma pasta do script. O arquivo de configuração, chamado "config.txt", contém as informações sobre os diretórios, grupos e usuários a serem criados.

Depois ele lê o arquivo de configuração e armazena as informações em três variáveis: "directories", "groups" e "users". Em seguida, ele cria cada um dos diretórios especificados no arquivo de configuração usando o comando "mkdir".

Em seguida, o script cria os grupos especificados no arquivo de configuração usando o comando "groupadd". Ele usa um loop "for" para iterar sobre cada um dos grupos e criá-los individualmente.

Por fim, o script cria os usuários especificados no arquivo de configuração usando o comando "useradd". Antes de criar o usuário, ele usa o comando "id" para verificar se o grupo ao qual o usuário pertence já foi criado. Se o grupo não tiver sido criado, ele é criado primeiro. Em seguida, o usuário é criado e atribuído ao grupo especificado por seu número.

Este script é uma ferramenta útil para administradores de sistemas que precisam criar repetidamente diretórios, grupos e usuários em seus sistemas operacionais. Ao invés de executar manualmente cada um desses comandos, o script faz isso de forma automatizada e com base nas informações especificadas no arquivo de configuração.

# Rodando na sua máquina

Como root, vá para a raiz e crie uma pasta para receber os arquivos necessários

    > cd /
    > mkdir downloads
    > cd downloads

Faça o download dos arquivos necessários no GitHub:

REESCREVER!###########################################

    > wget https://raw.githubusercontent.com/jhonesaly/linux-study/master/project_iac/config.txt
    > wget https://raw.githubusercontent.com/jhonesaly/linux-study/master/project_iac/new_iac.sh

REESCREVER!###########################################

Atribua a possibilidade de ler, editar e executar os arquivos na pasta project_iac:

    > chmod -R 775 project_iac

Entre na pasta do projeto e abra o arquivo config.txt para definir o que será criado por meio do comando no prompt:

    > nano config.txt

Com tudo configurado, execute: 

    > ./new_iac.sh