# importar dados de usuario.txt
# biblioteca com nome e tamanho
# transforma tamanho em MB
# cria relatorio.txt

with open('usuarios.txt', 'r') as input:
    lines = input.readlines()
    for line in lines:
        name, size = line.split()
        size_mb = round(int(size)/1024/1024,2)
        print(name)
        print(size_mb)
