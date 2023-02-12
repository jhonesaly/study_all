#!/bin/bash

printf "\nComeçando criação da nova infraestrutura...\n"

read -p "Digite o nome da empresa dona do sistema: " company

mkdir /${company}_directories

##v##
printf "\nCriando diretório público e configurando...\n"

mkdir /${company}_directories/public
chown root:root /${company}_directories/public
chmod 777 /${company}_directories/public

read -p "Digite o nome das equipes separadas por espaço: " -a groups

##v##
printf "\nCriando grupos, seus diretórios e configurando...\n"

for group in "${groups[@]}"; do
    mkdir /${company}_directories/$group
    groupadd GRP_${group}
    chown root:GRP_${group} /${company}_directories/$group
    chmod 770 /${company}_directories/$group
done

##v##
printf "\nCriando usuários...\n"

for group in "${groups[@]}"; do
    read -p "Digite o nome dos colaboradores da equipe ${group} separandos por espaço: " -a users
    for user in "${users[@]}"; do
        useradd ${user} -m -s /bin/bash -p $(openssl passwd -6 123) -G GRP_${group}
    done
done