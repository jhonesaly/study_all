# Instalação do Linux

Existem 3 formas de utilizar o linux

## Instalando via WSL

Se seu PC é um Windows 10, provavelmente ele vem com suporte a WSL. Para usar o prompt do linux no Windows, basta abrir o prompt do windows e seguir:

    >wsl --install

    O Subsistema do Windows para Linux já está instalado.
    Veja a seguir uma lista de distribuições válidas que podem ser instaladas.
    Instalar usando 'wsl.exe --install <Distro>'.

    NAME               FRIENDLY NAME
    Ubuntu             Ubuntu
    Debian             Debian GNU/Linux
    kali-linux         Kali Linux Rolling
    SLES-12            SUSE Linux Enterprise Server v12
    SLES-15            SUSE Linux Enterprise Server v15
    Ubuntu-18.04       Ubuntu 18.04 LTS
    Ubuntu-20.04       Ubuntu 20.04 LTS
    Ubuntu-22.04       Ubuntu 22.04 LTS
    OracleLinux_8_5    Oracle Linux 8.5
    OracleLinux_7_9    Oracle Linux 7.9

    >wsl --install -d ubuntu
    
    Instalando: Ubuntu
    Ubuntu já foi instalado.
    Iniciando: Ubuntu

## Usando Virtual Machine

Se por um acaso o método anterior não der certo, você pode instalar o Oracle VM virtual Machine, baixar uma ISO de distro linux e rodá-lo em uma máquina virtual. Existem várias tutorias na internet que outro dia detalharei. Importante fazer a verificação do ISO baixada. Para tal, siga as informações do aquivo "ISOvalidation.md".

## Instalando o Linux no HD

A melhor forma e que garante o melhor desempenho é instalando o Linux na máquina. Farei esse método em breve, quando conseguir liberar espaço no PC ou aumentar o HD.