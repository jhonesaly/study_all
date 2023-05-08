# 12 Factories

"12 Factor" é um conjunto de práticas recomendadas para construir aplicativos modernos que são escaláveis, resilientes e fáceis de manter, recomendadas para desenvolvimento de software em nuvem. Essas práticas foram desenvolvidas por Adam Wiggins e seus colegas na Heroku em 2011, se tornaram uma referência no desenvolvimento de aplicativos.

As doze práticas descritas pelos "12 Factor" são:

- Codebase: O código da aplicação deve ser armazenado em um sistema de controle de versão e deve existir apenas uma única versão principal (main).
- Dependencies: Todas as dependências da aplicação devem ser declaradas explicitamente e isoladas das dependências do sistema operacional subjacente.
- Config: As configurações da aplicação devem ser armazenadas em variáveis de ambiente e nunca devem ser codificadas no código da aplicação.
- Backing services: Os serviços de suporte, como bancos de dados, filas e caches, devem ser tratados como recursos anexos e serem configurados por meio de variáveis de ambiente.
- Build, release, run: A construção, o empacotamento e a execução da aplicação devem ser separados e claramente definidos.
- Processes: Cada processo deve ser tratado como descartável e deve ser iniciado sem estado.
- Port binding: As aplicações devem ser autocontidas e exportar serviços por meio de portas.
- Concurrency: As aplicações devem ser projetadas para serem escalonadas horizontalmente, ou seja, adicionando mais instâncias em vez de aumentar a capacidade de cada instância.
- Disposability: As aplicações devem ser projetadas para iniciar rapidamente e encerrar sem problemas.
- Dev/prod parity: O ambiente de desenvolvimento deve ser o mais semelhante possível ao ambiente de produção.
- Logs: As aplicações devem emitir logs em formato padrão para facilitar a depuração e a análise.
- Admin processes: As tarefas administrativas, como a execução de migrações de banco de dados, devem ser executadas por meio de processos isolados e gerenciados.

As principais questões que podem ser cobradas em uma prova sobre as "12 Factor" incluem:

- O que são as "12 Factor"?


- Qual é o objetivo delas?


- Quais são os benefícios de seguir?


- Quais são as doze práticas que compõem as "12 Factor"?


- Como a prática "Config" é implementada em um aplicativo em nuvem?


- Por que a configuração deve ser armazenada em variáveis de ambiente, em vez de ser codificada no código da aplicação?


- Como os 12 Factor abordam a portabilidade de aplicativos em nuvem?


- Por que a prática "Backing services" é importante para aplicativos em nuvem?


- Como a prática "Dev/prod parity" ajuda a reduzir problemas em produção?


- Como os 12 Factor abordam a escalabilidade horizontal de aplicativos em nuvem?


- Por que a prática "Disposability" é importante para a escalabilidade de aplicativos em nuvem?


- Qual é o papel da prática "Logs" na operação de aplicativos em nuvem?


- Como a prática "Admin processes" ajuda a manter aplicativos em nuvem saudáveis?


- Como os 12 Factor lidam com a separação de processos para tarefas administrativas?


- Como as práticas recomendadas dos 12 Factor podem ser aplicadas a diferentes tipos de aplicativos em nuvem?


