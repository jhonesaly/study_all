#!/bin/bash

printf "\nCriando diretórios...\n"

mkdir /company

read -p "Digite o nome da empresa dona do sistema: " company

mkdir /company/${company}_publico
mkdir /company/${company}_adm
mkdir /company/${company}_ven
mkdir /company/${company}_sec

printf "\nCriando grupos de usuários...\n"

groupadd GRP_ADM
groupadd GRP_VEN
groupadd GRP_SEC

printf "\nCriando usuários e os adicionando nos grupos...\n"

useradd carlos -c "Carlos" -m -s /bin/bash -p $(openssl passwd -6 123) -G GRP_ADM
useradd maria -c "Maria" -m -s /bin/bash -p $(openssl passwd -6 123) -G GRP_ADM
useradd joão -c "João" -m -s /bin/bash -p $(openssl passwd -6 123) -G GRP_ADM

useradd debora -c "Debora" -m -s /bin/bash -p $(openssl passwd -6 123) -G GRP_VEN
useradd sebastiana -c "Sebastiana" -m -s /bin/bash -p $(openssl passwd -6 123) -G GRP_VEN
useradd roberto -c "Roberto" -m -s /bin/bash -p $(openssl passwd -6 123) -G GRP_VEN

useradd josefina -c "Josefina" -m -s /bin/bash -p $(openssl passwd -6 123) -G GRP_SEC
useradd amanda -c "Amanda" -m -s /bin/bash -p $(openssl passwd -6 123) -G GRP_SEC
useradd rogerio -c "Rogerio" -m -s /bin/bash -p $(openssl passwd -6 123) -G GRP_SEC

printf "\nEspecificando permissões dos diretórios...\n"

chown root:GRP_ADM /company/${company}_adm
chown root:GRP_VEN /company/${company}_ven
chown root:GRP_SEC /company/${company}_sec
chown root:root /company/${company}_publico

chmod 770 /company/${company}_adm
chmod 770 /company/${company}_ven
chmod 770 /company/${company}_sec
chmod 777 /company/${company}_publico