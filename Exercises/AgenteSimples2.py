def liga_ar():
    print('Ar ligado')

def desliga_ar():
    print('Ar desligado')

def captura_sensor():
    temp = int(input('Digite a temperatura: '))
    return temp

def valida_temp():
    temp = captura_sensor()
    if temp > 21:
        liga_ar()
    else:
        desliga_ar()

valida_temp()
