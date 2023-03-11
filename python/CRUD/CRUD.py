import mysql.connector

conexao = mysql.connector(
    host='localhost',
    user='root',
    password='1234',
    database='test',
)

cursor = conexao.cursor()

# CRUD

cursor.close()
conexao.close()