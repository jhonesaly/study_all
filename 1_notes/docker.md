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

O Docker Swarm é uma ferramenta que permite orquestrar a implantação e gerenciamento de aplicativos distribuídos em um ambiente de contêiner. Ele permite que você agrupe um conjunto de hosts Docker em um cluster, o que permite que os aplicativos sejam executados em vários contêineres em vários hosts.

Um cluster do Docker Swarm pode ser composto por várias máquinas, cada uma executando o Docker Engine. Cada máquina no cluster é chamada de "nó" e é capaz de executar contêineres. No entanto, o Docker Swarm abstrai a complexidade de gerenciamento de múltiplos hosts e os apresenta como um único host virtual para o usuário.

Os contêineres são as unidades básicas de implantação no Docker Swarm. Eles podem ser implantados em qualquer nó no cluster, e o Swarm garante que haja um número específico de contêineres em execução a qualquer momento para garantir a disponibilidade do aplicativo. Os contêineres são agrupados em serviços, que são uma definição lógica do aplicativo a ser implantado. Os serviços podem ser escalados horizontalmente (adicionando ou removendo contêineres), atualizados, removidos e gerenciados de maneira transparente pelo Docker Swarm.

Portanto, um cluster do Docker Swarm é composto por máquinas que executam o Docker Engine e essas máquinas hospedam contêineres que executam os aplicativos. O Swarm abstrai a complexidade de gerenciamento de múltiplos hosts e contêineres e apresenta uma única interface para o usuário gerenciar o aplicativo distribuído.

# Docker Hub

O Docker Hub é um registro de imagens de contêineres mantido pela Docker, Inc. É um serviço baseado na nuvem que permite que os desenvolvedores compartilhem e gerenciem imagens de contêineres. Os usuários podem enviar suas próprias imagens de contêineres para o Docker Hub e também podem baixar imagens de contêineres de outras pessoas.

O Docker Hub é uma plataforma central para encontrar e compartilhar imagens de contêineres. Ele permite que os desenvolvedores compartilhem imagens de contêineres publicamente ou as mantenham privadas, exigindo autenticação para acessá-las. O Docker Hub também fornece recursos para integração contínua e entrega contínua (CI/CD) e colaboração em equipe.

Os desenvolvedores podem usar o Docker Hub para hospedar suas próprias imagens de contêineres ou podem usar as imagens públicas disponíveis no registro para executar aplicativos. Ao usar imagens de contêineres do Docker Hub, os desenvolvedores podem reduzir o tempo e o esforço necessários para configurar um ambiente de desenvolvimento ou produção, pois as imagens contêm tudo o que é necessário para executar o aplicativo, incluindo o sistema operacional, bibliotecas e dependências.

O Docker Hub é uma plataforma importante para a comunidade de contêineres, pois ajuda a promover a adoção de contêineres ao fornecer uma maneira fácil de compartilhar e distribuir imagens de contêineres.

repositório onde estão as imagens dos ambientes rodando determinada aplicação. <https://hub.docker.com/search?q=mysql>

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

    > docker ps : mostra os conteiners em execução
    > docker run : cria um container
    > docker exec : entra no conteiner
    > docker nspect <conteiner-name> : dá as informações do conteiner-name especificado
    > docker image ls : lista as imagens na máquina
    > docker stop <id_container> : para o container
    > docker kill <id_container> : força a parada do container
    > docker rm <id_container> : apaga container
    > docker container prune -f : Remove todos os containers parados
    > docker kill $(docker ps -q) : Remove todos os containers em execução
    > docker rm -f $(docker ps -aq) : Remove todos os containers (parados e em execução)
    > docker image prune -f : Remove todas as imagens
    > docker container prune --force --filter "label!=com.docker.stack.namespace" : Remove containers órfãos (não associados a nenhum serviço ou stack)
    
    docker network prune -f : Remove todas as redes não utilizadas
    docker volume prune -f : Remove todos os volumes não utilizados