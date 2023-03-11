import mysql.connector

conexao = mysql.connector.connect(
    user='root',
    password='1234',
    database='test',
)

cursor = conexao.cursor()

# CRUD

# comando = ''
# cursor.execute(comando)
# conexao.commit() #edita o banco de dados
# resultado = cursor.fetchall() #ler o banco de dados

# Create

prod_name = "todynho"
prod_val = 3.3

comando = f'INSERT INTO produtos (Name, Value) VALUES ("{prod_name}", {prod_val})'

cursor.execute(comando)
conexao.commit() #edita o banco de dados

cursor.close()
conexao.close()