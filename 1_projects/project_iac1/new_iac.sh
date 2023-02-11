#!/bin/bash

echo "Iniciando protocolo new_iac..."

echo "Em caso de dúvida, consulte a documentação disponível em ..."

exit = false

while [ "$exit" != true]; do

    read -n 1 -p "Deseja que o programa siga estritamente aquilo que foi proposto no projeto? [y/n]" answer_1

    if [ "$answer_1" == "e"]; then
        echo "Finalizando..."
        exit = true
        break

    elif [ "$answer_1" == "y"]; then
        echo "Seguindo para protocolo simplificado..."
        # Caminho do new_iac1a.sh 
        ./.new_iac1a.sh
        
    elif [ "$answer_1" == "n"]; then
        echo "Seguindo para protocolo avançado..."
        # Caminho do new_iac1b.sh
        ./.new_iac1b.sh
        
    else
        echo "Opção inválida. Por favor, escolha 'y' para sim, 'n' para não ou 'e' para sair."
    fi

done

# ---

echo "Finalizado"