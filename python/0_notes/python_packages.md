# Bibliotecas

Tempo:

- import datetime
- import dateutil
- import calendar

Cálculos/números

- import itertools
- import math
- import random

Segurança

- import secrets
- import crypto

DataScience

- import pandas as pd
- import numpy as np
- import matplotlib.pyplot as plt
- import seaborn as sns
- import statsmodels.api as sm
- import statsmodels.formula.api as smf


Tradução/Palavras

- import locale
- import string

Comunicação com o Sistema Operacional

- import os
- import shutil
- import sys
- import pathlib

Planilhas/dados

- import csv
- import json
- import pickle
- import xlrd
- import xlwt
- import xlsxwriter
- import openpyxl
- import xlrd
- import openpyxl
- import xlsxwriter

Scraping

- import request
- import beaultifulsoup4

Navegador

- import selenium

Music from image: <https://github.com/victormurcia/Making-Music-From-Images>

# Criando Pacote

## Passo 1: Criando a estrutura do diretório

Primeiro, crie um diretório para o seu pacote e, dentro dele, crie outro diretório com o mesmo nome do pacote. Este diretório será usado para conter os arquivos do pacote. Por exemplo:

    meu_pacote/
    └── meu_pacote/

## Passo 2: Criando o arquivo init.py

Dentro do diretório meu_pacote, crie um arquivo vazio chamado __init__.py. Esse arquivo indica ao Python que o diretório é um pacote Python.

    meu_pacote/
    └── meu_pacote/
        └── __init__.py

## Passo 3: Escrevendo o código do pacote

Escreva o código do seu pacote dentro do diretório meu_pacote. Você pode criar um ou mais módulos Python, dependendo do tamanho do seu pacote.

    meu_pacote/
    └── meu_pacote/
        ├── __init__.py
        ├── modulo1.py
        └── modulo2.py


## Passo 4: Criando o arquivo setup.py

Crie um arquivo setup.py na raiz do diretório meu_pacote. Este arquivo contém informações sobre o pacote, como nome, versão, autor, descrição, dependências e outros metadados. Além disso, ele contém as instruções para construir, instalar e distribuir o pacote. Veja um exemplo básico de arquivo setup.py abaixo:

    from setuptools import setup, find_packages

    setup(
        name='meu_pacote',
        version='0.1',
        author='Seu Nome',
        author_email='seuemail@exemplo.com',
        description='Uma descrição curta do seu pacote',
        packages=find_packages(),
        install_requires=['numpy', 'matplotlib'],
    )

## Passo 5: Construindo o pacote

Para construir o pacote, abra um terminal na raiz do diretório meu_pacote e execute o seguinte comando:

    python setup.py sdist

Este comando cria um pacote distribuível no formato tar.gz.

## Passo 6: Instalando o pacote

Para instalar o pacote, use o seguinte comando:

    pip install caminho/para/meu_pacote/dist/meu_pacote-0.1.tar.gz

## Passo 7: Usando o pacote

Agora, você pode usar o seu pacote em qualquer projeto Python, importando os módulos do pacote normalmente:

    import meu_pacote.modulo1
    import meu_pacote.modulo2

Pronto! Agora você tem um pacote Python que pode ser facilmente distribuído e instalado em outras máquinas. É claro que existem muitas opções adicionais que você pode adicionar ao arquivo setup.py para personalizar a construção, instalação e distribuição do seu pacote. Consulte a documentação do setuptools para obter mais informações.

# Pacotes específicos

## tree

A biblioteca tree é uma ferramenta para gerar árvores de diretórios a partir de um diretório ou arquivo. Ela está disponível como um pacote Python no PyPI e pode ser instalada utilizando o gerenciador de pacotes pip.

Para instalá-la, basta abrir o terminal e digitar o seguinte comando:

    pip install tree

Após a instalação, a biblioteca pode ser utilizada para gerar uma árvore de diretórios de um diretório específico. Para isso, basta abrir o terminal e navegar até o diretório em questão. Em seguida, execute o comando tree seguido do nome do diretório:

    tree diretorio
        ou
    tree /caminho/completo/para/diretorio

O comando tree irá listar todos os arquivos e subdiretórios contidos no diretório informado, organizando-os em uma árvore de diretórios com uma representação similar à seguinte:

    diretorio/
    ├── arquivo1.txt
    ├── arquivo2.txt
    ├── subdiretorio1/
    │   ├── arquivo3.txt
    │   └── arquivo4.txt
    └── subdiretorio2/
        ├── arquivo5.txt
        └── arquivo6.txt

Além disso, a biblioteca tree possui diversos parâmetros opcionais que permitem personalizar a exibição da árvore de diretórios, como:

- -a: exibe todos os arquivos, incluindo os arquivos ocultos;
- -f: exibe os nomes completos dos arquivos, incluindo o caminho completo até eles;
- -d: exibe apenas os diretórios, sem os arquivos;
- -L n: define o nível máximo de profundidade da árvore;
- -I pattern: exclui da árvore os arquivos que correspondem ao padrão informado.

Para mais informações sobre esses parâmetros e outros recursos da biblioteca tree, consulte a documentação oficial da biblioteca: https://pypi.org/project/tree/