# importar dados de usuario.txt
# biblioteca com nome e tamanho
# transforma tamanho em MB
# cria relatorio.txt

users = {}

with open('usuarios.txt', 'r') as input:
    lines = input.readlines()
    for line in lines:
        name, size = line.split()
        size_mb = round(int(size)/1024/1024,2)
        users['name'] = name
        users['size'] = size_mb
        print(users)
print(users)
