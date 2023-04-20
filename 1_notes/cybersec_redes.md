# Redes

Uma rede de computadores é um conjunto de dispositivos eletrônicos, como computadores, servidores, roteadores e switches, que são interconectados para compartilhar informações e recursos. O objetivo da rede é permitir a comunicação entre esses dispositivos, permitindo a transferência de dados e a execução de tarefas em conjunto.

O enfoque em cybersecurity (ou segurança cibernética) em uma rede de computadores diz respeito à proteção desses dispositivos e dos dados que são transmitidos e armazenados na rede contra ameaças cibernéticas, como ataques maliciosos, intrusões, malware, roubo de dados, entre outros. A segurança cibernética é uma preocupação crítica em redes de computadores, uma vez que a exposição a riscos e ameaças pode resultar em danos financeiros, reputacionais e legais para organizações e indivíduos.

Uma rede de computadores segura envolve a implementação de várias medidas de segurança, como firewall, autenticação de usuários, criptografia, monitoramento de tráfego de rede, atualizações de software e políticas de acesso restrito. Além disso, a conscientização e treinamento dos usuários também são fundamentais para garantir a segurança da rede, uma vez que muitos ataques cibernéticos exploram ações humanas, como cliques em links maliciosos ou divulgação de informações sensíveis.

## Arquiteturas

Cliente/Servidor: É um modelo de arquitetura em que os dispositivos na rede são divididos em duas categorias principais: clientes e servidores. Os clientes são dispositivos que solicitam serviços, como computadores pessoais, smartphones ou tablets, e os servidores são dispositivos que fornecem serviços, como servidores de arquivos, servidores de impressão ou servidores de aplicativos. Os clientes solicitam serviços aos servidores, que respondem às solicitações e fornecem os recursos ou serviços necessários.

Ponto a Ponto (P2P): É um modelo de arquitetura em que os dispositivos na rede têm funções semelhantes e podem atuar tanto como clientes quanto como servidores. Cada dispositivo pode compartilhar recursos diretamente com outros dispositivos na rede, sem a necessidade de servidores dedicados. Esse modelo é comumente usado em redes de compartilhamento de arquivos, como redes de compartilhamento de arquivos peer-to-peer (P2P).

Arquitetura em Camadas: É um modelo de arquitetura em que as funções de rede são organizadas em camadas distintas, com cada camada sendo responsável por uma função específica. As camadas são interconectadas e trabalham em conjunto para fornecer serviços de rede. Um exemplo conhecido de arquitetura em camadas é o modelo OSI (Open Systems Interconnection), que é um modelo de referência usado para entender e projetar redes de computadores.

Arquitetura em Nuvem (Cloud Computing): É um modelo de arquitetura em que os recursos de computação, como armazenamento, processamento e aplicativos, são fornecidos de forma remota através da internet. Os usuários acessam esses recursos através de uma rede, geralmente a Internet, e não precisam se preocupar com a infraestrutura subjacente.

## Tipos

Rede Local (LAN - Local Area Network): É uma rede que abrange uma área geográfica limitada, como um escritório, uma empresa ou um campus universitário. É comumente usada para conectar dispositivos em uma área específica e pode ser configurada com alta velocidade e baixa latência.

Rede de Longa Distância (WAN - Wide Area Network): É uma rede que abrange uma grande área geográfica, como cidades, estados ou países. É usada para conectar redes locais em diferentes locais geográficos, geralmente usando tecnologias de telecomunicações, como linhas dedicadas, redes de satélite ou conexões de internet.

Rede de Área Global (GAN - Global Area Network): É uma rede que abrange uma grande escala geográfica, como todo o mundo, e é usada para interconectar redes de longa distância em diferentes países ou continentes. A Internet é o exemplo mais conhecido de uma GAN.

Rede sem Fio (Wireless Network): É uma rede que permite a conexão de dispositivos sem fio, como smartphones, tablets, laptops e dispositivos IoT (Internet das Coisas), utilizando tecnologias como Wi-Fi, Bluetooth, 4G/5G, entre outras.

Rede Definida por Software (SDN - Software-Defined Networking): É uma arquitetura de rede que separa o plano de controle (responsável pela tomada de decisões) do plano de dados (responsável pela transferência de dados). Isso permite uma maior flexibilidade e controle centralizado na configuração e gerenciamento da rede, tornando-a mais adaptável às necessidades de segurança cibernética.

