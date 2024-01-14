# Engenharia de Prompt

A engenharia de prompt é uma abordagem utilizada em modelos de linguagem, como o GPT, para ajustar o comportamento do modelo através da manipulação dos prompts de entrada. Ao projetar prompts de maneira específica, os usuários podem influenciar as respostas do modelo, buscando resultados desejados. Essa prática envolve experimentação com a formulação de perguntas ou instruções para obter saídas mais precisas e úteis. É uma técnica valiosa para personalizar a interação com modelos de linguagem, adaptando-se às necessidades específicas de cada usuário.

## FTAE

Me [função] um [tipo_de_texto] sobre [assunto] nesse [estilo]

- Função: (escreva/resuma/traduza/crie tópicos)
- Tipo de texto: (roteiro/post para blog/artigo/poema/postagem para [rede_social])
- Assunto: (I.A, futebol, música, filme... etc)
- Estilo: (como se fosse [personalidade], como se fosse para [público_alvo], como se estivesse [sentimento])

## 3R

use os itens em {RESUMO} para compor o {ROTEIRO} seguindo as {REGRAS}.

- Resumo: refere-se a uma síntese concisa e informativa de um texto ou conceito.
- Roteiro: Envolve a elaboração de um conjunto de instruções ou passos a serem seguidos.
- Regras: São diretrizes ou princípios estabelecidos para orientar o comportamento ou processo.

{RESUMO}
[Variável1]: Nome do autor
[Variável2]: nome do destinatário

{ROTEIRO}
Olá, eu sou [Variável1] e vou ajudar [Variável2].

{REGRAS}
> Siga o {ROTEIRO} acima e substitua os emlementos entre [ ] por aqules listados em {RESUMO} acima.
