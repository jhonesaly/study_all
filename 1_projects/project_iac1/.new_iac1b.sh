#!/bin/bash

# ---
# Chama o script que exclui antigos diretórios, arquivos, grupos e usuários anteriores

while true; do
    read -n 1 -p "\nDeseja apagar todos os diretórios, grupos e usuários anteriores? [y/n] \n" ans_b1
    if [ $ans_b1 = "y" ]; then
        ./modules/exclude_past_gud.sh
        break
    elif [ $ans_b1 = "n" ]; then
        break
    else
        echo "\nDigite um comando válido.\n"
        continue
    fi
done

# ---
# Chama o script que criar novos diretórios, grupos e usuários
while true; do
    read -n 1 -p "\nDeseja Deseja criar novos diretórios, grupos e usuários anteriores? [y/n] " ans_b2
    if [ $ans_b2 = "y" ]; then
        ./modules/create_new_gud.sh
        break
    elif [ $ans_b2 = "n" ]; then
        break
    else
        echo "\nDigite um comando válido.\n"
        continue
    fi
done

# ---
