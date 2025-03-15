def prever_vendas(temperatura):
    # Carregar o modelo salvo
    model = mlflow.sklearn.load_model('models/modelo_sorvete')

    # Fazer a previsão
    venda_prevista = model.predict([[temperatura]])
    return venda_prevista[0]

# Testar a previsão
print(prever_vendas(30))  # Exemplo: prever vendas para 30°C
