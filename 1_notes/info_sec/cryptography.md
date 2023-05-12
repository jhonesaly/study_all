# Criptografia

Criptografia é a técnica de codificar a informação de forma que somente pessoas autorizadas possam decodificá-la. A criptografia é amplamente utilizada para proteger a confidencialidade da informação, como senhas, números de cartão de crédito e outros dados confidenciais.

## Tipos

Criptografia simétrica: Também conhecida como criptografia de chave secreta, é um método de criptografia em que a mesma chave é usada tanto para criptografar quanto para descriptografar a informação. A criptografia simétrica é mais rápida e eficiente do que a criptografia assimétrica, mas requer que a chave seja compartilhada de forma segura entre as partes.

Criptografia assimétrica: Também conhecida como criptografia de chave pública, é um método de criptografia que envolve o uso de duas chaves diferentes, uma pública e outra privada, para criptografar e descriptografar a informação. A chave pública pode ser compartilhada com qualquer pessoa, mas a chave privada deve ser mantida em segredo pelo proprietário.

Criptografia de hash: É um método de criptografia que transforma dados em um código de hash exclusivo, que é usado para verificar a integridade dos dados. A criptografia de hash é frequentemente usada em sistemas de autenticação e para garantir que a informação não tenha sido alterada.

Criptografia de ponta a ponta: É um método de criptografia em que a informação é criptografada no dispositivo do remetente e só é descriptografada no dispositivo do destinatário. Isso ajuda a garantir a privacidade e a segurança da informação, mesmo quando ela está sendo transmitida pela internet.

## Algoritmos

AES (Advanced Encryption Standard): Este é um algoritmo de criptografia simétrica amplamente utilizado que usa chaves de 128, 192 ou 256 bits para proteger a confidencialidade dos dados. É considerado um dos algoritmos mais seguros e é usado em muitos sistemas e aplicativos, incluindo o TLS/SSL, que é usado para criptografar conexões seguras na internet.

RSA: Este é um algoritmo de criptografia assimétrica que usa chaves públicas e privadas para proteger a privacidade das mensagens. Ele é amplamente utilizado em aplicativos que exigem autenticação e assinatura digital, como em certificados digitais e em criptografia de e-mail.

SHA (Secure Hash Algorithm): Este é um conjunto de algoritmos de criptografia hash usado para proteger a integridade dos dados. Eles são amplamente utilizados em aplicativos de segurança, incluindo TLS/SSL, senhas de usuário e autenticação de mensagens.

## Chaves

Uma chave de criptografia de 128 bits é uma sequência de 128 bits de comprimento, o que significa que há 2^128 possíveis chaves diferentes que poderiam ser usadas para criptografar e descriptografar dados.

Um exemplo de uma chave de criptografia de 128 bits em hexadecimal seria:

    F4B6A28D3ED8E8761BFA589ECE7C0356

Note que essa chave é representada em hexadecimal, que é uma forma de representar números em base 16, onde cada dígito representa um valor de 0 a 15. Como cada dígito hexadecimal representa 4 bits, uma chave de 128 bits teria 32 dígitos hexadecimais (32 x 4 = 128 bits).

Observe que a chave acima é apenas um exemplo e, na prática, as chaves são geradas aleatoriamente ou derivadas de uma senha ou frase de acesso, usando algoritmos de derivação de chave seguros.

Cada dígito hexadecimal representa 4 bits porque a base numérica do sistema hexadecimal é 16, o que significa que existem 16 possíveis dígitos que podem ser usados para representar valores de 0 a 15. Os dígitos do sistema hexadecimal são:

    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F

Os dígitos de 0 a 9 representam os valores de 0 a 9, enquanto os dígitos de A a F representam os valores de 10 a 15. Cada dígito hexadecimal pode ser representado por 4 bits, porque 2^4 = 16. Então, cada dígito hexadecimal representa uma combinação de 4 bits.

A contagem de 0 a 15 em bits pode ser representada em binário ou em hexadecimal, como segue:

Representação em binário:

    0000 = 0
    0001 = 1
    0010 = 2
    0011 = 3
    0100 = 4
    0101 = 5
    0110 = 6
    0111 = 7
    1000 = 8
    1001 = 9
    1010 = A
    1011 = B
    1100 = C
    1101 = D
    1110 = E
    1111 = F

Observe que cada dígito hexadecimal representa um número de 0 a 15 em decimal, que é igual a uma combinação de 4 bits em binário.
