# Server

Um servidor, em informática, é um computador ou um sistema de computação que fornece serviços para outros dispositivos e programas, conhecidos como clientes. Esses serviços podem ser diversos, incluindo armazenamento e gerenciamento de arquivos, acesso a recursos de rede, hospedagem de sites e aplicativos, processamento de dados, entre outros. Os servidores são projetados para serem confiáveis, seguros e escaláveis, para lidar com grandes volumes de solicitações de clientes simultâneas. Eles geralmente operam em sistemas operacionais de servidor específicos, como o Windows Server ou o Linux, e podem ser executados em hardware dedicado ou em nuvem.

## Tipos de servidor




## Remote Server

Idealmente, cada máquina é para um tipo de servidor. Claro que, em empreendimentos de menor escala, colocar tudo no mesmo aparelho é ok, mas em grandes estruturas, compensa a especialização.

# Web Server

Um web server é um software de servidor responsável por atender solicitações de clientes (navegadores da web) e entregar conteúdo web, como páginas HTML, imagens, arquivos de áudio e vídeo. Ele é responsável por receber as solicitações dos clientes por meio do protocolo HTTP, processar a solicitação e retornar a resposta apropriada.

O web server pode executar em diferentes sistemas operacionais, como Windows, Linux e Mac OS X. Ele é usado por empresas e organizações para hospedar seus sites na internet, bem como por desenvolvedores que desejam criar e testar aplicativos web em seus computadores locais. Alguns exemplos de servidores web populares são o Apache, o Nginx e o Microsoft IIS.

## Aplicações de Web Server

### Apache

O Apache HTTP Server, mais conhecido como Apache, é um servidor web de código aberto, gratuito e multiplataforma, mantido pela Apache Software Foundation. Ele foi lançado em 1995 e é um dos servidores web mais populares e amplamente usados no mundo, com mais de 50% de participação no mercado de servidores web.

O Apache é conhecido por sua estabilidade, segurança, flexibilidade e extensibilidade, suportando várias tecnologias e linguagens de programação, como PHP, Perl, Python e Ruby. Ele é executado em vários sistemas operacionais, incluindo Linux, Unix, Windows, macOS e outros. O servidor Apache é altamente configurável e pode ser personalizado para atender às necessidades específicas de diferentes aplicativos e sites da web. Ele é amplamente utilizado para hospedar sites, aplicativos da web, serviços web e outras soluções de software baseadas na web.

### NGINX

O NGINX é um servidor web de código aberto e software de proxy reverso. Ele é conhecido por sua alta performance, escalabilidade, baixo consumo de recursos e capacidade de lidar com grandes volumes de tráfego da web.

O NGINX pode ser usado para servir conteúdo estático e dinâmico da web, incluindo HTML, imagens, arquivos de estilo em cascata (CSS), arquivos de script JavaScript, APIs e muito mais. Ele também pode ser configurado para atuar como um servidor proxy reverso para redirecionar solicitações para outros servidores web ou para equilibrar a carga entre vários servidores web.

O NGINX é frequentemente usado como uma camada intermediária entre clientes e servidores web, e é comumente usado como um servidor web de front-end para aplicativos da web que usam tecnologias como Node.js, Ruby on Rails e Python.

O NGINX é amplamente utilizado em ambientes de hospedagem de sites, grandes empresas e aplicativos da web de alto tráfego. Seu uso é amplamente difundido em todo o mundo e é uma das principais opções de servidor web para muitos desenvolvedores e organizações.


# Load Test

Um "load test", ou teste de carga, é um tipo de teste de software que tem como objetivo avaliar o desempenho de um sistema quando submetido a uma carga de trabalho simulada. Esse tipo de teste é geralmente realizado em servidores, aplicativos ou sites da web, para verificar como eles se comportam em condições de uso intensivo.

Durante um teste de carga, uma grande quantidade de solicitações é enviada ao servidor ou aplicativo de destino, simulando um grande número de usuários acessando o sistema ao mesmo tempo. O objetivo é identificar os gargalos de desempenho, como tempos de resposta lentos ou falhas de servidor, que podem ocorrer quando o sistema é submetido a uma carga pesada.

Existem diversas ferramentas disponíveis para realizar testes de carga em servidores e aplicativos. Essas ferramentas geralmente permitem que os testes sejam personalizados para atender às necessidades específicas de cada sistema, definindo o número de usuários simulados, as ações que devem ser executadas e as condições de teste.

Após a realização do teste, é feita uma análise dos resultados, que geralmente inclui métricas como tempo de resposta médio, número de solicitações bem-sucedidas e número de erros. Com base nesses resultados, é possível identificar os gargalos de desempenho e trabalhar em soluções para melhorar a capacidade do sistema em lidar com cargas de trabalho pesadas.

