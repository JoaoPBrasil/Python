def liga_ar(temp):
    print('Ar ligado')
    print(temp)

def desliga_ar():
    print('Ar desligado')

def captura_sensor_temp():
    temp = int(input('Digite a temperatura: '))
    return temp

def captura_sensor_alunos():
    alunos = int(input('Digite o número de alunos: '))
    return alunos

def valida_temp_com_alunos(alunos):
    temp_inicial = 20
    temp_inicial = temp_inicial - alunos // 3
    return temp_inicial

def valida_temp():
    temp = captura_sensor_temp()
    alunos = captura_sensor_alunos()
    if temp > 21:
        temp_inicial = valida_temp_com_alunos(alunos = alunos)
        liga_ar(temp = temp_inicial)
    else:
        desliga_ar()





valida_temp()