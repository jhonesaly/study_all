# Remote Server

# Server linux na própria máquina (Virtual Machine)

configure a virtual machine criada para a conexão estar em modo brige, como na imagem:

![configurações de rede da VM](/images/virtualmachine1.png)

Se estiver usando windows, é necessário baixar o putty em <https://www.putty.org/>. Vá em downloads e, para facilitar, baixe o .exe (putty.exe) para sua versão adequada, provavelmente a primeira opção (64-bit x86) e não o instalador .msi.

Abra a sua virtual machine e coloque o comando 

    > ip a

no endereço enp0s3, anote o ip informado em inet

Execute o putty.exe e no campo IP adress, coloque o ip informado, como na imagem:

![putty session](/images/puttysession.png)

# Server linux na AWS

Primeiro, crie uma conta na AWS <https://aws.amazon.com/pt/> (é necessário registrar cartão de crédito, ainda que só use serviços gratuitos)

No menu "esecutar instância", clique em "executar instância"

crie um nome para o servidor e selecione o tipo de servidor e suas especificações (aqui, use uma qualificada para nível gratuito) conforme a imagem:

![criando server na aws](/images/aws1.png)

No menu par de chaves, clique em "criar nova chave", dê um nome para a mesma. Se for usar um linux para conectar ao servidor, baixe o .pem para usar o openssh. Se for usar widowns, baixe o .ppk para usar o putty. Ao clicar em "criar par de chaves", a chave sera baixada automaticamente.

Se a chave que você baixou for do tipo .pem, mas quer usar no windows (no putty), é necessário fazer o download, no mesmo site, do puttygen.exe para a versão adequada e convertê-la.

deixe a caixa "permitir tráfego SSH de " habilitada e permite "qualquer lugar"

Para acessar via putty, configure a conexão adicionando a chave conforme a imagem:

![putty session conection](/images/puttysession2.png)

Não se esqueça de, quando terminar a atividade, encerrar a instância na AWS, pois pode ser cobrado alguma tarifa por excesso de uso.


# Servidor de arquivos

Primeiramente, monte um drive separado do sistema operacional para não sobrecarregá-lo em caso de muitos acessos. Para facilitar, todos os comandos serão dados como root.

    > fdisk /dev/sdb
    > mkfs.ext4 /dev/sdb
    > mkdir disk2
    > mount /dev/sdb /disk2
    > nano /etc/fstab

add na última linha: 

/dev/sdb /disk2 ext4 defaults 0 0

    > cd /
    > cd disk2
    > mkdir publica
    > chmod 777 publica/
    > apt install samba -y
    > nano /etc/samba/smb.conf

add na última linha:

[publica]

path = /disk2/publica
writable = yes
guest ok = yes
guest only = yes

    > systemctl restart smbd
    > systemctl status smdb
    > systemctl enable smbd

Com isso, você deve ser capaz de acessar a pasta /publica por meio do seu explorador de arquivos. Para tal, use o comando 'ip a' (ex: 192.168.0.0) para descobrir o ip da máquina e então coloque no endereço:

    \\192.168.0.0\publica

# Montando Servidor web

Instalando apache

    > apt install apache2 -y
    > systemctl apache2

Nesse momento, se você colocar o ip da máquina com o apache instalado no endereço do seu navegador já verá a página do apache.

    > cd /var/www/html

Nesta path está o arquivo (index.html) que foi mostrado na página ao acessar o endereço do ip da máquina.

    > rm index.html
    > nano index.html

crie o que quiser para página inicial

Esse site já está disponível para qual quer dispositivo conectado na rede local.

para torná-lo disponível globalmente, você pode precisa de um ip público. Você pode conseguir isso por meio de uma instância na AWS.

Para habilitar o acesso na AWS, é necessário habilitar o firewall para permitir requisições HTTP. Isso é feito no menu:

    > Security Groups > Instância >  Edit inbound rules

Você pode fazer um site, por exemplo, em um ambiente controlado e depois colocá-lo dentro da pasta apache.