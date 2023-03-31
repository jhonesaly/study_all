# AWS

## Instalando MySQL no servidor

Comandos no server:

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

Comandos no server:

    git config --global user.name 'Seu nome'
    git config --global user.email 'seu_email@gmail.com'
    git config --global init.defaultBranch main

## Repositório bare

Comandos no server:

    mkdir -p ~/app_bare
    cd ~/app_bare
    git init --bare
    cd ~

## Repositório da aplicação

Comandos no server:

    mkdir -p ~/app_repo
    cd ~/app_repo
    git init
    git remote add origin ~/app_bare
    git add . && git commit -m 'Initial'
    cd ~

## Fazendo conexão SSH

Comandos no local:

    ssh-keygen
    cat ~/.ssh/id_rsa.pub

Copie a chave ssh mostrada

Comandos no server:

    nano ~/.ssh/authorized_keys

Adicione a chave copiada no local computer na última linha do arquivo, salve e feche

## Copie o app para o server

Comandos no local:

    git remote add app_bare ubuntu@<aws_server_ip>:~/app_bare
    git push app_bare <branch> (master ou main)

Comandos no server:

    cd app_repo
    git pull origin <branch> (master ou main)
