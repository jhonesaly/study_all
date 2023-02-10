#!/bin/bash

echo "Criando diretórios..."

mkdir /publico
mkdir /adm
mkdir /ven
mkdir /sec

echo "Criando grupos de usuários..."

groupadd GRP_ADM
groupadd GRP_VEN
groupadd GRP_SEC

echo "Criando usuários..."

useradd carlos -c "Carlos" -m -s /bin/bash -p $(openssl passwd -6 123)
useradd maria -c "Maria" -m -s /bin/bash -p $(openssl passwd -6 123)
useradd joão -c "João" -m -s /bin/bash -p $(openssl passwd -6 123)

useradd debora -c "Debora" -m -s /bin/bash -p $(openssl passwd -6 123)
useradd sebastiana -c "Sebastiana" -m -s /bin/bash -p $(openssl passwd -6 123)
useradd roberto -c "Roberto" -m -s /bin/bash -p $(openssl passwd -6 123)

useradd josefina -c "Josefina" -m -s /bin/bash -p $(openssl passwd -6 123)
useradd amanda -c "Amanda" -m -s /bin/bash -p $(openssl passwd -6 123)
useradd rogerio -c "Rogerio" -m -s /bin/bash -p $(openssl passwd -6 123)

echo ("Adicionando usuários aos grupos...")