Rede Virtual Privada (VPN - Virtual Private Network): É uma rede que utiliza a infraestrutura de uma rede pública, como a Internet, para criar uma conexão segura e criptografada entre dispositivos remotos. É frequentemente usada para acessar recursos de rede de forma segura e proteger a comunicação em ambientes de acesso remoto.

## Topologia

Topologia em Estrela: É um tipo de topologia em que todos os dispositivos em uma rede estão conectados a um dispositivo central, conhecido como hub ou switch. O hub ou switch atua como ponto central de conexão, e todos os dispositivos na rede se comunicam através dele. Se um dispositivo falhar, apenas esse dispositivo será afetado, sem impactar os demais dispositivos na rede.

Topologia em Barramento: É um tipo de topologia em que todos os dispositivos em uma rede são conectados a um único cabo, conhecido como barramento. Os dispositivos compartilham o mesmo meio de transmissão para se comunicarem. Se um dispositivo falhar ou o cabo for danificado, pode causar a interrupção de toda a rede.

Topologia em Anel: É um tipo de topologia em que os dispositivos são conectados em forma de anel, em que cada dispositivo está conectado aos dispositivos vizinhos, formando um circuito fechado. Os dados são transmitidos em uma única direção ao redor do anel até chegar ao destino correto. Se um dispositivo falhar, pode afetar a comunicação em toda a rede.

Topologia em Malha: É um tipo de topologia em que todos os dispositivos estão conectados a todos os outros dispositivos na rede, criando uma rede de conexões redundantes. Essa topologia oferece alta confiabilidade e tolerância a falhas, pois permite que os dados sejam roteados por caminhos alternativos se uma rota falhar.

Topologia em Árvore: É um tipo de topologia em que os dispositivos são organizados em uma estrutura hierárquica em forma de árvore, com um nó raiz que está conectado aos nós filhos, e assim por diante. Essa topologia é comumente usada em redes de grande escala, como redes corporativas, e permite uma maior organização e controle da rede.

## Camadas

As camadas da rede se referem à organização hierárquica dos protocolos de rede em diferentes níveis de abstração, também conhecida como modelo de referência. O modelo de referência mais comum é o Modelo OSI (Open Systems Interconnection), que é composto por sete camadas. Aqui estão as sete camadas do Modelo OSI:

Camada Física: É a camada mais baixa do modelo OSI e trata da transmissão física dos dados na rede. Ela define os padrões de transmissão de bits por meio de meios físicos, como cabos, sinais elétricos ou ondas de rádio.

Camada de Enlace de Dados: É responsável pelo controle de acesso ao meio físico, como a detecção e correção de erros na transmissão de dados, controle de fluxo e endereçamento físico (como endereços MAC em redes Ethernet).

Camada de Rede: É responsável pela transferência de dados de um nó para outro em diferentes redes. Ela lida com o roteamento de pacotes, encaminhamento de dados e controle de congestionamento.

Camada de Transporte: É responsável pelo transporte confiável e eficiente de dados entre dispositivos finais. Ela fornece serviços de transporte, como segmentação e remontagem de dados, controle de fluxo e controle de erro.

Camada de Sessão: É responsável pelo estabelecimento, manutenção e encerramento das sessões de comunicação entre dispositivos. Ela gerencia a troca de dados e estabelece a sincronização e a recuperação em caso de falhas de conexão.

Camada de Apresentação: É responsável pela tradução, compressão e criptografia dos dados, garantindo que eles estejam em um formato adequado para transmissão e compreensão pelos dispositivos finais.

Camada de Aplicação: É a camada mais alta do modelo OSI e fornece interfaces para que as aplicações de usuário possam interagir com a rede. Ela inclui protocolos específicos de aplicação, como HTTP (para a World Wide Web), SMTP (para email), FTP (para transferência de arquivos) e muitos outros.

É importante notar que nem todos os modelos de rede seguem exatamente o Modelo OSI, e alguns modelos, como o Modelo TCP/IP, têm uma abordagem diferente com um número diferente de camadas e funcionalidades. No entanto, o Modelo OSI é amplamente utilizado como uma referência padrão para entender a estrutura e a organização dos protocolos de rede em diferentes camadas.
