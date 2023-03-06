# Gerenciando repositório local

## Comandos

- git init : Cria a pasta .git e torna a pasta atual um repositório

> No vscode o git init pode ser criado em source control

- git config --list
- git config --global
- git config --unset user.name

> 'list' vai listar todas as configurações do Git
> 'global' vai aplicar alterações em todos os repositórios
> 'unset' remove algo das configurações

- git config --global user.email "example@email.com"
- git config --global user.name namexample

> atribui um e-mail e apelido para o usuário do git

- git add * : Muda o atributo de um arquivo para Staged

> selecionar todos os arquivos: '*','.' e '-A'

- git commit -m "anotações" : Cria snapshot (como checkpoint) dos arquivos Staged
    git commit -m "Closes #x" : se tiver uma issue com o número x aberta, será fechada

> Modifica atributos para Unmodified
> Nomeia snapshot
> Arquivos do Commit passam a integrar o Local Repository
> Local Repository pode ser empurrado para um Remote Repository (GitHub)

- git status : Mostra a situação atual da branch
- git log : Monstra commits do repositório
- git clone <https://github.com/username/remoterepository> :clona para o repositório local um repositório no github

> pode ser feito com o Git bash

- git push -u origin main: empurra as alterações 'staged' para a nuvem
- git push --set-upstream origin new_branch : exporta a branch criada no repositório local para a nuvem

> A opção "-u" é usada para estabelecer a associação entre o ramo local e o ramo remoto. Isso significa que, ao usar "git push -u origin main", você está informando ao Git que deseja que o ramo "main" no repositório remoto "origin" seja o destino padrão para futuros "git push" no seu ramo local "main".
> "Origin" é o nome padrão que o Git dá ao repositório remoto quando você clona um repositório pela primeira vez usando "git clone". No entanto, você pode dar a ele outro nome, se desejar. Para fazer isso, você pode usar o comando "git remote rename"
> Você pode verificar qual nome está sendo usado para o ramo principal de um repositório Git usando o seguinte comando: git branch -a

- git branch: mostra as branches disponíveis no repositório local.
- git checkout [option] branch_name: muda para branch_name.
  - [-b]: se não houver branch destino, cria e muda
- git fetch: faz o download de tudo que está no reposótio remoto e não está no local.
- git merge: exclui arquivos duplicados ou que foram substituídos por novos no fetch.
- git pull: faz o fetch e depois o merge de uma vez.

## Atributos Git

- Untracked (U - green)
- Unmodified ( - gray)
- Modified (M - orange)
- Staged

> Alterar arquivo muda o seu sha1, que altera atributo de Unmodified para Modified
> Remover arquivo Unmodified o torna Untracked

## Conventional Commits

Os Conventional Commits são um padrão de mensagens de commit que ajudam a padronizar a comunicação entre desenvolvedores de software sobre as mudanças realizadas em um código-fonte. O objetivo é facilitar a automação do processo de release notes, geração de changelogs e análise de impacto de alterações.

As mensagens de commit seguem uma estrutura predefinida, com um cabeçalho que descreve o tipo de alteração realizada (como "feat" para uma nova funcionalidade ou "fix" para uma correção de bug), seguido de um escopo opcional e uma descrição detalhada do que foi alterado. Além disso, as mensagens também podem incluir um corpo para fornecer mais informações e um rodapé para incluir referências a issues relacionadas ou notas de rodapé.

Ao seguir os Conventional Commits, os desenvolvedores podem ter uma comunicação mais clara e eficiente, permitindo que outros membros da equipe entendam rapidamente o que foi alterado e por que, além de facilitar a automação de processos relacionados a controle de versão e gestão de mudanças.

Cada commit segue o formato <tipo>(<escopo>): <descrição>. O tipo descreve o tipo de alteração realizada (como feat para uma nova funcionalidade, fix para uma correção de bug, docs para uma mudança na documentação, style para uma alteração de estilo ou test para novos testes). O escopo é opcional e pode ser usado para especificar o contexto da alteração, e a descrição detalha o que foi alterado. Ao seguir essas regras, a comunicação entre os membros da equipe é padronizada e torna mais fácil entender o que foi alterado e por quê.

exemplos:

- feat: add feature to allow users to upload profile picture
- fix(authentication): fix issue with login form not clearing after logout
- docs: update README with instructions for running tests
- style(header): change background color of header to match new design
- test: add unit test for new function to calculate user age

### types

Existem alguns tipos predefinidos de Conventional Commits que são comumente usados para descrever o tipo de alteração realizada. Aqui estão alguns exemplos dos tipos mais comuns:

- feat: para uma nova funcionalidade ou recurso adicionado ao sistema
- fix: para uma correção de bug ou problema no sistema
- docs: para uma mudança na documentação, como atualizações no README, no manual do usuário ou na documentação técnica
- style: para uma alteração na formatação ou no estilo do código, sem afetar o seu comportamento ou funcionalidade
- refactor: para uma alteração no código que não adiciona novas funcionalidades ou corrige bugs, mas melhora a sua estrutura ou legibilidade
- test: para adição ou atualização de testes unitários ou de integração
- build: para alterações no processo de build ou na configuração do ambiente de desenvolvimento
- chore: para mudanças em arquivos de configuração, dependências ou outras tarefas relacionadas à manutenção do projeto

### escopo

o escopo é uma parte opcional da mensagem de commit dos Conventional Commits que pode ser usada para especificar o contexto da alteração. Em muitos casos, o escopo é usado para identificar o módulo ou componente específico do sistema que foi alterado.

O escopo pode ser definido de várias maneiras, dependendo da estrutura e do tamanho do projeto. Um escopo pode ser um componente, um módulo, uma página ou uma funcionalidade específica. Um arquivo específico também pode ser usado como escopo, especialmente se o arquivo é um componente independente que é frequentemente alterado.

Não é necessário incluir a extensão do arquivo como parte do escopo. O escopo deve ser uma descrição curta e concisa do componente ou funcionalidade específica que foi alterada, e não deve conter informações adicionais como a extensão do arquivo ou outras informações técnicas desnecessárias.

Por exemplo, se você estiver fazendo uma alteração em um arquivo home.js que faz parte de um componente HomePage, você pode usar HomePage como escopo da sua mensagem de commit. A mensagem de commit pode ser feat(HomePage): adiciona animação de transição na navegação ou fix(HomePage): corrige erro na renderização do componente. Dessa forma, outros desenvolvedores podem entender rapidamente qual parte do sistema foi alterada e por quê.

### Dicas

- Escreva a mensagem de commit no imperativo: isso ajuda a dar clareza sobre o que foi alterado no commit e torna a mensagem mais fácil de entender. Por exemplo, "corrige um bug" em vez de "corrigido um bug".
- Seja breve e direto ao ponto: a mensagem deve ser clara e concisa, de modo que outras pessoas possam entender rapidamente a alteração que foi feita.
- Descreva o que foi alterado e por quê: explique brevemente qual a alteração realizada e por que ela foi necessária. Isso ajuda outros desenvolvedores a entender melhor a alteração e a decidir se precisam revisá-la ou não.
- Não inclua informações desnecessárias: evite incluir informações desnecessárias, como nomes de arquivos, extensões ou informações técnicas que não sejam relevantes para a alteração realizada.
- Se a informação não coube no commit, foi feito demais.
