# Previsão de Vendas de Sorvete com Machine Learning 🍦

## Descrição

Este projeto tem como objetivo prever as vendas diárias de sorvetes com base na temperatura do dia utilizando técnicas de **Machine Learning**. O modelo desenvolvido é uma **regressão linear**, que prevê quantos sorvetes serão vendidos dependendo da temperatura ambiente. Isso ajuda donos de sorveterias a otimizar a produção, evitando desperdícios e maximizando os lucros.

O projeto é baseado na ideia de uma **sorveteria chamada Gelato Mágico**, localizada em uma cidade litorânea, onde a venda de sorvetes tem uma forte correlação com a temperatura do dia.

## Objetivos

- **Treinar um modelo de Machine Learning** para prever as vendas de sorvetes com base na temperatura do dia.
- **Registrar e gerenciar o modelo** utilizando o **MLflow**.
- **Implementar previsões em tempo real**, simulando um ambiente de produção.
- **Estruturar o código em um pipeline** que garanta a reprodutibilidade dos resultados.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação utilizada.
- **Pandas**: Manipulação e análise de dados.
- **Scikit-learn**: Para construir o modelo de regressão linear.
- **MLflow**: Para registrar e gerenciar o modelo de Machine Learning.
- **Jupyter Notebooks/VS Code**: Para desenvolvimento e execução do código.
- **GitHub**: Para versionamento do código e compartilhamento do projeto.

## Estrutura do Repositório

```plaintext
├── inputs/                   # Pasta contendo os dados de entrada (CSV)
│   └── dados_sorvete.csv      # Dados de temperatura e vendas
├── modelo.py                  # Código para treinamento do modelo de ML
├── previsao_temperatura.py    # Código para fazer previsões de vendas
├── requirements.txt           # Dependências do projeto
├── README.md                 # Documento de descrição do projeto
└── .gitignore                 # Arquivos para ignorar no Git
