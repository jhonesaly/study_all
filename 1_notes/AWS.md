# AWS

## Instalando MySQL no servidor

Comandos:
    sudo apt update
    sudo apt-get install mysql-server
    sudo mysql -u root -p 

    use mysql 
    update user set plugin='mysql_native_password' where user='root';
    flush privileges; 
    ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';
    exit()

    sudo mysql_secure_installation
