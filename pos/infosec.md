# Segurança da informação

## Órgãos responsáveis pela elaboração de padrões

- National Institute of Standads and Technology (NIST)
- Internet Society (ISOC)
- The International Telecommunication Union (ITU)
- International Organization for Standardization (ISO)

## Conceitos

Objetivo da segurança da informação é preservar a integridade, a disponibilidade e a confidencialidade dos recursos do sistema de informação

- Confidencialidade: A confidencialidade garante que as informações sejam acessíveis somente a pessoas autorizadas e que tenham a necessidade de conhecê-las. Isso implica em proteger os dados contra o acesso não autorizado, vazamentos ou divulgação inadequada.
- Integridade: A integridade diz respeito à garantia de que as informações sejam precisas, completas e consistentes, e que não sejam alteradas de forma não autorizada. Isso envolve proteger os dados contra modificações não autorizadas, corrupção ou destruição acidental.
- Disponibilidade: A disponibilidade garante que as informações estejam disponíveis e acessíveis quando necessário, para as pessoas autorizadas. Isso envolve garantir que os sistemas e recursos de tecnologia da informação estejam funcionando adequadamente, protegidos contra falhas e indisponibilidade.
- Autenticidade: A autenticidade assegura que as informações sejam provenientes de fontes confiáveis e que sejam genuínas. Isso envolve a verificação da identidade dos usuários, sistemas e recursos envolvidos no processamento e transmissão de informações.
- Não repúdio: O não repúdio garante que as ações realizadas por usuários ou sistemas sejam irrefutáveis, ou seja, não possam ser negadas posteriormente. Isso envolve a utilização de mecanismos de registro e rastreamento de atividades para provar a autoria e ação realizada.
- Conformidade: A conformidade refere-se ao cumprimento de leis, regulamentações, políticas, normas e diretrizes aplicáveis à proteção de informações. Isso envolve garantir que as práticas de segurança da informação estejam alinhadas com os requisitos legais e regulatórios aplicáveis.

### Confidencialidade x Privacidade

Em resumo, a confidencialidade está mais relacionada à proteção de informações sensíveis em geral, enquanto a privacidade está mais relacionada à proteção das informações pessoais de um indivíduo em específico, e aos direitos e controle que esse indivíduo tem sobre suas próprias informações. Ambos os conceitos são importantes na área de segurança da informação e são utilizados para garantir a proteção adequada dos dados e da privacidade das pessoas.

## Níveis de impacto

Os níveis de impacto de segurança são uma abordagem usada para avaliar a gravidade dos efeitos potenciais de uma violação de segurança da informação. Esses níveis são geralmente usados para classificar a gravidade dos riscos ou ameaças associados à confidencialidade, integridade e disponibilidade das informações. Os três níveis de impacto de segurança comuns são:

- Baixo impacto: Um incidente de baixo impacto geralmente tem um efeito limitado nas operações e nos ativos de informação de uma organização. Pode envolver a exposição de informações de baixa sensibilidade, com um impacto mínimo na confidencialidade, integridade ou disponibilidade dessas informações. Pode ser uma violação de segurança isolada que é corrigida facilmente sem causar grandes danos ou interrupções significativas nos negócios ou serviços.
- Moderado impacto: Um incidente de moderado impacto pode ter um efeito mais significativo nas operações e nos ativos de informação de uma organização. Pode envolver a exposição de informações sensíveis, com potencial para afetar a confidencialidade, integridade ou disponibilidade dessas informações em maior escala. Pode requerer uma resposta mais extensa e ações corretivas mais significativas para mitigar os efeitos e restaurar a segurança das informações afetadas.
- Alto impacto: Um incidente de alto impacto é considerado grave e pode ter consequências significativas para as operações e ativos de informação de uma organização. Pode envolver a exposição de informações altamente sensíveis, com um impacto grave na confidencialidade, integridade ou disponibilidade dessas informações. Pode resultar em interrupções significativas nos negócios, danos financeiros, danos à reputação e/ou consequências legais ou regulatórias graves. A resposta a um incidente de alto impacto pode exigir uma ação imediata e abrangente para conter os danos e restaurar a segurança das informações afetadas.

