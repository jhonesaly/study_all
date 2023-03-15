# Django

## Arquitetura e Características

Django é um framework que faz o meio campo entre um web browser e um banco de dados.

Seus principais elementos estruturais são:

- **Model**: Define a estrutura lógica de dados e é o manipulador de dados entre o banco de dados e a view.
- **Template**: É a camada de apresentação. Django usa um sistema de modelo de texto simples que mantém tudo o que o navegador renderiza.
- **View**: Comunica-se com o banco de dados através do Model e transfere os dados para o Template para visualização.

Quando o Django recebe um HTTP Request do browser, esse vai para o arquivo de URLs, que procura nas pastas uma view que tenha o endereço certo.

A View puxa a informação da base de dados através do Model, que faz a filtragem e tratamento adequado da informação por meio de sua lógica.

Com os dados prontos, a View envia para um dos Templates que enviam o HTTP Response com as instruções de renderização no browser.

Todos esses arquivos ficam dentro de um projeto Django, que é pasta base com seus settings e o conjunto de aplicativos.

Aplicações são grupos de modelos, views, templates e URLs que interagem com o framework para providenciar funcionalidades, podendo ser reutilizado em vários projetos.

Principais características:

- loosely coupled
- DRY principle
- MTV pattern

------

## Criando ambiente virtual

O primeiro passo para criar uma aplicação web em Django é criar um ambiente virtual. Isso compartimentaliza o projeto, de modo que os projetos possam usar versões diferentes, muito comum no desenvolvimento web.

Comandos no Windows:

    1. py -m venv my_env
    2. my_env\Scripts\activate
    3. pip install django

Explicando:

1. cria o ambiente virtual (pasta my_env)
2. ativa o ambiente virtual
3. instala o Django usando python

------

## Pasta de projeto Django

Criando projeto:

    django-admin startproject mysite

Pastas criadas:

- **manage.py**: Este é um utilitário de linha de comando usado para interagir com seu projeto. você não precisa para editar este arquivo.
- **mysite/__init__.py**: Um arquivo vazio que diz ao Python para tratar o diretório mysite como um Python módulo.
- **mysite/asgi.py**: Esta é a configuração para rodar seu projeto como um Servidor Assíncrono Aplicativo Gateway Interface (ASGI) com servidores da Web compatíveis com ASGI. ASGI é o padrão Python emergente para servidores e aplicativos web assíncronos.
- **mysite/settings.py**: Isso indica definições e configurações para seu projeto e contém configurações padrão iniciais.
- **mysite/urls.py**: Este é o lugar onde estão seus padrões de URL. Cada URL definido aqui é mapeado para uma exibição.
- **mysite/wsgi.py**: Esta é a configuração para rodar seu projeto como um Web Server Gateway Interface (WSGI) com servidores da Web compatíveis com WSGI.

Migrando a base de dados:

    cd mysite
    python manage.py migrate

------

## Project settings

- **DEBUG**: é um booleano que ativa e desativa o modo de depuração do projeto. Se for definido como True, Django exibirá páginas de erro detalhadas quando uma exceção não capturada for lançada por seu aplicativo. Ao mudar para um ambiente de produção, lembre-se de que você deve defini-lo como False. Nunca implante um site em produção com o DEBUG ativado porque você exporá informações confidenciais dados relacionados ao projeto.
- **ALLOWED-HOSTS**: não é aplicado enquanto o modo de depuração está ativado ou quando os testes são executados. uma vez que você mova seu site para produção e defina DEBUG como False, você terá que adicionar seu domínio/host a esta configuração para permitir que ele sirva seu site Django.
- **ISTALLED_APPS**: é uma configuração que você terá que editar para todos os projetos. Esta configuração diz ao Django qual aplicativos estão ativos para este site. Por padrão, o Django inclui os seguintes aplicativos:
  - **django.contrib.admin**: Um site de administração
  - **django.contrib.auth**: Um framework de autenticação Quando você tem que lidar com vários ambientes que requerem configurações diferentes, você pode criar um arquivo de configurações diferentes para cada ambiente.
  - **django.contrib.contenttypes**: Um framework para lidar com tipos de conteúdo
  - **django.contrib.sessions**: Uma estrutura de sessão
  - **django.contrib.messages**: Uma estrutura de mensagens
  - **django.contrib.staticfiles**: Um framework para gerenciar arquivos estáticos
- **MIDDLEWARE é uma lista que contém o middleware a ser executado.
- **ROOT_URLCONF**: indica o módulo Python onde os padrões de URL raiz do seu aplicativo são definidos.
- **DATABASES**: é um dicionário que contém as configurações de todos os bancos de dados a serem utilizados no projeto. Sempre deve haver um banco de dados padrão. A configuração padrão usa um banco de dados SQLite3.
- **LANGUAGE_CODE**: define o código de idioma padrão para este site Django.
- **USE_TZ**: diz ao Django para ativar/desativar o suporte ao fuso horário. Django vem com suporte para datas com reconhecimento de fuso horário. Essa configuração é definida como True quando você cria um novo projeto usando o comando de gerenciamento de projeto inicial.

------

## Rodando o Django

Comando para iniciar o Django

    python manage.py runserver

