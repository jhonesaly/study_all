#!/bin/bash

printf "\nIniciando protocolo new_iac..."

printf "\nEm caso de dúvida, consulte a documentação disponível em ...\n"

while true; do

    read -n 1 -p "Deseja que o programa siga estritamente aquilo que foi proposto no projeto? [y/n] " answer_1

    if [ "$answer_1" == "e" ]; then
        printf "\nFinalizando...\n"
        break

    elif [ "$answer_1" == "y" ]; then
        printf "\nSeguindo para protocolo simplificado...\n"
        # Caminho do new_iac1a.sh 
        ./.new_iac1a.sh
        break
        
    elif [ "$answer_1" == "n" ]; then
        printf "\nSeguindo para protocolo avançado...\n"
        # Caminho do new_iac1b.sh
        ./.new_iac1b.sh
        break
        
    else
        printf "\nOpção inválida. Por favor, escolha 'y' para sim, 'n' para não ou 'e' para sair.\n"
        continue
    fi

done

# ---

printf "\nFinalizado.\n"