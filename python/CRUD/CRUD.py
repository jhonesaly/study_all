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
conexao.commit()

# Read

comando = f'SELECT * FROM produtos;'

cursor.execute(comando)
resultado = cursor.fetchall()
print(resultado)

# Update

prod_name = "todynho"
prod_new_val = 6.0

comando = f'UPDATE produtos SET Value = {prod_new_val} WHERE Name = "{prod_name}"'

cursor.execute(comando)
conexao.commit()

cursor.close()
conexao.close()