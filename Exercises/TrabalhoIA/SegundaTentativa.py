import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Carregar os dados
df = pd.read_csv("Vigorou.csv", sep=';', encoding='ISO-8859-1')

# Definir as colunas independentes e a dependente
colunas_independentes = ["Categoria do veiculo", "Numero de passageiros", "Capacidade de porta-malas", "Possui ar-condicionado", "Tipo de cambio"]
X = df[colunas_independentes]
y = df['Valor do aluguel diário']  # Certifique-se de que esta coluna exista no seu CSV

# Codificação das variáveis categóricas
X['Categoria do veiculo'] = X['Categoria do veiculo'].map({'Intermediario': 1, 'Compacto': 2, 'SUV': 3, 'Premium': 4})
X['Possui ar-condicionado'] = X['Possui ar-condicionado'].map({'Sim': 1, 'Não': 0})
X['Tipo de cambio'] = X['Tipo de cambio'].map({'Manual': 0, 'Automático': 1})

# Normalização dos dados
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Divisão dos dados em treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Treinamento do modelo
model = LinearRegression()
model.fit(X_train, y_train)

# Interação com o usuário para coletar dados
print('=' * 40)
print('BEM VINDO AO ALUGUEL DE CARROS!')
print('=' * 40)

# Coleta de dados do usuário
c = input(f'Qual a categoria do veículo:\n 1 - Intermediario\n 2 - Compacto\n 3 - SUV\n 4 - Premium\n Escolha: ')
p = input(f'Informe o número de passageiros do veículo que pretende alugar:\n 5, 6 ou 7 passageiros\n Escolha: ')
m = input(f'Informe a capacidade do porta-malas do veículo:\n 2, 3 ou 4 malas\n Escolha: ')
a = input(f'O carro deve possuir ar condicionado:\n 1 - Sim\n 2 - Não\n Escolha: ')
cam = input(f'Qual o tipo do câmbio do carro:\n 1 - Manual\n 2 - Automático\n Escolha: ')

# Criação de um DataFrame com os dados fornecidos pelo usuário
user_data = pd.DataFrame({
    'Categoria do veiculo': [int(c)],
    'Numero de passageiros': [int(p)],
    'Capacidade de porta-malas': [int(m)],
    'Possui ar-condicionado': [int(a)],
    'Tipo de cambio': [int(cam)]
})

# Normalização dos dados do usuário
user_data_scaled = scaler.transform(user_data)

# Previsão do valor do aluguel
predicao = model.predict(user_data_scaled)
print(f'O valor estimado do aluguel diário é: R$ {predicao[0]:.2f}')
