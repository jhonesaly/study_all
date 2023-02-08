#!/bin/bash

echo "Starting..."

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