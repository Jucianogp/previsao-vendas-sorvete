import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import mlflow
import mlflow.sklearn

# Carregar os dados
df = pd.read_csv('inputs/dados_sorvete.csv')

# Definir as variáveis independentes e dependentes
X = df[['Temperatura']]  # Variável independente (Temperatura)
y = df['Vendas']        # Variável dependente (Vendas)

# Dividir em dados de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Criar e treinar o modelo de regressão linear
model = LinearRegression()
model.fit(X_train, y_train)

# Fazer previsões
y_pred = model.predict(X_test)

# Avaliar o modelo
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

# Logar o modelo com MLflow
mlflow.start_run()
mlflow.sklearn.log_model(model, 'modelo_sorvete')
mlflow.log_metric('mean_squared_error', mse)
mlflow.end_run()
