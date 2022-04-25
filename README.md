# Gods Unchained Cards Analyzer
![tests](https://github.com/ericvenarusso/gods_unchained_card_analyzer/actions/workflows/tests.yaml/badge.svg?branch=main)
[![Gitter](https://badges.gitter.im/gods-unchained-cads-analyzer/gods-unchained-card-analyzer.svg)](https://gitter.im/gods-unchained-cads-analyzer/gods-unchained-card-analyzer?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)

Uma API  que classifica a estratégia de um card a partir de seus atributos.

<img src="images/gods_unchained.jpeg" width=600 height=350></img>

## Motivação
Recentemente acabei encontrando um jogo de cartas chamado [Gods Unchained](https://godsunchained.com/) e decidi participar de um campeonato. Para me preparar para a competição decidi treinar um modelo de machine learning que faz a classificação das cartas a partir de seus atributos (mana, attack, health).

A classificação das cartas é feita em:
* **early**: Cards que são mais forte nos primeiros turnos do jogo.
* **late**: Cards que são mais fortes nos turnos finais do jogo.

## Instalação
Este código é executado usando Docker e Docker compose. Caso você não tenha instalado em sua máquina, você pode acessar os links abaixo que contém um guia de instalação.
* [Docker](https://docs.docker.com/get-docker/)
* [Docker Compose](https://docs.docker.com/compose/install/)

## Execução
O Projeto é divido em dois principais componentes.
* **Train**: Aplicação que permite realizar o treino do modelo de machine learning utilizado no projeto de forma iterativa utilizando o framework Hydra.
* **API**: Aplicação REST que permite realizar a classificação da estratégia do card a partir de seus atributos.

### Train
A etapa de treinamento do modelo foi construida com o objetivo de ser reprodutivel e parametrizavel, assim evitando qualquer manutenção trabalhosa no código. 
Para isso foi utilizado o framework [Hydra](https://hydra.cc/), que permite que configurações sejam passadas por arquivos de configuração ou parâmetros.

**Por padrão já existe um [modelo treinado](models/card_analyzer.pkl) salvo no repositório.**

Para começar o processo de execução é necessário realizar o build da imagem Docker.
```console
docker build -t card_analyzer_train -f docker/train/Dockerfile .
```

Para realizar a execução da etapa de treinamento, você deve executar.
```console
docker run -v $(pwd)/models:/usr/src/app/models card_analyzer_train
```

Por padrão as configurações do treinamento estão sendo consumidas a partir de um [arquivo de configuração](config/train/config.yaml), caso você deseje alterar alguma configuração sem re-buildar a imagem, você pode passar como parâmetro.

Exemplo:
```console
docker run -v $(pwd)/models:/usr/src/app/models card_analyzer_train python trainer.py machine_learning.model.bootstrap=False machine_learning.model.n_jobs=2
```
Ao final da execução o modelo será salvo na pasta **/models** local substituindo o modelo default.

### API
A aplicação REST foi construida utilizando o framework [Fast API](https://fastapi.tiangolo.com/) e o banco de dados [MongoDB](https://www.mongodb.com/) que armazena o historico de requisições.

#### Rotas:
* **/healthcheck (GET)** - Retorna o status de saúde da API.
* **/predict (POST)** - Realiza a classificação da estratégia do Card e grava a requisição no banco de dados.
* **/cards_analyzed (GET)** - Retorna 100 registros de Cards que foram previamente classificados.

Para realizar a subida da API e do banco de dados, você deve executar.

```console
docker compose up --build
```

Após os serviços terem subido, você pode acessa-los em:
* [Cards Analyzer API](https://localhost:8000)
* [Cards Analyzer API - Swagger](https://localhost:8000/docs)

Caso você deseje desligar os serviços, você deve executar.
```console
docker compose down
```
## Arquitetura
Você pode encontrar uma referência de arquitetura do projeto no [link](https://docs.google.com/presentation/d/15iem7jYjGmS4Z7g4uNOSbmQ3femrCAIjej23FKqL0ms/edit?usp=sharing).

## Licensa, Autores, e Agradecimentos.
Eric Buzato Venarusso
