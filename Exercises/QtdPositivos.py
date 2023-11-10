contardor = 0
positivo = 0 

while contardor < 6:
    print(f'Informe um valor, seguido da tecla ENTER: ')
    valor = int(input())
    contardor += 1

    if (valor > 0):
        positivo = positivo + 1

print(f"A quantidade de numero que são positivos é igual a: {positivo}") 
