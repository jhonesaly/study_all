# Arquitetura de software

Arquitetura de software é a estrutura fundamental ou organização de um sistema de software, que inclui seus componentes, suas interações, seus padrões e as restrições que regem o seu design e sua evolução.

Ela é a base para a construção de um sistema de software e influencia fortemente como ele é desenvolvido, testado, mantido e escalado. A arquitetura de software envolve decisões de design de alto nível, como escolher as tecnologias a serem utilizadas, decidir a divisão do sistema em módulos e definir os padrões de comunicação entre eles.

Uma boa arquitetura de software é crucial para o sucesso do projeto, pois garante que o sistema atenda aos requisitos de negócio, que seja facilmente modificável e que tenha um desempenho adequado. Além disso, uma arquitetura bem definida permite que a equipe de desenvolvimento trabalhe de forma mais eficiente e colaborativa, com uma compreensão clara de como as partes do sistema se encaixam.

Vale destacar que a arquitetura de software não é algo que possa ser definido uma vez e ser deixado de lado. Ela deve ser iterada e evoluir ao longo do tempo, acompanhando as necessidades e mudanças do negócio, tecnologia e usuários.

# Tipos de arquitetura

Monolítico: todas as funções estejam em um único processo. O desenvolvimento é mais ágil e é possível subir uma primeira versão (Minimum Viable Product, ou MVP) mais facilmente, permitindo a execução por uma equipe menor e com menos qualificação.

Baseada em microsserviços (Microservices architecture): Uma arquitetura que divide o sistema em pequenos serviços independentes, cada um executando uma função específica. Cada serviço é autônomo e pode ser atualizado, implantado e dimensionado independentemente dos outros serviços. desenvolvimento especializado de acordo com a função, que fica bem-delimitada e serve a um propósito específico. Por ser uma estrutura mais complexa, exige um maior nível de automação das implementações. Além disso, orquestrar todos os microsserviços é essencial para que tudo funcione, exigindo desenvolvedores com qualificação maior ou, ao menos, uma boa coordenação de DevOps. Esta arquitetura é utilizada em sistemas que são compostos por um conjunto de microsserviços independentes, cada um responsável por uma funcionalidade específica. Um exemplo de empresa que utiliza essa arquitetura é o Netflix, que usa microsserviços para gerenciar seu catálogo de filmes e séries.

Em camadas (layered): Uma arquitetura que organiza o sistema em camadas, em que cada camada é responsável por uma funcionalidade específica. As camadas se comunicam somente com as camadas adjacentes, criando um alto grau de modularidade. Esta arquitetura é comum em aplicativos empresariais, onde a camada de apresentação (interface do usuário) é separada das camadas de lógica de negócios e de dados. Um exemplo de aplicativo que utiliza essa arquitetura é o Microsoft Office.

Cliente-servidor (Client-server architecture): Uma arquitetura que divide o sistema em dois tipos de componentes: um cliente, que solicita serviços, e um servidor, que fornece os serviços. O cliente envia solicitações para o servidor, que processa e retorna os resultados. Esta arquitetura é utilizada em sistemas em que há uma separação clara entre o cliente (interface do usuário) e o servidor (lógica de negócios e armazenamento de dados). Um exemplo de sistema que utiliza essa arquitetura é o sistema bancário online.

Orientada a serviços (Service-oriented architecture - SOA): Uma arquitetura que se concentra na criação de serviços independentes, que podem ser reutilizados em vários aplicativos. Esses serviços podem ser acessados ​​por meio de uma interface comum, tornando o sistema altamente modular. Esta arquitetura é comum em sistemas distribuídos em que diferentes componentes se comunicam por meio de serviços web. Um exemplo de empresa que utiliza essa arquitetura é a Amazon, que utiliza serviços web como o Amazon S3 e o Amazon EC2.

Orientada a eventos (Event-driven architecture): Uma arquitetura que se concentra em eventos, como ações do usuário ou mensagens recebidas de outros sistemas. Os componentes do sistema se comunicam por meio de eventos, permitindo que o sistema seja altamente escalável e resiliente. Esta arquitetura é comum em sistemas que envolvem a troca de mensagens ou eventos entre diferentes componentes. Um exemplo de sistema que utiliza essa arquitetura é o sistema de reservas de passagens aéreas.

Baseada em contêineres (Container-based architecture): Uma arquitetura que usa contêineres para isolar e gerenciar aplicativos e serviços. Os contêineres são implantados e gerenciados em uma plataforma de orquestração de contêineres, como Kubernetes. Existem muitos softwares que usam arquitetura baseada em contêineres, como Dicker, Kubernetes, Google Cloud Platform, AWS Fargate, Microsoft Azure, Apache mesos.

# Principais bibliografias

Em camadas (Layered architecture):

- "Software Architecture in Practice" de Len Bass, Paul Clements e Rick Kazman
- "Patterns of Enterprise Application Architecture" de Martin Fowler

Cliente-servidor (Client-server architecture):

- "Distributed Systems: Principles and Paradigms" de Andrew S. Tanenbaum e Maarten Van Steen
- "TCP/IP Illustrated, Volume 1: The Protocols" de W. Richard Stevens

Orientada a serviços (Service-oriented architecture - SOA):

- "SOA Principles of Service Design" de Thomas Erl
- "Service-Oriented Architecture (SOA) For Dummies" de Judith Hurwitz e Robin Bloor

Baseada em microsserviços (Microservices architecture):

- "Building Microservices" de Sam Newman
- "Microservices Patterns: With examples in Java" de Chris Richardson

Orientada a eventos (Event-driven architecture):

- "Event-Driven Architecture: How SOA Enables the Real-Time Enterprise" de Hugh Taylor, Angela Yochem e Les Phillips
- "Building Event-Driven Microservices: Leveraging Organizational Data at Scale" de Adam Bellemare

Baseada em contêineres (Container-based architecture):

- "Kubernetes: Up and Running: Dive into the Future of Infrastructure" de Kelsey Hightower, Brendan Burns e Joe Beda
- "Docker: Up & Running: Shipping Reliable Containers in Production" de Sean P. Kane e Karl Matthias