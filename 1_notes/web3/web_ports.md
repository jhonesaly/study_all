# Ports

As portas de rede são números de identificação atribuídos a processos de rede que permitem que eles se comuniquem com outros processos de rede em uma rede. Existem 65.535 portas TCP e UDP disponíveis para uso, mas algumas são reservadas para usos específicos e outras são comumente usadas para serviços de rede.

as portas de rede são divididas em duas categorias principais: as portas registradas (ou conhecidas) e as portas dinâmicas (ou privadas).

As portas registradas são atribuídas pela Internet Assigned Numbers Authority (IANA) e são numeradas de 0 a 1023. Essas portas são reservadas para serviços comuns de rede, como HTTP, HTTPS, FTP, SSH, Telnet, SMTP, POP3, IMAP, DNS, entre outros. As portas registradas são bem conhecidas e podem ser usadas por qualquer pessoa que deseje executar um serviço de rede nessa porta. As portas registradas também são conhecidas como portas de sistema ou portas comerciais.

As portas dinâmicas, por outro lado, são numeradas de 1024 a 65535. Essas portas são geralmente usadas por aplicativos de cliente para se comunicar com um servidor em uma porta registrada. Por exemplo, um navegador da web pode usar uma porta dinâmica para se comunicar com um servidor HTTP em uma porta registrada (como a porta 80). As portas dinâmicas também são conhecidas como portas privadas.

As portas dinâmicas são escolhidas pelo sistema operacional do cliente ou servidor e podem ser usadas por qualquer aplicativo que precise se comunicar com outro aplicativo na rede. Como as portas dinâmicas não são pré-atribuídas ou reservadas, elas fornecem uma camada extra de segurança, pois é improvável que um invasor conheça qual porta dinâmica um aplicativo está usando para se comunicar com outro.

Algumas fontes se referem às portas de rede entre 1024 e 49151 como portas registradas ou portas registráveis, enquanto outras fontes se referem apenas às portas de 0 a 1023 como portas registradas e chamam as portas entre 1024 e 49151 de portas registráveis ou portas de usuário.

Lista completa de portas registradas em:

<https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml?skey=2&page=1>
