# GitHub

## Autenticando máquina

### Token Classic

1. **Crie um Token de Acesso Pessoal no GitHub:**
   - Acesse o GitHub e faça login na sua conta.
   - No canto superior direito, clique na sua foto de perfil e vá em "Settings" (Configurações).
   - No menu à esquerda, selecione "Developer settings" (Configurações de desenvolvedor) e, em seguida, clique em "Personal access tokens" (Tokens de acesso pessoal).
   - Clique em "Generate token" (Gerar token), insira sua senha e configure as permissões necessárias para o token (geralmente, `repo` é suficiente para operações de repositório). Depois, clique em "Generate token" no final da página.

2. **Configurar o Git na sua Máquina:**
   - Abra o terminal ou prompt de comando.
   - Execute os seguintes comandos, substituindo `SEU_TOKEN_AQUI` pelo token que você gerou e `SEU_USUÁRIO_GIT` pelo seu nome de usuário no GitHub.

   ```bash
   git config --global user.name "SEU_USUÁRIO_GIT"
   git config --global user.email "SEU_EMAIL_GIT"

   git config --global credential.helper store
   git config --global credential.helper cache 
   ```

   Certifique-se de substituir `seu_usuario` e `seu_repositorio` pelos seus valores reais.

3. **Realizar Operações no GitHub:**
   - Agora, você deve conseguir clonar, fazer push e pull dos seus repositórios usando o Git sem ser solicitado a inserir suas credenciais toda vez.

Lembre-se de manter seu token seguro e não compartilhá-lo publicamente. Se precisar revogar ou regenerar um token, você pode fazer isso nas configurações do GitHub.

### SSH

1. **Verifique se você já possui uma chave SSH:**
   - Abra o terminal ou prompt de comando.
   - Digite o seguinte comando para verificar se você já possui uma chave SSH: 
     ```bash
     ls -al ~/.ssh
     ```
   - Se você já tiver uma chave chamada `id_rsa` (chave privada) e `id_rsa.pub` (chave pública), você pode pular para o próximo passo. Caso contrário, continue com o próximo passo.

2. **Gere um novo par de chaves SSH:**
   - Se você não tem uma chave SSH, você pode gerar uma nova usando o seguinte comando:
     ```bash
     ssh-keygen -t ed25519 -C "your_email@example.com"
     ```
   - Pressione Enter para aceitar o local padrão para salvar a chave (normalmente `~/.ssh/id_rsa`), e configure uma senha se desejar.

3. **Adicione a chave SSH ao agente SSH (opcional, mas recomendado):**
   - Para adicionar a chave ao agente SSH e evitar ter que digitar a senha toda vez que usar a chave, execute os seguintes comandos:
     ```bash
     eval "$(ssh-agent -s)"
     ssh-add ~/.ssh/id_ed23319
     ```

4. **Adicione a chave SSH à sua conta do GitHub:**
   - Copie a chave pública para a área de transferência:
     ```bash
     cat ~/.ssh/id_ed23319.pub | pbcopy  # para sistemas macOS
     ```

     ou

     ```bash
     cat ~/.ssh/id_ed23319.pub | clip  # para sistemas Windows
     ```

   - Acesse o GitHub, vá em "Settings" (Configurações) -> "SSH and GPG keys" (Chaves SSH e GPG) -> "New SSH key" (Nova chave SSH).
   - Cole a chave que você copiou e dê um nome significativo para a chave.

5. **Teste a conexão SSH:**
   - Execute o seguinte comando para verificar se a autenticação SSH está funcionando corretamente:
     ```bash
     ssh -T git@github.com
     ```

   - Se tudo estiver configurado corretamente, você verá uma mensagem indicando que você foi autenticado com sucesso.

Agora, sua máquina está configurada para autenticar com o GitHub usando SSH. Você pode usar o Git normalmente sem precisar digitar suas credenciais a cada operação.

## Verificando commits



1. Instalação do GPG4Win:

