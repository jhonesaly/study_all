from zipfile import ZipFile
import os

# Para caminhos com barra invertida (\), utilize r
caminho = r'C:\Users\Cougar_Gamer\Desktop\Workspace\Projetos\Zipper\Input'

# Caminho do arquivo zipado (na pasta de entrada)
caminho_zip = os.path.join(caminho, 'arquivo.zip')

# ESCREVE
with ZipFile(caminho_zip, 'w') as zip:
    for arquivo in os.listdir(caminho):
        caminho_completo = os.path.join(caminho, arquivo)
        zip.write(caminho_completo, arquivo)

# LISTA
with ZipFile(caminho_zip, 'r') as zip:
    for arquivo in zip.namelist():
        print(arquivo)

# EXTRAI
with ZipFile(caminho_zip, 'r') as zip:
    # Cria a pasta de destino, se ela não existir
    if not os.path.exists(caminho_zip):
        os.makedirs(caminho_zip, exist_ok=True)
    zip.extractall(os.path.join(caminho, 'descompactado'))