isso fará o Django iniciar o seu serviço na porta padrão 8000. Acessando o IP local e abrindo essa porta (<http://127.0.0.1:8000>), aparecerá uma imagem mostrando que o django foi configurado corretamente.

------

## Criando Apps

O comando para criar um novo app é:

    python manage.py startapp blog

Isso irá criar a pasta blog/ da aplicação com os seguintes arquivos:

- **__init__.py**: Um arquivo vazio que informa ao Python para tratar o diretório do blog como um módulo Python.
- **admin.py**: Aqui é onde você registra os modelos para incluí-los na administração do Django site—a utilização deste site é opcional.
- **apps.py**: inclui a configuração principal do aplicativo de blog.
- **migrations**: Este diretório conterá as migrações do banco de dados da aplicação. Migrações permitem que o Django rastreie as alterações do seu modelo e sincronize o banco de dados de acordo. Esta diretório contém um arquivo __init__.py vazio.
- **models.py**: Isso inclui os modelos de dados do seu aplicativo; todos os aplicativos Django precisam tem um arquivo models.py, mas pode ser deixado vazio.
- **tests.py**: Aqui é onde você pode adicionar testes para sua aplicação.
- **views.py**: A lógica do seu aplicativo vai aqui; cada visualização recebe uma solicitação HTTP, processa e retorna uma resposta.

------

## API

O Django oferece suporte para a criação de APIs através do Django REST framework. O Django REST framework é uma extensão para o Django que fornece ferramentas e bibliotecas para ajudar na criação de APIs RESTful.

Para criar uma API com o Django REST framework, você precisará seguir os seguintes passos:

- Instalar o Django REST framework: Para começar, você precisará instalar o Django REST framework usando o pip. Basta abrir um terminal e digitar o seguinte comando:

    pip install djangorestframework

- Configurar o Django REST framework: Em seguida, você precisará configurar o Django REST framework adicionando as configurações necessárias ao arquivo settings.py do seu projeto Django.
- Definir as views: Agora você precisa definir as views que irão mapear as URLs da sua API para as funções que irão lidar com as solicitações HTTP. Isso pode ser feito usando as classes genéricas fornecidas pelo Django REST framework, como APIView ou ViewSet.
- Definir as URLs: Por fim, você precisará definir as URLs que mapeiam as solicitações HTTP para as views corretas. Isso é feito usando o arquivo urls.py da sua aplicação Django.

Após seguir esses passos, você terá uma API RESTful em execução usando o Django REST framework. Seus clientes poderão se comunicar com sua API usando solicitações HTTP, como GET, POST, PUT e DELETE, e receber respostas em formatos como JSON ou XML.

------

## Static Files
### STATIC_URL:

STATIC_URL é a URL base que o Django usará para servir arquivos estáticos (como arquivos CSS, JavaScript e imagens) em uma aplicação web. Por padrão, o valor de STATIC_URL é "/static/", o que significa que os arquivos estáticos serão servidos em uma URL com esse formato: http://example.com/static/. Você pode alterar essa configuração no arquivo "settings.py" do seu projeto Django.

Por exemplo, se você quiser alterar a URL base de arquivos estáticos para "/assets/", você pode adicionar a seguinte linha ao seu arquivo "settings.py":

    STATIC_URL = '/assets/'

Dessa forma, o Django usará a URL http://example.com/assets/ para servir os arquivos estáticos da sua aplicação.

### STATICFILES_DIRS:

STATICFILES_DIRS é uma configuração que especifica uma lista de diretórios onde o Django deve procurar por arquivos estáticos. Por padrão, o Django procura por arquivos estáticos em um diretório chamado "static" dentro de cada aplicação instalada. No entanto, você também pode especificar outros diretórios que contenham arquivos estáticos que não estão associados a nenhuma aplicação específica.

Por exemplo, se você tiver um diretório em seu projeto chamado "assets" que contém arquivos estáticos, você pode adicionar o seguinte código ao seu arquivo "settings.py":

    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'assets'),
    ]

Dessa forma, o Django irá procurar por arquivos estáticos dentro do diretório "assets" no diretório raiz do seu projeto. Observe que você precisa importar o módulo "os" para usar a função "os.path.join()" neste exemplo.

Com essas configurações, você pode servir arquivos estáticos em sua aplicação Django de forma fácil e eficiente.

### STATIC_ROOT:

STATIC_ROOT é a configuração que especifica o diretório em que o Django irá coletar todos os arquivos estáticos da sua aplicação, em preparação para a implantação em um servidor de produção. Você precisa definir essa configuração para que o comando "collectstatic" possa coletar todos os arquivos estáticos em um único diretório.

Por exemplo, se você deseja coletar todos os arquivos estáticos em um diretório chamado "staticfiles" na raiz do seu projeto, você pode adicionar o seguinte código ao seu arquivo "settings.py":

    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

Observe que você precisa importar o módulo "os" para usar a função "os.path.join()" neste exemplo.

### collectstatic:

O collectstatic é um comando do Django que coleta todos os arquivos estáticos das suas aplicações e reúne-os em um único diretório especificado em STATIC_ROOT, que pode então ser servido por um servidor web.

Para usar o collectstatic, você precisa primeiro definir STATIC_ROOT em seu arquivo "settings.py". Em seguida, abra um terminal e navegue até o diretório raiz do seu projeto. Digite o seguinte comando:

    python manage.py collectstatic

Isso coletará todos os arquivos estáticos da sua aplicação e salvá-los no diretório especificado em STATIC_ROOT.

É importante lembrar que você precisa executar o comando collectstatic sempre que adicionar, atualizar ou remover arquivos estáticos em sua aplicação web. Isso garantirá que todos os arquivos estáticos necessários estejam disponíveis para sua aplicação, mesmo após a implantação em um servidor de produção.

Com essas configurações e o comando collectstatic, você pode gerenciar facilmente os arquivos estáticos em sua aplicação Django e implantá-los em um ambiente de produção.

