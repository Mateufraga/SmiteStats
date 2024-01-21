# README

Este é um aplicativo web simples desenvolvido em Python usando o framework Flask para recuperar e exibir estatísticas do jogo Smite de um jogador específico. Ele utiliza web scraping para extrair informações do perfil do jogador no site [smite.guru](https://smite.guru).

## Funcionalidades

O aplicativo possui uma única rota (`"/"`) que renderiza uma página HTML usando o template `index.html`. As estatísticas do jogador são obtidas através da função `get_smite_stats()`, que faz uma requisição HTTP para o perfil do jogador no Smite Guru, analisa a página HTML e extrai as informações relevantes sobre os deuses jogados, incluindo o nome do deus, a taxa de KDA (Kill/Death/Assist).
