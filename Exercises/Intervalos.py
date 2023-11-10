# # Input
print("Digite um número para verificarmos: ")
num = int(input())

# Processamento
if num >= 0 and num <= 25:
    resp = ("Número entre 0 e 25!")
elif num > 25 and num <= 50:
    resp = ("Número entre 25 e 50!")
elif num > 50 and num <= 75:
    resp = ("Número entre 50 e 75!")
elif num > 75 and num <= 100:
    resp = ("Número entre 75 e 100!")
else:
    resp = ("Fora dos intervalos!")
# Output
print(resp)