1.1. Baixe o GPG4Win:
   - Acesse o [site oficial do GPG4Win](https://www.gpg4win.org/).
   - Baixe a versão mais recente do GPG4Win e execute o instalador.

1.2. Instale o GPG4Win:
   - Siga as instruções do instalador.
   - Certifique-se de selecionar a opção para instalar o Kleopatra durante o processo.

1.3 Configurando VS Code:
   - No vs code, abra as configurações com o atalho "ctrl + ,"
   - procure por "gpg"
   - habilite a caixa "Git: Enable Commit Signing"

1. Geração da Chave GPG com o Kleopatra:

2.1. Abra o Kleopatra:
   - Após a instalação, abra o Kleopatra.

2.2. Crie uma Nova Chave:
   - No Kleopatra, clique em "File" (Arquivo) -> "New Certificate" (Novo Certificado).
   - Siga as instruções para gerar uma nova chave. Insira seu nome e endereço de e-mail.

2.3. Exporte a Chave Pública:
   - Selecione a chave criada.
   - Clique com o botão direito e escolha "Export Certificates" (Exportar Certificados).
   - Guarde o arquivo com a extensão ".asc".

3. Adição da Chave GPG ao GitHub:

3.1. Copie a Chave Pública:
   - Abra o arquivo ".asc" gerado anteriormente com um editor de texto.
   - Copie o conteúdo da chave pública.

3.2. Adicione a Chave ao GitHub:
   - Acesse o GitHub e vá para "Settings" (Configurações) -> "SSH and GPG keys" (Chaves SSH e GPG) -> "New GPG key" (Nova chave GPG).
   - Cole a chave pública copiada e adicione.

4. Configuração do Git para Assinatura de Commits:

4.1. Abra o Terminal ou Prompt de Comando:
   - Abra o terminal ou prompt de comando onde você costuma interagir com o Git.

4.2. Configure o Git:
   - Execute o seguinte comando, substituindo `<SUA_CHAVE>` pela ID da chave GPG ou pelo endereço de e-mail associado à chave:
     ```bash
     git config --global user.signingkey <SUA_CHAVE>
     ```

4.3. Ative a Assinatura Automática de Commits:
   - Execute o seguinte comando para configurar o Git para assinar automaticamente todos os commits:
     ```bash
     git config --global commit.gpgSign true
     ```

5. Teste a Configuração:

5.1. Faça um Novo Commit:
   - Realize um novo commit em um repositório Git.

5.2. Verifique o Status do Commit:
   - Execute o seguinte comando para verificar o status do commit:
     ```bash
     git log --show-signature
     ```
   - Se a configuração estiver correta, você verá a informação de assinatura no log do commit.

5.3. Verificação no GitHub:
   - Vá para o GitHub e verifique se o commit aparece como "Verified" (Verificado).

Com isso, seu ambiente está configurado para assinar e verificar commits usando GPG no Git e GitHub.

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

------

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

Para fazer o pull e push de maneira simplificada no vscode, basta ir na barra vertical esquerda, localizar o "Source Control" e realizar todos esses comandos.

## Apagando repositório

Para apagar um repositório no GitHub, você precisa navegar até a página do repositório que deseja excluir. Em seguida, clique no botão "Settings" (Configurações) no menu à direita. Na seção "Danger Zone" (Zona de Perigo), clique em "Delete this repository" (Excluir este repositório). Isso abrirá uma caixa de diálogo pedindo a confirmação da exclusão. Digite o nome do repositório e clique em "I understand the consequences, delete this repository" (Eu entendo as consequências, excluir este repositório). Lembre-se de que essa ação é irreversível e que todo o histórico de commits e arquivos do repositório serão perdidos.

------

## Versionamento

O número da versão é geralmente atribuído a cada lançamento (release) e não a cada commit. Cada commit é uma alteração no código-fonte do software que pode ser um pequeno ajuste ou uma grande funcionalidade nova.

Normalmente, os desenvolvedores adicionam várias alterações a um repositório antes de criar uma nova release. Eles podem criar commits regulares ao longo do tempo para registrar seu progresso e, quando estiverem prontos para lançar uma nova versão, criarão uma nova tag que representa o número da versão e incluirá todas as alterações (commits) que foram adicionadas desde a última release.

Quanto ao versionamento com o Git e o GitHub, é comum usar as tags do Git para atribuir um número de versão a uma release. Por exemplo, você pode usar o comando git tag para criar uma nova tag e associá-la a um determinado commit. Em seguida, você pode enviar as tags para o GitHub usando o comando git push --tags.

Para criar uma nova release no GitHub, basta navegar até a página do seu repositório no GitHub, clicar na guia "Releases" e clicar no botão "Draft a new release". Em seguida, você pode escolher a tag que deseja associar com a nova release e adicionar quaisquer notas de lançamento relevantes. Quando você publicar a nova release, ela aparecerá na página do seu repositório no GitHub e será vinculada à tag correspondente no histórico de commits do Git.
