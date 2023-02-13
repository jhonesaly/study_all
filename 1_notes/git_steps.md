# Gerenciando repositório local

## init

    git init 

> Cria a pasta .git e torna a pasta atual um repositório
> No vscode o git init pode ser criado em source control

## config

    git config --list
    git config --global
    git config --unset user.name

> 'list' vai listar todas as configurações do Git
> 'global' vai aplicar alterações em todos os repositórios
> 'unset' remove algo das configurações

### user

    git config --global user.email "example@email.com"
    
    git config --global user.name namexample

> atribui um e-mail e apelido para o usuário do git

## Atributos Git

- Untracked (U - green)
- Unmodified ( - gray)
- Modified (M - orange)
- Staged

> Alterar arquivo muda o seu sha1, que altera atributo de Unmodified para Modified
> Remover arquivo Unmodified o torna Untracked

## Add
    
    git add *

> Muda o atributo de um arquivo para Staged
> selecionar todos os arquivos: '*','.' e '-A'

## commit

    git commit -m "anotações"

> Cria snapshot (como checkpoint) dos arquivos Staged 
> Modifica atributos para Unmodified
> Nomeia snapshot
> Arquivos do Commit passam a integrar o Local Repository
> Local Repository pode ser empurrado para um Remote Repository (GitHub)

## status

    git status

## log

    git log

> Monstra commits do repositório

## clone

    git clone https://github.com/username/remoterepository

> clona para o repositório local um repositório no github
> pode ser feito com o Git bash

## push

    git push -u origin main

> empurra as alterações 'staged' para a nuvem
> A opção "-u" é usada para estabelecer a associação entre o ramo local e o ramo remoto. Isso significa que, ao usar "git push -u origin main", você está informando ao Git que deseja que o ramo "main" no repositório remoto "origin" seja o destino padrão para futuros "git push" no seu ramo local "main".
> "Origin" é o nome padrão que o Git dá ao repositório remoto quando você clona um repositório pela primeira vez usando "git clone". No entanto, você pode dar a ele outro nome, se desejar. Para fazer isso, você pode usar o comando "git remote rename"
> Você pode verificar qual nome está sendo usado para o ramo principal de um repositório Git usando o seguinte comando: git branch -a