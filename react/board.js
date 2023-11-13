const axios = require('axios');

// Defina o nome de usuário do GitHub que você deseja consultar
const username = 'username';

// Configuração básica do Axios para a API do GitHub
const axiosInstance = axios.create({
  baseURL: 'https://api.github.com',
  headers: {
    'Content-Type': 'application/json',
  },
});

// Fazendo a requisição para obter os repositórios do usuário
axiosInstance.get(`/users/${username}/repos`)
  .then(response => {
    // Manipule os dados da resposta conforme necessário
    const repositories = response.data;
    console.log(`Repositórios de ${username}:`);
    
    repositories.forEach(repo => {
      console.log(`${repo.name} - ${repo.description}`);
    });
  })
  .catch(error => {
    console.error('Erro na requisição:', error.message);
  });
