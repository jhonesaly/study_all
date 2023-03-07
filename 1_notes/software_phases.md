# Software Release Life Cycle

Software Release Life Cycle (Ciclo de Vida da Liberação de Software) é o processo que descreve as etapas pelas quais um software passa desde o seu início até a sua retirada do mercado. O ciclo de vida da liberação de software é composto por várias fases, cada uma com seus próprios objetivos, atividades e entregas. O objetivo final do ciclo de vida da liberação de software é garantir que o software seja de alta qualidade e atenda às necessidades dos usuários.

As fases do ciclo de vida da liberação de software podem variar dependendo da metodologia de desenvolvimento de software utilizada, mas geralmente incluem as seguintes etapas:

- Planejamento: nesta fase, o objetivo é definir o escopo do software, identificar os requisitos do usuário e as metas de negócios.
- Análise: nesta fase, o objetivo é analisar os requisitos do usuário e transformá-los em requisitos técnicos.
- Projeto: nesta fase, o objetivo é criar a arquitetura do software, definir as funcionalidades, identificar os módulos do sistema e desenhar a interface de usuário.
- **Implementação**: nesta fase, o objetivo é desenvolver o software, escrevendo o código, integrando os módulos e testando o sistema.
- Teste: nesta fase, o objetivo é testar o software para garantir que ele esteja funcionando corretamente e que atenda às especificações.
- **Implantação**: nesta fase, o software é implantado em um ambiente de produção e disponibilizado para os usuários finais.
- Manutenção: nesta fase, o software é mantido e atualizado para corrigir falhas e atender às necessidades dos usuários.

## Fases de desenvolvimento

Dentro do desenvolvimento em si, que vai da Implementação até a Implantação, um software pode passar por diferentes estágios de desenvolvimento. Esses estágios geralmente incluem:

- Pre-alpha: Essa é a fase inicial de desenvolvimento, onde o software está em uma fase muito inicial de construção e não está pronto para ser testado ainda. Nessa fase, geralmente não há garantia de que o software irá funcionar como esperado e pode haver muitos bugs.
  - Nessa fase inicial de desenvolvimento, os testes podem se concentrar em verificar se o software está executando as funções básicas e se está sendo criado de acordo com as especificações. Podem ser realizados testes de unidade, testes de integração e testes de sistema para garantir que as partes individuais do software estejam funcionando corretamente.
- Alpha: Nessa fase, o software está em um estado em que pode ser testado, mas ainda não está completo. A equipe de desenvolvimento pode convidar um grupo seleto de usuários para testar o software e fornecer feedback. Ainda pode haver bugs e o software pode não ter todos os recursos planejados.
  - Nessa fase, os testes podem ser realizados em um ambiente controlado por um grupo seleto de usuários para fornecer feedback sobre o software. Os testes podem se concentrar em identificar bugs e falhas de desempenho, além de avaliar a usabilidade do software.
- Beta: Quando o software passa para a fase beta, significa que a equipe de desenvolvimento está perto de concluir o desenvolvimento do software. Nessa fase, o software é lançado para um grupo maior de usuários para testes. O objetivo é identificar problemas adicionais e garantir que o software seja estável o suficiente para uso público.
  - Nessa fase, os testes podem ser realizados em um ambiente mais amplo por um grupo maior de usuários. Os testes podem se concentrar em identificar bugs e falhas de desempenho em uma ampla gama de sistemas e dispositivos, além de avaliar a usabilidade do software.
  - Types of Beta
    - Open Beta - Open to all public customers for testing
    - Closed Beta - Restricted to selected customers for testing
- Release Candidate (RC): Um Release Candidate é uma versão do software que a equipe de desenvolvimento acredita estar completa e pronta para lançamento. Antes de lançar o software publicamente, eles podem disponibilizar uma versão RC para testes finais. Isso é feito para garantir que não haja problemas críticos que impedirão o lançamento.
  - Nessa fase, os testes finais são realizados para garantir que não haja problemas críticos que impedirão o lançamento. Os testes podem se concentrar em garantir que todos os recursos funcionem corretamente, avaliar a qualidade do código e verificar se o software está em conformidade com os padrões de segurança.
- Versão final: Finalmente, quando a equipe de desenvolvimento está satisfeita com a qualidade do software, ele é lançado oficialmente para o público como uma versão final.

Daí em diante são lançadas versões que adicionam features o corrigem bugs.

## Versionamento

