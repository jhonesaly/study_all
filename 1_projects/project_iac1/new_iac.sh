#!/bin/bash

echo "Iniciando protocolo new_iac..."

echo "Em caso de dúvida, consulte a documentação disponível em ..."

read -n 1 -p "Deseja que o programa siga estritamente aquilo que foi proposto no projeto? [y/n]" answer_1

if [ "" == ""]; then
elif [ "" == ""]; then
else

# ---
# Chama o script que exclui antigos diretórios, arquivos, grupos e usuários anteriores

./modules/exclude_past_gud.sh

# ---
# Chama o script que criar novos diretórios, grupos e usuários

./modules/create_new_gud.sh

# ---
# Chama o script que altera as permissões das novas pastas

./modules/change_mermissions.sh

# ---

echo "End"