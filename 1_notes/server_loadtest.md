# Load Test

Um "load test", ou teste de carga, é um tipo de teste de software que tem como objetivo avaliar o desempenho de um sistema quando submetido a uma carga de trabalho simulada. Esse tipo de teste é geralmente realizado em servidores, aplicativos ou sites da web, para verificar como eles se comportam em condições de uso intensivo.

Durante um teste de carga, uma grande quantidade de solicitações é enviada ao servidor ou aplicativo de destino, simulando um grande número de usuários acessando o sistema ao mesmo tempo. O objetivo é identificar os gargalos de desempenho, como tempos de resposta lentos ou falhas de servidor, que podem ocorrer quando o sistema é submetido a uma carga pesada.

Existem diversas ferramentas disponíveis para realizar testes de carga em servidores e aplicativos. Essas ferramentas geralmente permitem que os testes sejam personalizados para atender às necessidades específicas de cada sistema, definindo o número de usuários simulados, as ações que devem ser executadas e as condições de teste.

Após a realização do teste, é feita uma análise dos resultados, que geralmente inclui métricas como tempo de resposta médio, número de solicitações bem-sucedidas e número de erros. Com base nesses resultados, é possível identificar os gargalos de desempenho e trabalhar em soluções para melhorar a capacidade do sistema em lidar com cargas de trabalho pesadas.

Em resumo, o teste de carga é uma importante etapa no processo de desenvolvimento e manutenção de sistemas, pois permite identificar e corrigir problemas de desempenho antes que eles afetem a experiência do usuário final.

## Principais ferramentas de teste

Existem várias ferramentas gratuitas que você pode usar para fazer teste de estresse em contêineres em um servidor Ubuntu. Aqui estão algumas opções:

- Docker Bench for Security - É uma ferramenta de código aberto da Docker que verifica a segurança do seu ambiente Docker e fornece sugestões para melhorias. Ele pode ser usado para testar a segurança dos contêineres em seu ambiente.
- Apache JMeter - É uma ferramenta de teste de carga de código aberto que pode ser usada para testar a capacidade de resposta e desempenho dos seus aplicativos. Ele pode ser usado para testar contêineres e serviços em um cluster de contêineres. **Embora seja escrita em Java**, o Apache JMeter tem um plug-in que permite escrever testes em Python. O JMeter é uma ferramenta de teste de carga muito popular e possui uma grande comunidade de usuários e suporte para vários protocolos de comunicação.
- Siege - É uma ferramenta de teste de carga de código aberto que permite simular múltiplos usuários acessando um servidor web. Ele pode ser usado para testar contêineres que executam aplicativos web.
- Vegeta - É uma ferramenta de teste de carga de código aberto que é fácil de usar e pode gerar grandes volumes de tráfego. Ele pode ser usado para testar a capacidade de resposta e desempenho de contêineres e serviços. Uma ferramenta de teste de carga baseada em linha de comando **escrita em Go**, mas que tem uma biblioteca em Python para processar e visualizar os resultados. O Vegeta permite testar vários endpoints e configurar diferentes taxas de requisições simultâneas.
- Wrk - É uma ferramenta de teste de carga de código aberto que pode ser usada para testar a capacidade de resposta e desempenho de contêineres e serviços. Ele fornece uma visão detalhada das métricas de desempenho, como latência e taxa de transferência.
- Tsung: Uma ferramenta de teste de carga de código aberto **escrita em Erlang**, mas que pode ser usada com scripts escritos em Python. O Tsung é altamente escalável e pode simular milhares de usuários simultâneos.
- Locust: Uma ferramenta de código aberto para testes de carga em que os testes são definidos em Python. O Locust é fácil de usar, escalável e pode simular milhares de usuários em um único host.
- PyTest: Uma estrutura de teste em Python que pode ser usada para testes de carga. O PyTest é altamente extensível e pode ser usado com outras ferramentas de teste de carga, como o Selenium.

Essas são apenas algumas das ferramentas disponíveis para testar a capacidade de resposta e desempenho de contêineres em um servidor Ubuntu. É importante escolher a ferramenta certa para seus requisitos específicos de teste.