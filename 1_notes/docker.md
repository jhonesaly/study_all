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

## Microsserviços

arquitetura de software, que consiste em construir aplicações desmembrando-as em serviços independentes. Estes serviços se comunicam entre si usando APIs e promovem grande agilidade e escalabilidade em times de desenvolvimento.

Quando há uma aplicação monolítica e ela roda na máquina de vários clientes, é desperdiçada muito processamento enviando informações que não serão utilizadas, pois nem tudo no código o cliente irá usar. Mas quando um grande software é quebra de em microsserviços, pode-se dar mais processamento para os que efetivamente necessitam de mais.

## Cluster

Consiste em computadores ligados que trabalham em conjunto, de modo que, em muitos aspectos, podem ser considerados como um único sistema. Cada máquina presente em um cluster é conhecido como nó (node).

## Docker Swarm

O Docker Swarm é uma ferramenta que permite orquestrar a implantação e gerenciamento de aplicativos distribuídos em um ambiente de contêiner. Ele permite que você agrupe um conjunto de hosts Docker em um cluster, o que permite que os aplicativos sejam executados em vários contêineres em vários hosts.

Um cluster do Docker Swarm pode ser composto por várias máquinas, cada uma executando o Docker Engine. Cada máquina no cluster é chamada de "nó" e é capaz de executar contêineres. No entanto, o Docker Swarm abstrai a complexidade de gerenciamento de múltiplos hosts e os apresenta como um único host virtual para o usuário.

Os contêineres são as unidades básicas de implantação no Docker Swarm. Eles podem ser implantados em qualquer nó no cluster, e o Swarm garante que haja um número específico de contêineres em execução a qualquer momento para garantir a disponibilidade do aplicativo. Os contêineres são agrupados em serviços, que são uma definição lógica do aplicativo a ser implantado. Os serviços podem ser escalados horizontalmente (adicionando ou removendo contêineres), atualizados, removidos e gerenciados de maneira transparente pelo Docker Swarm.

Portanto, um cluster do Docker Swarm é composto por máquinas que executam o Docker Engine e essas máquinas hospedam contêineres que executam os aplicativos. O Swarm abstrai a complexidade de gerenciamento de múltiplos hosts e contêineres e apresenta uma única interface para o usuário gerenciar o aplicativo distribuído.

## Docker Hub

O Docker Hub é um registro de imagens de contêineres mantido pela Docker, Inc. É um serviço baseado na nuvem que permite que os desenvolvedores compartilhem e gerenciem imagens de contêineres. Os usuários podem enviar suas próprias imagens de contêineres para o Docker Hub e também podem baixar imagens de contêineres de outras pessoas.

O Docker Hub é uma plataforma central para encontrar e compartilhar imagens de contêineres. Ele permite que os desenvolvedores compartilhem imagens de contêineres publicamente ou as mantenham privadas, exigindo autenticação para acessá-las. O Docker Hub também fornece recursos para integração contínua e entrega contínua (CI/CD) e colaboração em equipe.

Os desenvolvedores podem usar o Docker Hub para hospedar suas próprias imagens de contêineres ou podem usar as imagens públicas disponíveis no registro para executar aplicativos. Ao usar imagens de contêineres do Docker Hub, os desenvolvedores podem reduzir o tempo e o esforço necessários para configurar um ambiente de desenvolvimento ou produção, pois as imagens contêm tudo o que é necessário para executar o aplicativo, incluindo o sistema operacional, bibliotecas e dependências.

O Docker Hub é uma plataforma importante para a comunidade de contêineres, pois ajuda a promover a adoção de contêineres ao fornecer uma maneira fácil de compartilhar e distribuir imagens de contêineres.

