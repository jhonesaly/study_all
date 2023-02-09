# Gerenciando repositório remoto no GitHub

## Criando repositório remoto

- Com sua conta GitHub criada (username), vá em: <https://github.com/new>
- Crie o repositoryname
- Faça a descrição (opcional)
- Set Public (outros podem ver) ou Private (outros não podem ver)
- add README.md file (arquivo que descreve o repositório com mais detalhes)
- add .gitignore (tipos de arquivos que serão ignorados quando realizar o commit)

### README.md

Arquivo que descreve detalhadamente os componentes e objetivos do repositório. Utiliza para tal a extensão .md que são arquivos markdown. Para saber mais, veja o arquivo notes_markdown.md (link: <https://github.com/jhonesaly/git-study/blob/main/notes_markdown.md>) nesse repositório.

### .gitignore

Arquivo que faz certos tipos de arquivo serem ignorados na hora do commit, facilitando questões de segurança (não fazer commit de dados sensíveis) e de espaço (não fazer commit das bibliotecas baixadas)

Ex de .gitignore para python (Link: <https://github.com/jhonesaly/git-study/blob/main/.gitignore>)

    *.txt # evita que a extensão (txt no caso) entre no commit
    downloads/ # evita que a pasta (downloads no caso) entre no commit 

### License 

Tipos de licença de distribuição disponíveis no GitHub:

- None: Sem licença
- Licença MIT: Uma licença permissiva que permite que o código seja usado, modificado e distribuído para qualquer finalidade, desde que seja incluida uma cópia da licença e os créditos aos autores originais.
- Licença GPL: Uma licença copyleft que exige que qualquer software que use o código licenciado também seja liberado sob a mesma licença GPL. Isso garante que o código permaneça livre e aberto, mesmo quando é incluído em outros projetos.
- Licença CC-NC (Creative Commons - NonCommercial): Essa licença permite que o código seja usado, modificado e distribuído sem fins comerciais. Isso significa que você não pode usar o código para ganhar dinheiro, mas pode usá-lo para outros fins, como aprendizado ou pesquisa.



## Adicionando arquivos no repositório remoto

O repositório remoto pode ser criado primeiramente no Github e então os arquivos serem criados diretamente nele, ou pode-se jogar todos os arquivos de um repositório local, com todos os seus commits, para o um repositório remoto através do comando push.

Para trazer um repositório remoto e suas alterações para o repositório local, utiliza-se o comando pull.

### Criando repositório local vazio fazendo pull para remoto

    echo "# git-study" >> README.md
    git init
    git add README.md
    git commit -m "first commit"
    git branch -M main
    git remote add origin git@github.com:username/repositoryname.git
    git push -u origin main

> para fazer o pull é necessário fornecer a senha de acesso ao seu GitHub


### Pull de repositório local para o repositório remoto

    git remote add origin git@github.com:username/repositoryname.git
    git branch -M main
    git push -u origin main

> O comando "git remote add origin git@github.com:username/repositoryname.git" adiciona um novo repositório remoto chamado "origin" com a URL especificada. A URL é o endereço do repositório no GitHub criado por "username" com o nome "repositoryname". Esse comando é geralmente usado quando você está criando um novo repositório local e deseja vinculá-lo a um repositório remoto, como o GitHub.

> O comando "git branch -M main" renomeia a branch atual para "main". Isso é útil quando você quer mudar o nome da branch principal de um repositório, para evitar conflitos com as convenções de nomenclatura de branch.

> O comando "git push -u origin main" envia as alterações da branch local "main" para o repositório remoto "origin" e cria uma nova branch com o mesmo nome no repositório remoto. O parâmetro "-u" é usado para estabelecer a branch remota como a branch padrão para o qual as alterações serão enviadas no futuro. Isso é útil para garantir que as alterações na branch local sejam sempre enviadas para a branch remota correspondente.

### Pull usando vscode

Para fazer o pull e push de maneira simplificada no vscode, basta ir na barra vertical esqueda, localizar o "Source Control" e realizar todos esses comandos.

## Apagando repositório

Para apagar um repositório no GitHub, você precisa navegar até a página do repositório que deseja excluir. Em seguida, clique no botão "Settings" (Configurações) no menu à direita. Na seção "Danger Zone" (Zona de Perigo), clique em "Delete this repository" (Excluir este repositório). Isso abrirá uma caixa de diálogo pedindo a confirmação da exclusão. Digite o nome do repositório e clique em "I understand the consequences, delete this repository" (Eu entendo as consequências, excluir este repositório). Lembre-se de que essa ação é irreversível e que todo o histórico de commits e arquivos do repositório serão perdidos.