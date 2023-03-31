# AWS

## Instalando MySQL no servidor

Comandos:
    sudo apt update
    sudo apt-get install mysql-server
    sudo mysql -u root -p 

    use mysql 
    update user set plugin='mysql_native_password' where user='root';
    flush privileges; 
    ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'root_password';
    exit

    sudo mysql_secure_installation

    sudo mysql -u root -p
    CREATE USER 'db_admin'@'localhost' IDENTIFIED BY 'admin_password';
    CREATE DATABASE db_name;
    GRANT ALL PRIVILEGES ON db_name.* TO 'db_admin'@'localhost';
    exit

## Configurando git

Comandos:

    git config --global user.name 'Seu nome'
    git config --global user.email 'seu_email@gmail.com'
    git config --global init.defaultBranch main

## Repositório bare

Comandos:

    mkdir -p ~/app_bare
    cd ~/app_bare
    git init --bare
    cd ~

## Repositório da aplicação

Comandos:

    mkdir -p ~/app_repo
    cd ~/app_repo
    git init
    git remote add origin ~/app_bare
    git add . && git commit -m 'Initial'
    cd ~

## Fazendo conexão SSH

Comandos no local computer:

    ssh-keygen
    cat ~/.ssh/id_rsa.pub

Copie a chave ssh mostrada

Comandos no server computer:

    nano ~/.ssh/authorized_keys

Adicione a chave copiada no local computer na última linha do arquivo, salve e feche
