import mysql.connector

conexao = mysql.connector.connect(
    user='root',
    password='1234',
    database='test',
)

cursor = conexao.cursor()

# CRUD

cursor.close()
conexao.close()