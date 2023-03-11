# CRUD

CRUD é um acrônimo utilizado em tecnologia da informação que representa as quatro operações básicas em bancos de dados relacionais:

- Create (Criar): operação que permite criar um novo registro no banco de dados.
- Read (Ler): operação que permite ler ou visualizar um registro existente no banco de dados.
- Update (Atualizar): operação que permite modificar ou atualizar um registro existente no banco de dados.
- Delete (Excluir): operação que permite excluir um registro existente no banco de dados.

Essas quatro operações são consideradas fundamentais para a gestão de dados em um sistema que utiliza um banco de dados relacional. Ao implementar um sistema com as operações CRUD, é possível criar, ler, atualizar e excluir dados de forma estruturada e segura.

## MySQL

Para realizar o procedimento em python, é necessário já ter um banco de dados pronto para testes. Para tal, será utilizado o MySQL que possui uma ótima compatibilidade com a linguagem e o framework.

Será necessária a instalação do mysql server para disponibilizar o banco de dados. Depois disso ele pode ser acessado via mysql workbench ou qualquer outro SGBD (como o DBeaver).

Para tal, foi montando o mysql server no Windows, adicionando a pasta /bin do server ao path e rodando o comando 'mysqld'.

Depois, foi criado, usando o mysql workbench, um banco de dados chamado de test, com a tabela produtos que contém o ID (PK), nome e valores. Com isso, agora podemos seguir para o script em python.

    CREATE TABLE `test`.`produtos` (
    `ID` INT NOT NULL AUTO_INCREMENT,
    `Name` VARCHAR(45) NOT NULL,
    `Value` DECIMAL NOT NULL,
    PRIMARY KEY (`ID`));

## Python

Para realizar a conexão, é necessário, primeiramente instalar a biblioteca de conexão:

    pip install mysql-connector

 E então a escrever a seguinte estrutura básica para conexão:

    import mysql.connector

    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='1234',
        database='test',
    )

host é o endereço da conexão, user é o usuário, password é a senha para acesso e database é o nome do banco que será conectado.

Para realizar os comandos, é necessário criar um cursor, que será encerrado no final juntamente com a conexão, como em:

    cursor = conexao.cursor()

    # onde vai entrar o CRUD

    cursor.close()
    conexao.close()

Estrutura básica de um CRUD:

    comando = ''
    cursor.execute(comando)
    conexao.commit() #edita o banco de dados
    resultado = cursor.fetchall() #ler o banco de dados

O comando indica o que será feito, a próxima linha executa o comando. Se o comando alterar o banco de dados, é necessário o commit. Se o comando é para pegar alguma informação do banco de dados, precisa ser guardado em 'resultado'.

Para fazer o Create, o modelo é:

    prod_name = "todynho"
    prod_val = 3.3

    comando = f'INSERT INTO produtos (Name, Value) VALUES ("{prod_name}", {prod_val})'

    cursor.execute(comando)
    conexao.commit()

Para fazer o Read, o modelo é:

    comando = f'SELECT * FROM produtos;'

    cursor.execute(comando)
    resultado = cursor.fetchall()
    print(resultado)

Para fazer o Update, o modelo é:

    prod_name = "todynho"
    prod_new_val = 6.0

    comando = f'UPDATE produtos SET Value = {prod_new_val} WHERE Name = "{prod_name}"'

    cursor.execute(comando)
    conexao.commit()

