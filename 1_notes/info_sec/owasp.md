# OWASP

OWASP significa "Open Web Application Security Project" e é uma organização sem fins lucrativos que se concentra em melhorar a segurança de software na web. A organização fornece recursos gratuitos e abertos para ajudar desenvolvedores, profissionais de segurança e organizações a criar, desenvolver e manter aplicativos web mais seguros.

Entre os recursos disponíveis no projeto OWASP, podemos destacar a "OWASP Top 10", que é uma lista das dez principais vulnerabilidades de segurança em aplicativos web mais comuns, e o "OWASP ZAP" (Zed Attack Proxy), uma ferramenta de teste de segurança automatizada para aplicativos web.

Além disso, a OWASP promove a colaboração da comunidade de segurança em torno de projetos de código aberto, a realização de eventos de treinamento e conferências para disseminar boas práticas de segurança e a promoção de pesquisa e desenvolvimento para melhorar a segurança na web.

## Análise de Risco

A classificação de risco no OWASP é uma forma de avaliar a gravidade das vulnerabilidades encontradas em aplicativos web. Existem várias metodologias e modelos de classificação de risco, mas uma das mais conhecidas é a "Common Vulnerability Scoring System" (CVSS), que é utilizada pela OWASP e outras organizações.

O CVSS atribui uma pontuação a cada vulnerabilidade com base em três dimensões: a gravidade do impacto, a facilidade de exploração e a complexidade de atenuação. Cada dimensão é avaliada em uma escala de 0 a 10, e a pontuação final é calculada a partir de uma fórmula que leva em consideração essas três dimensões.

A pontuação final pode ser classificada em três níveis de risco: baixo, médio e alto. As vulnerabilidades com pontuação entre 0 e 3,9 são consideradas de risco baixo, aquelas entre 4 e 6,9 são consideradas de risco médio e as que possuem pontuação entre 7 e 10 são classificadas como de risco alto.

Essa classificação de risco é importante para que as organizações possam priorizar as correções de vulnerabilidades em seus aplicativos, focando nas mais críticas e que apresentam maior risco para a segurança. Além disso, a classificação de risco ajuda a orientar as equipes de desenvolvimento e segurança a tomarem as medidas necessárias para corrigir as vulnerabilidades de forma mais eficaz.

## Top 10 2021

![owasp top10](images/mapping.png)

A01:2021 - Controle de Acesso Quebrado: Este tipo de ataque ocorre quando há falhas no controle de acesso de um sistema, permitindo que um invasor acesse recursos que não deveriam estar disponíveis para ele. Isso pode permitir a execução de ações maliciosas, como roubo de informações ou modificações indevidas no sistema.

A02:2021 - Falhas Criptográficas: Esse tipo de ataque acontece quando o sistema não utiliza criptografia adequada ou quando há falhas na implementação da criptografia. Isso pode permitir que um invasor acesse informações confidenciais ou comprometa o sistema de outras maneiras.

A03:2021 - Injeção: A injeção ocorre quando um invasor consegue inserir código malicioso em um sistema através de entradas de usuário não sanitizadas, como formulários web, campos de pesquisa ou parâmetros de URL. Isso pode permitir que o invasor execute comandos não autorizados no sistema ou acesse informações confidenciais.

A04:2021 - Design Inseguro: Esse tipo de ataque ocorre quando há falhas no design do sistema, tornando-o vulnerável a outros tipos de ataques, como injeção ou quebra de controle de acesso. Isso pode acontecer quando o design do sistema não leva em consideração a segurança desde o início do processo de desenvolvimento.

A05:2021 - Configuração Insegura: Esse tipo de ataque acontece quando as configurações do sistema não são feitas adequadamente ou não são atualizadas, deixando o sistema vulnerável a ataques externos. Isso pode permitir que um invasor acesse informações confidenciais ou execute ações maliciosas no sistema.

A06:2021 - Componentes Vulneráveis e Desatualizados: Esse tipo de ataque ocorre quando o sistema utiliza componentes de software com vulnerabilidades conhecidas ou desatualizados, deixando o sistema vulnerável a outros tipos de ataques. Isso pode permitir que um invasor acesse informações confidenciais ou execute ações maliciosas no sistema.

A07:2021 - Falhas de Identificação e Autenticação: Esse tipo de ataque ocorre quando há falhas no processo de identificação e autenticação de usuários, permitindo que um invasor acesse informações ou execute ações indevidas no sistema. Isso pode acontecer quando senhas são fracas, o sistema não verifica adequadamente a identidade do usuário ou não utiliza autenticação multifator.

A08:2021 - Falhas na Integridade de Dados e Software: Esse tipo de ataque ocorre quando há falhas na validação de dados ou no processo de atualização do software, permitindo que um invasor execute ações indevidas ou comprometa o sistema de outras maneiras. Isso pode acontecer quando o sistema não verifica adequadamente as informações recebidas ou não verifica se as atualizações de software são válidas.

A09:2021 - Falhas em log e monitoramento de segurança: anteriormente intitulado "Logging & Monitoring Insufficient", este item sobe para a nona posição do ranking e foi adicionado a partir da pesquisa de mercado. Esta categoria foi expandida para incluir mais tipos de falhas, é desafiadora de testar e não é bem representada nos dados CVE / CVSS. No entanto, as falhas nesta categoria podem afetar diretamente a visibilidade, alerta de incidentes e forense.

A10:2021 - Forgery de solicitação do lado do servidor: adicionado a partir da pesquisa da comunidade, este item representa a situação em que os membros da comunidade de segurança estão nos dizendo que isso é importante, embora não seja ilustrado nos dados no momento. Os dados mostram uma taxa de incidência relativamente baixa com cobertura de teste acima da média, juntamente com classificações acima da média para potencial de exploração e impacto.

## Defesas


Existem várias formas de evitar os ataques elencados no OWASP Top 10, algumas delas são:

- Mantenha o software atualizado e corrigido - verifique regularmente se há atualizações de segurança e corrija quaisquer vulnerabilidades conhecidas.
- Use autenticação forte e controles de acesso - certifique-se de que seus usuários são autenticados e autorizados corretamente e de acordo com as práticas recomendadas.
- Proteja seus dados - use criptografia forte para proteger os dados em repouso e em trânsito.
- Faça a validação correta dos dados - garanta que a entrada do usuário seja validada e sanitizada corretamente antes de ser usada em operações críticas.
- Implemente medidas de segurança apropriadas - utilize as melhores práticas de segurança, como firewalls, IDS/IPS, monitoramento de segurança, etc.
- Eduque seus usuários - sensibilize seus usuários sobre as ameaças de segurança e as melhores práticas para proteger as informações e recursos da empresa.
- Utilize ferramentas de segurança - utilize ferramentas de segurança automatizadas para verificar periodicamente a segurança de seu sistema, tais como análise de código-fonte estática, varreduras de vulnerabilidade, etc.

Lembre-se de que a segurança não é algo que possa ser adicionado posteriormente a uma aplicação ou sistema - ela deve ser projetada e implementada desde o início do processo de desenvolvimento. Além disso, as medidas de segurança devem ser revistas e atualizadas regularmente para manter a proteção contra ameaças atuais e emergentes.
