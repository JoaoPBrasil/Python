def imprime():
    temp = int(input('Qual a temperatura do ambiente? '))
    num = int(input('Qual a quantidade de alunos da sala? '))

    if temp >= 21:
        s = (f'A temperatura está em {temp}°C. O Ar Condicionado será ligado!')

        qtd = num / 3

        x = (f'O ar ficará na temperatura {20 - qtd}°C.')

    else: 
        s = (f'A temperatura está em {temp}°C. O Ar condicionado não será ligado!')

    print(s)
    print(x)
 

imprime()