Em resumo, o teste de carga é uma importante etapa no processo de desenvolvimento e manutenção de sistemas, pois permite identificar e corrigir problemas de desempenho antes que eles afetem a experiência do usuário final.

## Principais ferramentas de teste

Existem várias ferramentas gratuitas que você pode usar para fazer teste de estresse em contêineres em um servidor Ubuntu. Aqui estão algumas opções:

- Docker Bench for Security - É uma ferramenta de código aberto da Docker que verifica a segurança do seu ambiente Docker e fornece sugestões para melhorias. Ele pode ser usado para testar a segurança dos contêineres em seu ambiente.
- Apache JMeter - É uma ferramenta de teste de carga de código aberto que pode ser usada para testar a capacidade de resposta e desempenho dos seus aplicativos. Ele pode ser usado para testar contêineres e serviços em um cluster de contêineres.
- Siege - É uma ferramenta de teste de carga de código aberto que permite simular múltiplos usuários acessando um servidor web. Ele pode ser usado para testar contêineres que executam aplicativos web.
- Vegeta - É uma ferramenta de teste de carga de código aberto que é fácil de usar e pode gerar grandes volumes de tráfego. Ele pode ser usado para testar a capacidade de resposta e desempenho de contêineres e serviços.
- Wrk - É uma ferramenta de teste de carga de código aberto que pode ser usada para testar a capacidade de resposta e desempenho de contêineres e serviços. Ele fornece uma visão detalhada das métricas de desempenho, como latência e taxa de transferência.

Essas são apenas algumas das ferramentas disponíveis para testar a capacidade de resposta e desempenho de contêineres em um servidor Ubuntu. É importante escolher a ferramenta certa para seus requisitos específicos de teste.

### Ferramentas de teste para python

Existem várias ferramentas de testes de carga de servidores que usam Python. Algumas das mais populares são:

- Locust: Uma ferramenta de código aberto para testes de carga em que os testes são definidos em Python. O Locust é fácil de usar, escalável e pode simular milhares de usuários em um único host.
- PyTest: Uma estrutura de teste em Python que pode ser usada para testes de carga. O PyTest é altamente extensível e pode ser usado com outras ferramentas de teste de carga, como o Selenium.
- Vegeta: Uma ferramenta de teste de carga baseada em linha de comando escrita em Go, mas que tem uma biblioteca em Python para processar e visualizar os resultados. O Vegeta permite testar vários endpoints e configurar diferentes taxas de requisições simultâneas.
- Tsung: Uma ferramenta de teste de carga de código aberto escrita em Erlang, mas que pode ser usada com scripts escritos em Python. O Tsung é altamente escalável e pode simular milhares de usuários simultâneos.
- Apache JMeter: **Embora seja escrita em Java**, o Apache JMeter tem um plug-in que permite escrever testes em Python. O JMeter é uma ferramenta de teste de carga muito popular e possui uma grande comunidade de usuários e suporte para vários protocolos de comunicação.

#### Locust

O Locust é uma ferramenta de teste de carga de código aberto escrita em Python. Ele foi desenvolvido para ser uma ferramenta fácil de usar e altamente escalável, permitindo que os usuários criem testes de carga para aplicativos web e serviços RESTful.

Algumas das principais características do Locust incluem:

Scripting de teste em Python: Os testes de carga podem ser definidos em Python, tornando a criação e personalização dos testes muito flexível.

Monitoramento em tempo real: O Locust exibe informações em tempo real sobre a carga de trabalho, tempo de resposta, erros e outras métricas, permitindo que os usuários acompanhem o desempenho do aplicativo em tempo real.

Escalabilidade: O Locust foi projetado para ser altamente escalável e pode lidar com um grande número de usuários simulados.

Simulação de comportamento realista do usuário: Os testes podem ser configurados para simular o comportamento de usuários reais, como o número de sessões, a frequência de acesso a determinadas páginas e o tempo de permanência no site.

Integração com sistemas de monitoramento de terceiros: O Locust pode ser integrado com sistemas de monitoramento de terceiros, como New Relic e StatsD, permitindo que os usuários monitorem a carga de trabalho e as métricas de desempenho do aplicativo.

O Locust é uma ótima opção para quem prefere usar Python para testes de carga de aplicativos. Ele é fácil de configurar e pode ser executado em diferentes ambientes, incluindo localmente ou em servidores na nuvem. Além disso, como uma ferramenta de código aberto, o Locust é gratuito e possui uma comunidade ativa de desenvolvedores que contribuem para sua evolução e suporte.

