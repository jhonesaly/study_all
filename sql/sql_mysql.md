# MySQL

## Preparando ambiente

Para gerenciar o banco de dados, foi baixado o DBeaver pelo link: <https://dbeaver.io/download/>

Para facilitar, o MySQL será rodado em um container criado a partir da imagem do MySQL no DockerHub. Para entender melhor essa terminologia, confira o arquivo "notes_docker.md" na raiz. Para conferir a imagem do MySQL no DockerHub, confira o link: <https://hub.docker.com/_/mysql>

-------
## Criando o Banco de Dados

### Criando Container e Banco de Dados

Comando para puxar do Docker Hub a imagem do MySQL

    docker pull mysql:tag


Comando para criar o container servidor do MySQL:

    docker 
        run --name container-name 
        -p xxxx:xxxx 
        -e MYSQL_ROOT_PASSWORD=my-secret-pw 
        -v /path/to/data:/var/lib/mysql
        -d mysql
    
    docker exec -it container-name mysql -uroot -p
    
comando para executar o container (MySQL, no caso):

    docker exec -it container-name mysql -uroot -p

Comando para criar data base MySQL no conteiner:

    mysql> CREATE DATABASE db_name;    


Comando para sair do container:

    mysql> quit

Variáveis:

- container-name = containertest1
- xxxx:xxxx = 3306:3306
- MYSQL_ROOT_PASSWORD = test1
- tag = latest
- /path/to/data = \volumes (pasta onde vai salvar os dados)
- db_name = mysqltest1

----------
### vinculando container ao DBeaver e criando primeira tabela:

- Clique em "+" no MySQL connections
- De um nome à conexão em connection name (docker containertest1)
- defina a porta (deve se a porta do container)
- forneça a senha

clique com o botão direito sobre o database desejado e o torne o padrão para poder criar uma tabela nele.


Criando tabela e definindo chave primária:

    CREATE TABLE mysqltest1.Pessoas (
        ID INT auto_increment NOT NULL,
        Nome varchar(100) NOT NULL,
        Nascimento DATE NOT NULL,
        Peso FLOAT NULL,
        CONSTRAINT Pessoas_PK PRIMARY KEY (ID)
        )
    ENGINE=InnoDB
    DEFAULT CHARSET=utf8mb4
    COLLATE=utf8mb4_0900_ai_ci;

Para rodar o script em SQL basta clicar "ctrl + enter"

Para adicionar novas colunas à tebela:

    ALTER TABLE mysqltest1.Pessoas ADD Altura FLOAT NULL;

------
## Adicionando dados

SQL para adicionar dados

    INSERT INTO Pessoas (Nome, Nascimento, Peso, Altura) VALUES ('Aba', '2000-01-01', 80.5, 1.75);

> ID não é necessário porque isso já foi configurado para ser feito automaticmanete
> Pese e Altura eram dados opcionais

SQL para adicionar dados aleatórios

    INSERT INTO Pessoas (Nome, Nascimento) VALUES ( 
        TO_BASE64(RANDOM_BYTES(6)), 
        DATE_ADD(DATE(NOW()), INTERVAL FLOOR(RAND()*365) DAY)
        );

--------
## Filtrando Dados

SQL para selecionar todos os dados da tabela

    SELECT * FROM Pessoas

SQL para selecionar dados específicos da tabela

    SELECT nome, nascimento FROM Pessoas

> SQL não é capital sensitive

-------
## Alterando Dados

SQL para alterar determinado dado:

    UPDATE Pessoas SET nome = 'Felipe' WHERE ID = 5;

> **CUIDADO!** Se não colocar "WHERE", todos os dados da tabela seriam alterados para 'Felipe'.

-------
## Deletando Dados

SQL para deletar dados:

    DELETE * FROM Pessoas Where ID = 5;

> **CUIDADE!** O comando delete não pode ser desfeito!
> Para gatantir que está deletando o dado certo, é uma boa prática usar o SELECT antes do DELETE para conferir o dado
> Deletar determinado dado não muda o ID dos demais valores por serem chaves primárias, portanto irrepetíveis.

--------
## Ordenando Dados

SQL para ordenar dados:

    SELECT * FROM Pessoas ORDER BY Nome;
    SELECT * FROM Pessoas ORDER BY Nome DESC;
    SELECT * FROM Pessoas ORDER BY Nome DESC LIMIT 10;

- ASC: crescente
- DESC: decrescente
- LIMIT N: Retorna só até N

------
## Agrupamento de dados

SQL para agrupar dados:

    SELECT SUBSTRING(Nome, 1, 1) as inicial, COUNT(*) as quantidade
    FROM Pessoas
    GROUP BY inicial;

Explicando:
inicial = SUBSTRING(Nome,1,1) = primeira letra do Nome
quantidade = contagem de vezes que determinada inicial apareceu
