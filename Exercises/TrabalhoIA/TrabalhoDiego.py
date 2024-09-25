print('=' * 40)
print('BEM VINDO AO ALUGUEL DE CARROS!')
print('=' * 40)

c = ' '
while c not in '123':
    c = str(input(f'Qual a categoria do veículo:\n 1 - Intermediario\n 2 - Compacto\n 3 - SUV\n 4 - Premium\n Escolha: '))

p = ' '
while p not in '567':
   p = str(input(f'Informe o número de passageiros do veículo que pretende alugar:\n 5 passageiros\n 6 passageiros\n 7 passageiros\n Escolha: '))

m = ' '
while m not in '234':
    m = str(input(f'Informe a capacidade do porta-malas do veículo:\n 2 malas\n 3 malas\n 4 malas\n Escolha: '))

a = ' '
while a not in '12':
    a = str(input(f'O cara deve possuir ar condicionado:\n 1 - Sim\n 2 - Não\n Escolha:'))

cam = ' '
while cam not in '12':
    cam = str(input(f'Qual o tipo do câmbio do carro:\n 1 - Manual\n 2 - Automático\n Escolha:'))
























'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

df = pd.read_csv("data.csv")
colunas_independentes = ["numero-de-alunos","temperatura-ambiende","N-Computadores","capacidade-de-sala","Horario-do-dia"]
colunas_dependentes = ["Temperadura"]


dados_x = df[colunas_independentes]
dados_y = df[colunas_dependentes]


modelo = LinearRegression().fit(dados_x, dados_y)

num_alunos = 21
temperatura = 27
N_computadores = 27
capacidade_de_sala = 30
Horario_do_dia = 20

valores = np.array([num_alunos,temperatura,N_computadores,capacidade_de_sala,Horario_do_dia])


print("A temperatura prevista   de:", modelo.predict([valores]))'''