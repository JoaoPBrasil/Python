("Informe o valor dos dois catetos: ")
print("Primeiro cateto: ")
cateto1 = float(input())
print("Segundo cateto: ")
cateto2 = float(input())

hipotenusa = (cateto1 * cateto1) + (cateto2 * cateto2)
hip = hipotenusa ** 0.5


print(f"O valor da hipotenusa desse triângulo é igual ao valor: {hip:.2f}")n
