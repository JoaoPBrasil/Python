def imprime():
    temp = int(input('Qual a temperatura do ambiente? '))
    if temp >= 21:
        s = (f'A temperatura está em {temp}°C. O Ar Condicionado será ligado!')
    else: 
        s = (f'A temperatura está em {temp}°C. O Ar condicionado não será ligado!')

    print(s)
 

imprime()