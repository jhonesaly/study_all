# Definir dono das pastas

## Mudar dono de todos os diretórios criados para root
sudo chown -R root:root /publico
sudo chown -R root:root /adm
sudo chown -R root:root /ven
sudo chown -R root:root /sec

## Conceder permissões a todos os usuários dentro do diretório publico
sudo chmod -R 777 /publico

## Conceder permissões aos usuários dentro de seus respectivos diretórios
sudo chmod -R 770 /adm
sudo chmod -R 770 /ven
sudo chmod -R 770 /sec