repositório onde estão as imagens dos ambientes rodando determinada aplicação. <https://hub.docker.com/search?q=mysql>

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

    > docker container ls [option]: mostra os conteiners em execução
        [-a] : mostra containers que já não estão mais em execução também
    > docker container create [option] <image>: cria um container da imagem especificada sem executá-lo
    > docker container run [option] <image>: cria um container da imagem especificada e executa
        [-ti] : roda como terminal com interatividade
        [-d] : roda como daemon
        [-m] : especifica uma quantidade de memória que pode ser utilizada pelo container (ex: 128M)
        [--cpus] : quantos % de 1 core pode ser usado (ex: 1.5 = 1 core e meio, se tiver)
        [--mount type={type},src=<path source>,dst=<path destiny>,[ro]] : torna arquivos do container persistentes, ainda que o container seja apagado.
            {bind} : conecta a pastas fora da pasta docker
            {volume} : conecta a arquivos específicos dentro da pasta /var/lib/docker/volumes (ex: type=volume,src=volume1,dst=/volume1)
            [ro] : faz o mount ser do tipo "read only", o que impede alterações  
    > docker container attach <container_id> : entra no container
    > exit : sai de dentro do container
    > docker container exec [option] <container_id> {command}: faz ações dentro do container
        [-ti]
    > docker container stop <container_id> : para o container especificado
    > docker container star <container_id> : recomeça o container especificado
    > docker container restart <container_id> : reinicia o container especificado
    > docker container pause <container_id> : trava o container especificado
    > docker container unpause <container_id> : destrava o container especificado
    > docker container inspect <container_name> : dá as informações do container especificado
    > docker container logs -f <container_id> : mostra todos os logs do container
    > docker container rm [option] <container_id> : apaga o container
        [-f] : executa forçadamente
    > docker rm -f $(docker ps -aq) : Remove todos os containers (parados e em execução)    
    > docker container stats <container_id> : mostra o gasto de cpu, memória e etc do containers (se não informar o container, mostra de todos)
    > docker container top <container_id> : mostra os processos do container
    > docker container update [options] <container_id> : atualiza configuração do container
    > docker container prune -f : Remove todos os containers parados
    
    > docker kill <id_container> : força a parada do container
    > docker kill $(docker ps -q) : Remove todos os containers em execução

    
    > docker network prune -f : Remove todas as redes não utilizadas
    
    > docker volume create <volume_name> : cria volume persistente na pasta /var/lib/docker/volumes
    > docker volume ls : lista volumes
    > docker volume inspect <volume_name> : 
    > docker volume prune -f : Remove todos os volumes não utilizados

    > docker image build [option] <image_name> .
        [-t name:version] : cria tags para imagem (ex: -t app_name:1.0)
        . : indica que o Dockerfile está nesse nível
    > docker image ls : lista as imagens na máquina
    > docker image tag <image_id> tag:tag : muda tags da imagem especificada
    > docker image prune -f : Remove todas as imagens
    > docker container prune --force --filter "label!=com.docker.stack.namespace" : Remove containers órfãos (não associados a nenhum serviço ou stack)

## Dockerfile

Arquivo utilizado na hora da criação do container via docker image build.

- FROM : Define a imagem de origem para a construção da nova imagem. Por exemplo, FROM ubuntu:latest.
- LABEL : Define metadados para a imagem. Por exemplo, LABEL version="1.0" maintainer="Meu nome".
- ENV : Define variáveis de ambiente para o container. Por exemplo, ENV PORT=8080.
- RUN : Executa comandos durante a construção da imagem. Por exemplo, RUN apt-get update && apt-get install -y nginx.
- CMD : Define o comando padrão a ser executado quando o container for iniciado. Por exemplo, CMD ["nginx", "-g", "daemon off;"].
- EXPOSE : Expõe uma porta do container para a rede host. Por exemplo, EXPOSE 80.
- VOLUME : Cria um ponto de montagem para armazenar dados persistentes. Por exemplo, VOLUME /var/lib/mysql.
- ENTRYPOINT : Define o comando principal do container. Por exemplo, ENTRYPOINT ["java", "-jar", "myapp.jar"].
- COPY : Copia um arquivo ou diretório do host para o container. Por exemplo, COPY app.jar /app/.
- ADD : Similar ao COPY, mas permite a extração de arquivos compactados no processo. Por exemplo, ADD app.tar.gz /app/.
- USER : Define o usuário padrão a ser usado dentro do container. Por exemplo, USER nginx.
- ARG : Define variáveis que podem ser passadas para o Dockerfile na linha de comando. Por exemplo, ARG VERSION=latest.
- WORKDIR : Define o diretório de trabalho para os comandos subsequentes no Dockerfile. Por exemplo, WORKDIR /app.
- HEALTHCHECK : Define um comando para verificar se o container está saudável. Por exemplo, HEALTHCHECK CMD curl --fail http://localhost:8080/ || exit 1.
- SHELL : Define o shell padrão a ser usado para execução dos comandos no Dockerfile. Por exemplo, SHELL ["/bin/bash", "-c"].
- STOPSIGNAL : Especifica o sinal que deve ser enviado para o processo principal quando o container for parado. Por exemplo, STOPSIGNAL SIGTERM.
- MAINTAINER : Define o nome e o endereço de email do mantenedor da imagem. Por exemplo, MAINTAINER "Meu nome" meu.email@exemplo.com.
- ONBUILD : Especifica um comando a ser executado em uma imagem filha após a construção da imagem atual. Por exemplo, ONBUILD COPY . /app/.
- LABEL-schema : Uma convenção para definir metadados sobre a imagem. Por exemplo, LABEL-schema.version="1.0" LABEL-schema.maintainer="Meu nome".
