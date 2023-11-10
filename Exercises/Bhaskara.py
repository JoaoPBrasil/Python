# Input
print("Informe os dados da equação de segundo grau: ")
print("a: ")
a = float(input())
print("b: ")
b = float(input())
print("c: ")
c = float(input())

# Procesamento
delta = ((b * b) - 4 * a * c)
if delta < 0:
    resultado = ("Não há solução!")
elif  delta >= 0:
    resultado1 = ((-(b) + delta**0.5) / 2 * a)
    resultado2 = ((-(b) - delta**0.5) / 2 * a)
      
# Output
if delta < 0:
    print(resultado)
elif delta >= 0:
    print(resultado1, resultado2)
