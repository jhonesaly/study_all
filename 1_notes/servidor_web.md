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

