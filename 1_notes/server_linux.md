# Server linux na própria máquina (Virtual Machine)

configure a virtual machine criada para a conexão estar em modo brige, como na imagem:

![configurações de rede da VM](/images/virtualmachine1.png)

Se estiver usando windows, é necessário baixar o putty em <https://www.putty.org/>. Vá em downloads e, para facilitar, baixe o .exe (putty.exe) para sua versão adequada, provavelmente a primeira opção (64-bit x86) e não o instalador .msi.

Abra a sua virtual machine e coloque o comando 

    > ip a

no endereço enp0s3, anote o ip informado em inet

Execute o putty.exe e no campo IP adress, coloque o ip informado, como na imagem:

![putty session](/images/puttysession.png)

# Server linux na AWS

Primeiro, crie uma conta na AWS <https://aws.amazon.com/pt/> (é necessário registrar cartão de crédito, ainda que só use serviços gratuitos)

No menu "esecutar instância", clique em "executar instância"

crie um nome para o servidor e selecione o tipo de servidor e suas especificações (aqui, use uma qualificada para nível gratuito) conforme a imagem:

![criando server na aws](/images/aws1.png)

No menu par de chaves, clique em "criar nova chave", dê um nome para a mesma. Se for usar um linux para conectar ao servidor, baixe o .pem para usar o openssh. Se for usar widowns, baixe o .ppk para usar o putty. Ao clicar em "criar par de chaves", a chave sera baixada automaticamente.

Se a chave que você baixou for do tipo .pem, mas quer usar no windows (no putty), é necessário fazer o download, no mesmo site, do puttygen.exe para a versão adequada e convertê-la.

deixe a caixa "permitir tráfego SSH de " habilitada e permite "qualquer lugar"

Para acessar via putty, configure a conexão adicionando a chave conforme a imagem:

![putty session conection](/images/puttysession2.png)

Não se esqueça de, quando terminar a atividade, encerrar a instância na AWS, pois pode ser cobrado alguma tarifa por excesso de uso.


# Servidor de arquivos

Primeiramente, monte um drive separado do sistema operacional para não sobrecarregá-lo em caso de muitos acessos. Para facilitar, todos os comandos serão dados como root.

    > fdisk /dev/sdb
    > mkfs.ext4 /dev/sdb
    > mkdir disk2
    > mount /dev/sdb /disk2
    > nano /etc/fstab

add na última linha: 

/dev/sdb /disk2 ext4 defaults 0 0

    > cd /
    > cd disk2
    > mkdir publica
    > chmod 777 publica/
    > apt install samba -y
    > nano /etc/samba/smb.conf

add na última linha:

[publica]

path = /disk2/publica
writable = yes
guest ok = yes
guest only = yes

    > systemctl restart smbd
    > systemctl status smbd
    > systemctl enable smbd

Com isso, você deve ser capaz de acessar a pasta /publica por meio do seu explorador de arquivos. Para tal, use o comando 'ip a' (ex: 192.168.0.0) para descobrir o ip da máquina e então coloque no endereço:

    \\192.168.0.0\publica

# Montando Servidor web

Instalando apache

    > apt install apache2 -y
    > systemctl apache2

Nesse momento, se você colocar o ip da máquina com o apache instalado no endereço do seu navegador já verá a página do apache.

    > cd /var/www/html

Nesta path está o arquivo (index.html) que foi mostrado na página ao acessar o endereço do ip da máquina.

    > rm index.html
    > nano index.html

crie o que quiser para página inicial

Esse site já está disponível para qual quer dispositivo conectado na rede local.

para torná-lo disponível globalmente, você pode precisa de um ip público. Você pode conseguir isso por meio de uma instância na AWS.

Para habilitar o acesso na AWS, é necessário habilitar o firewall para permitir requisições HTTP. Isso é feito no menu:

    > Security Groups > Instância >  Edit inbound rules

Você pode fazer um site, por exemplo, em um ambiente controlado e depois colocá-lo dentro da pasta apache.

# Servidores de banco de dados

Aqui usaremos o MySQL, mas poderia ser outros serviços.

    > apt search mysql server (verifique qual a versão mais recente do MySQL server)
    > apt install mysql-server-8.0
    > mysql -u root -p (para acessar o banco de dados como root, necessário senha)

Principais comandos para o mysql

- SHOW DATABASES; - Mostrar todas as bases de dados
- USE nome_da_base_de_dados; - Selecionar uma base de dados específica
- SHOW TABLES; - Mostrar todas as tabelas em uma base de dados
- CREATE DATABASE nome_da_base_de_dados; - Criar uma nova base de dados
- DROP DATABASE nome_da_base_de_dados; - Excluir uma base de dados
- CREATE TABLE nome_da_tabela (coluna1 tipo_de_dado, coluna2 tipo_de_dado, ...); - Criar uma nova tabela
- DROP TABLE nome_da_tabela; - Excluir uma tabela
- INSERT INTO nome_da_tabela (coluna1, coluna2, ...) VALUES (valor1, valor2, ...); - Adicionar dados a uma tabela
- SELECT coluna1, coluna2, ... FROM nome_da_tabela; - Selecionar dados de uma tabela

Você pode importar um banco de dados MySQL existente usando o seguinte comando no terminal:

    mysql -u usuario -p nome_da_base_de_dados < nome_do_arquivo.sql

Onde:

- usuario é o nome de usuário com permissão de acesso à base de dados.
- nome_da_base_de_dados é o nome da base de dados para a qual você deseja importar os dados.
- nome_do_arquivo.sql é o nome do arquivo SQL que contém a estrutura e os dados do banco de dados que você deseja importar.
- Você será solicitado a inserir a senha do usuário MySQL antes de o comando ser executado. Uma vez que o comando tenha sido executado com sucesso, o banco de dados importado estará disponível para uso.

> Observação: certifique-se de que o banco de dados alvo esteja vazio antes de importar os dados. Caso contrário, os dados existentes serão sobrescritos.

O comando **DROP DATABASE nome_do_banco** exclui permanentemente uma base de dados existente do servidor MySQL. Após a execução desse comando, a base de dados e todos os dados nela contidos serão perdidos e não poderão ser recuperados. Já o comando **rm nome_do_banco.sql** exclui um arquivo do sistema operacional (no caso, um arquivo SQL que representa o backup de uma base de dados). Esse arquivo pode ser recuperado a partir de backups ou pode ser gerado novamente a partir da base de dados original.

O arquivo .sql é uma representação em formato de texto da estrutura e dos dados de uma base de dados MySQL. Ele contém instruções em linguagem SQL que, quando executadas, recriam a estrutura e os dados da base de dados. O banco de dados em si é armazenado em um servidor MySQL e pode ser acessado por meio de uma aplicação cliente (como o próprio terminal, por exemplo). O arquivo .sql é apenas um backup da base de dados, e não a base de dados propriamente dita.

Para sair do mysql:

    mysql> exit

