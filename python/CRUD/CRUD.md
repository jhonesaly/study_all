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




