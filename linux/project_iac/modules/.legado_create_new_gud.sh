# Criar diretórios, grupos e usuários

# Lendo o arquivo

if [[ ! -r "config.txt" ]]; then
  echo "Não foi possível ler o arquivo config.txt"
  exit 1
fi

echo "Lendo o arquivo config.txt"

declare -A directories
declare -A groups
declare -A users

echo "diretórios: $directories"
echo "grupos: $groups"
echo "usuários: $users"

section=""
i=0

while read line; do
  echo "$line"
  if [[ $line =~ ^# ]]; then
    echo "primeiro if"
    ## Verificando se é uma linha de diretórios
    if [[ "$line" =~ "^#.*pastas.*" ]]; then
      echo "if do pastas"
      section="directories"
      i=0
    fi
  else
    if [ "$section" == "directories" ]; then
      directories[i]=$line
      i=$((i + 1))
    fi
  fi
done < config.txt

echo "diretórios: ${directories[@]}"
echo "grupos: $groups"
echo "usuários: $users"

## Criando diretórios
echo "Criando diretórios"
for dir in "${!directories[@]}"; do
    sudo mkdir -p "/$dir"
    echo "Criado $dir"
done

## Criando grupos
echo "Criando grupos"
for group in "${!groups[@]}"; do
    sudo groupadd "$group"
    echo "Criado $group"
done

## Criando usuários e adicionando a grupo
echo "Criando usuários..."
for user in "${!users[@]}"; do
    sudo useradd $user
    group=$(getent group ${groups[${users[$user]}]} | awk -F: '{print $1}')
    sudo usermod -aG $group $user
    echo "Criado $user"
done