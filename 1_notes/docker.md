# Docker

Servidor bare metal: um servidor físico dedicado a um único inquilino.

## Problemas com a nuvem privada:

- dificuldade com a segurança da tecnologia da informação (lógica e física)
- Custo com a mão de obra especializada
- Custo de hardware
- Custo de energia elétrica
- Uso de geradores em caso de queda de energia
- Despesas inesperadas

## Vantagens de usar nuvem pública:

- preço (pague somente o que usar)
- facilidade de contratação, configuração e infraestrutura
- escalabilidade
- performance

# Microsserviços

arquitetura de software, que consiste em construir aplicações desmembrando-as em serviços independentes. Estes serviços se comunicam entre si usando APIs e promovem grande agilidade e escalabilidade em times de desenvolvimento.

Quando há uma aplicação monolítica e ela roda na máquina de vários clientes, é desperdiçada muito processamento enviando informações que não serão utilizadas, pois nem tudo no código o cliente irá usar. Mas quando um grande software é quebra de em microsserviços, pode-se dar mais processamento para os que efetivamente necessitam de mais.

# Cluster

Consiste em computadores ligados que trabalham em conjunto, de modo que, em muitos aspectos, podem ser considerados como um único sistema. Cada máquina presente em um cluster é conhecido como nó (node).


## Docker Swarm

Swarm é um recurso do docker que fornece funcionalidades de orquestração de contêiner, incluindo clustering nativo de hosts do Docker e agendamento de cargas de trabalho de contêineres.

Se tiver problema de hardware em um dos nós, o container automaticamente passa para outro nó.

# Docker Hub

repositório onde estão as imagens dos ambientes rodando determinada aplicação. <https://hub.docker.com/search?q=mysql>

Criando container MySQL...


# Arquitetura

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
# Comandos

    docker ps
    docker run
    docker exec
    inspect conteiner-name

- ps: mostra os conteiners em execução
- run: cria um container
- exec: entra no conteiner
- inspect conteiner-name: dá as informações do conteiner-name especificado
