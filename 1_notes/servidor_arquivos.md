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

