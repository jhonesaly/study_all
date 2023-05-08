# 12 Factories

"12 Factor" é um conjunto de práticas recomendadas para construir aplicativos modernos que são escaláveis, resilientes e fáceis de manter, recomendadas para desenvolvimento de software em nuvem. Essas práticas foram desenvolvidas por Adam Wiggins e seus colegas na Heroku em 2011, se tornaram uma referência no desenvolvimento de aplicativos.

As doze práticas descritas pelos "12 Factor" são:

Codebase: O código da aplicação deve ser armazenado em um sistema de controle de versão e deve existir apenas uma única versão principal (main).
Dependencies: Todas as dependências da aplicação devem ser declaradas explicitamente e isoladas das dependências do sistema operacional subjacente.
Config: As configurações da aplicação devem ser armazenadas em variáveis de ambiente e nunca devem ser codificadas no código da aplicação.
Backing services: Os serviços de suporte, como bancos de dados, filas e caches, devem ser tratados como recursos anexos e serem configurados por meio de variáveis de ambiente.
Build, release, run: A construção, o empacotamento e a execução da aplicação devem ser separados e claramente definidos.
Processes: Cada processo deve ser tratado como descartável e deve ser iniciado sem estado.
Port binding: As aplicações devem ser autocontidas e exportar serviços por meio de portas.
Concurrency: As aplicações devem ser projetadas para serem escalonadas horizontalmente, ou seja, adicionando mais instâncias em vez de aumentar a capacidade de cada instância.
Disposability: As aplicações devem ser projetadas para iniciar rapidamente e encerrar sem problemas.
Dev/prod parity: O ambiente de desenvolvimento deve ser o mais semelhante possível ao ambiente de produção.
Logs: As aplicações devem emitir logs em formato padrão para facilitar a depuração e a análise.
Admin processes: As tarefas administrativas, como a execução de migrações de banco de dados, devem ser executadas por meio de processos isolados e gerenciados.
