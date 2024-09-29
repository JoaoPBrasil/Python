import pandas as pd
import numpy as np

df = pd.read_csv("DB1.csv")
colunas_independentes = ["Categoria-do-veiculo","Numero-de-passageiros","Capacidade-de-porta-malas","Possui-ar-condicionado","Tipo-de-cambio"]

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
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv("data.csv")
colunas_independentes = ["numero-de-alunos","temperatura-ambiende","N-Computadores","capacidade-de-sala","Horario-do-dia"]
colunas_dependentes = ["Temperadura"]'''