A avaliação do nível de impacto de segurança é importante para priorizar ações de resposta a incidentes, alocar recursos adequados, estabelecer políticas de segurança apropriadas e tomar decisões informadas em relação à gestão de riscos de segurança da informação. É importante que as organizações estabeleçam critérios claros e consistentes para avaliar o impacto de segurança de forma apropriada de acordo com suas necessidades e requisitos específicos.

## Arquitetura de segurança

No contexto de arquitetura de segurança da informação, os termos "ataque", "mecanismo" e "serviço" são usados da seguinte forma:

- Ataque: Um ataque é uma ação intencional realizada por uma parte mal-intencionada para violar a confidencialidade, integridade ou disponibilidade de informações ou sistemas de informação. Os ataques podem ser de diversas naturezas, como tentativas de acesso não autorizado, exploração de vulnerabilidades de segurança, interceptação de dados, destruição de dados, entre outros. Os ataques podem ser perpetrados por hackers, crackers, malware, insiders mal-intencionados ou outras ameaças.
- Mecanismo: Um mecanismo é uma técnica, método ou procedimento utilizado para implementar a segurança em sistemas de informação. Os mecanismos são projetados para proteger as informações e os sistemas contra ataques e outras ameaças à segurança. Exemplos de mecanismos de segurança incluem autenticação (como senhas, tokens, biometria), criptografia (para proteção de dados em trânsito e em repouso), firewalls (para proteção de redes), detecção de intrusão (para identificação de atividades suspeitas), políticas de segurança (para definir diretrizes e restrições de uso), entre outros.
- Serviço: Um serviço de segurança da informação é uma funcionalidade ou recurso que é fornecido para proteger as informações e sistemas de uma organização. Os serviços de segurança da informação são projetados para garantir a confidencialidade, integridade, disponibilidade e outras características de segurança das informações. Exemplos de serviços de segurança da informação incluem gerenciamento de identidade e acesso, gestão de chaves criptográficas, monitoramento de segurança, resposta a incidentes de segurança, auditoria de segurança, entre outros.

Em resumo, no contexto de arquitetura de segurança da informação, um ataque é uma ação mal-intencionada, um mecanismo é uma técnica ou método utilizado para implementar a segurança e um serviço é uma funcionalidade ou recurso que é fornecido para proteger as informações e sistemas de uma organização. Todos esses elementos são importantes para garantir a proteção adequada das informações e a mitigação de riscos de segurança em um ambiente de segurança da informação.

### Ataques

No contexto da segurança da informação, os ataques podem ser classificados em ataque passivo e ataque ativo. Vamos explorar as definições desses conceitos:

- Ataque Passivo: Um ataque passivo é uma tentativa de acesso não autorizado ou monitoramento de informações sem alterar seu conteúdo. O objetivo principal de um ataque passivo é obter informações confidenciais sem que o detentor dessas informações saiba que elas foram acessadas. Exemplos de ataques passivos incluem a interceptação de dados em uma rede, a análise de tráfego de rede para identificar padrões de uso ou a escuta de comunicações sem fio.
- Ataque Ativo: Um ataque ativo é uma tentativa de acesso não autorizado ou alteração de informações em um sistema ou rede. Diferentemente de um ataque passivo, um ataque ativo envolve a modificação ou destruição de informações, ou a realização de ações prejudiciais em um sistema ou rede. Exemplos de ataques ativos incluem a injeção de código malicioso em um site, a manipulação de dados em uma transação, a falsificação de pacotes de rede para enganar um sistema, ou a negação de serviço (DoS) para tornar um serviço ou recurso indisponível.

Esses conceitos de ataque passivo e ataque ativo são importantes para entender as diferentes maneiras pelas quais os sistemas e informações podem ser comprometidos. Os profissionais de segurança da informação precisam estar cientes desses tipos de ataques e implementar medidas adequadas para proteger suas informações e sistemas contra ambos os tipos de ameaças.