Versionamento se refere à prática de atribuir uma versão única a cada versão de um software, de modo que possa ser rastreada, gerenciada e controlada adequadamente. O versionamento é importante para o gerenciamento de mudanças em um projeto de software, permitindo que os desenvolvedores saibam exatamente em que versão do software estão trabalhando e possam gerenciar as alterações e correções de forma organizada e eficiente.

Para tal, é usada a convenção de numeração major.minor.patch. Ela é comum em muitos projetos de software e é usada para indicar a evolução da versão do software ao longo do tempo. Cada parte do número representa um aspecto diferente da versão, conforme explicado a seguir:

- Major: o número principal indica uma grande mudança ou evolução do software. Isso geralmente significa que foram adicionados novos recursos, o software passou por grandes mudanças de design ou quebra de compatibilidade com versões anteriores. Ao mudar a versão principal, geralmente é necessário atualizar a documentação e notificar os usuários sobre as mudanças significativas.
- Minor: o número secundário indica uma atualização menor ou uma evolução incremental do software. Isso geralmente significa que foram adicionados novos recursos ou melhorias, mas sem quebrar a compatibilidade com versões anteriores. As atualizações da versão secundária geralmente incluem correções de bugs e melhorias de desempenho.
- Patch: o número de patch indica uma correção de bugs ou uma atualização de segurança. Isso geralmente significa que foram corrigidos problemas específicos ou vulnerabilidades de segurança. As atualizações de patch geralmente não incluem novos recursos ou mudanças significativas no software.

Ao usar a convenção major.minor.patch, cada número pode ser incrementado independentemente, dependendo da magnitude da atualização. Por exemplo, se o software estiver atualmente na versão 1.2.3 e uma nova atualização importante for lançada com novos recursos e mudanças significativas, a versão pode ser atualizada para 2.0.0. Se uma atualização menor for lançada com algumas melhorias e correções de bugs, a versão pode ser atualizada para 1.3.0. Se uma atualização de segurança for lançada para corrigir um problema específico, a versão pode ser atualizada para 1.2.4.

A convenção major.minor.patch é amplamente usada por ser clara e fácil de entender, facilitando a comunicação e a compreensão das mudanças de versão do software.

Na convenção de numeração da versão de um software, a primeira versão é geralmente 1.0.0 e o estágio pode ser indicado após o número como 4.0.0-alpha, passar para 4.0.0-beta, 4.0.0-RC

**Numerar abaixo de 0 é incomum** em convenções de numeração de versão de software. Algumas equipes de desenvolvimento podem optar por usar uma numeração abaixo de 1 para indicar que o software está em fase inicial de desenvolvimento, mas é mais comum usar uma numeração a partir de 0.1.0 ou 0.0.1.

Para indicar a porcentagem de conclusão, a numeração de versão pode incluir um número após o segundo ponto para indicar o progresso. Por exemplo, uma versão 0.1.0 pode ser seguida por 0.2.0 para indicar que o software está 20% completo.

### Versionamento no GitHub

[Versionamento com GitHub](git_github.md#versionamento)

## Distribuição

Deploy e release são termos comumente usados em projetos de software para descrever diferentes etapas do processo de entrega de software. Embora os termos sejam frequentemente usados de forma intercambiável, eles se referem a conceitos diferentes.

Deploy é o processo de implantar o software em um ambiente de produção, onde os usuários podem interagir com o software. É o processo de instalação do software em um servidor ou plataforma de hospedagem para torná-lo disponível ao público ou a um conjunto limitado de usuários finais. O deploy geralmente ocorre após os testes internos e antes da liberação do software para o público em geral.

Release é o processo de disponibilizar o software para o público em geral. É o momento em que o software é considerado "pronto para uso" e é disponibilizado para download ou acesso pelos usuários. O processo de release geralmente envolve a criação de uma nova versão do software, testes finais e a disponibilização do software em um repositório público ou em um site de download.

As fases em que o deploy e o release ocorrem variam de acordo com a metodologia de desenvolvimento de software usada. Em geral, o deploy ocorre após o teste do software em um ambiente de pré-produção ou ambiente de teste. O release ocorre após a conclusão de todos os testes e aprovação do software para ser disponibilizado ao público.

Algumas metodologias de desenvolvimento de software, como a DevOps, integram o deploy e o release como parte do processo de entrega contínua, em que as atualizações são implantadas e lançadas em um ritmo mais rápido e constante, sem a necessidade de lançamentos formais ou grandes atualizações. Nesses casos, o deploy e o release podem ocorrer em várias fases do processo de desenvolvimento, dependendo do ciclo de vida do software.
