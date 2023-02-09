# Verificação de Integridade e Autenticidade da ISO do Linux Mint

A verificação da integridade e autenticidade de arquivos ISO é uma prática importante para garantir que o arquivo baixado é o original e não foi alterado. No caso do Linux Mint, a equipe fornece dois arquivos para verificação: sha256sum.txt e sha256sum.txt.gpg.

Para garantir a integridade e autenticidade da imagem ISO do Linux Mint, é necessário seguir alguns passos, **executando os comandos na pasta onde se encontra a ISO**.

## Verificação de Integridade

- Baixe os arquivos sha256sum.txt e a ISO do Linux Mint (<https://linuxmint.com/edition.php?id=304>).
- Abra o Prompt de Comando do Windows e navegue até o local onde os arquivos foram baixados.
- Use o comando certutil -hashfile nome_da_iso.iso SHA256 para gerar o hash da ISO baixada.
- Abra o arquivo sha256sum.txt e compare o hash gerado com o hash listado no arquivo. Se forem iguais, a integridade do arquivo foi confirmada.

No prompt:

    input:
    C:\Users\Cougar_Gamer\Desktop\linux-study\verification>certutil -hashfile linuxmint-21.1-xfce-64bit.iso SHA256
    
    output:
    SHA256 hash of linuxmint-20-cinnamon-64bit.iso:
    6fea221b5b0272d55de57f3d31498cdf76682f414e60d28131dc428e719efa8b
    CertUtil: -hashfile command completed successfully.

## Verificação da Autenticidade

- Faça o download e instale o GPG4win no seu computador <https://www.gpg4win.org/get-gpg4win.html>.
- Abra o prompt de comando (se já estiver aberto, precisa reiniciar o prompt para carregar a nova biblioteca) e execute o comando gpg --keyserver hkp://keyserver.ubuntu.com:80 --recv-key "27DE B156 44C6 B3CF 3BD7 D291 300F 846B A25B AE09" para importar a chave de assinatura do Linux Mint.
- Utilize o comando gpg --verify sha256sum.txt.gpg sha256sum.txt para verificar a assinatura do arquivo sha256sum.txt.
- Se o resultado for "Good signature", a assinatura é válida e o arquivo não foi alterado. Caso contrário, não confie na imagem ISO.
- É importante lembrar que esta chave não está certificada com uma assinatura confiável e não há indicação de que a assinatura pertence ao dono. 

No prompt:
    input:
    C:\Users\Cougar_Gamer\Desktop\linux-study\verification>gpg --keyserver hkp://keyserver.ubuntu.com:80 --recv-key "27DE B156 44C6 B3CF 3BD7  D291 300F 846B A25B AE09"
    
    output:
    gpg: key 300F846BA25BAE09: public key "Linux Mint ISO Signing Key <root@linuxmint.com>" imported
    gpg: Número total processado: 1
    gpg:               importados: 1

    input:
    C:\Users\Cougar_Gamer\Desktop\linux-study\verification>gpg --verify sha256sum.txt.gpg sha256sum.txt
    
    output:
    gpg: Signature made 18/12/2022 09:54:36 Hora oficial do Brasil
    gpg:                using RSA key 27DEB15644C6B3CF3BD7D291300F846BA25BAE09
    gpg: Good signature from "Linux Mint ISO Signing Key <root@linuxmint.com>" [unknown]
    gpg: AVISO: Esta chave não está certificada com uma assinatura confiável!
    gpg:          Não há indicação de que a assinatura pertence ao dono.
    Impressão da chave primária: 27DE B156 44C6 B3CF 3BD7  D291 300F 846B A25B AE09

Em resumo, esses passos garantem que a imagem ISO do Linux Mint baixada é autêntica e não foi alterada, garantindo uma instalação segura e confiável.