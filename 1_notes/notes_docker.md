# Docker

## Arquitetura

- Container image: pacote com todas as dependências que criam o contêiner. A imagem é como classe e o conteiner é o objeto instanciado
- Dockerfile: arqiovo de texto que contém todas as intruções para fazer o build da imagem (container image)
- Build: ação que cria uma imagem a partir do dockerfile
- Container: instância da imagem que representa uma aplicação, processo ou serviço
- Volumes: permite que o container armazene dados, de modo que em caso de finalização do conteiner, os dados persistem.
- Tag: auxiliar de versionamento das imagens
- Multi-stage build: 
- Repository: conjunto de imagens
- Registry: provê acesso do docker a um repository.
- Docker Hub: Repositório público
- Compose: metadata que permite criar múltiplos contêiners com um único comando

--------------
## Comandos

    docker ps
    docker run
    docker exec
    inspect conteiner-name

- ps: mostra os conteiners em execução
- run: cria um container
- exec: entra no conteiner
- inspect conteiner-name: dá as informações do conteiner-name especificado
