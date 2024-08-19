# Comprimento de onda

# Calcular comprimento de onda com velocidade da luz
def onda(velocidade,frequencia):
    """Return lambda value"""
    if velocidade and frequencia :
        comprimento = velocidade/frequencia
        resposta = f'O comprimento de onda e igua a:{comprimento}m'
    return resposta

# calcular comprimento de onda com constante de boltzman e temperatua 'lambda=b/temperatura

def onda1(constante,temperatura):
    """return lambda value"""
    comprimento = constante/temperatura
    resposta = f'O comprimento de onda e igual a:{comprimento}m'
    return resposta

# Calcular a frequencia

def freq(velocidade,comprimento):
    """Return frequency value"""
    frequencia = velocidade/comprimento
    resposta = f'A frequencia e igual a {frequencia}Hz'
    return resposta

# Calcular a temperatura

def temperature(b,l):
    """Return temperature value"""
    temperatura = b/l
    resposta = f'A temperatura e igual a {temperatura}K'
    return resposta







#############################################################################################################################################################################################
while True:
    Student = int(input('1-Comprimento de onda\n'
                    '2-Comprimento de onda segunda a lei de wien\n'
                    '3-Frequencia\n'
                    '4-Temperatura\n'))


# Enquanto a opcao do estudante for 1,o programa ira calcular o comrpimento de onda com base na formula da velocidade da luz
    while Student == 1 :
      c = 3*10**8
      f = int(input('A frequencia em Hz: '))
      resposta = print(onda(c,f))
      break

# enquanto a opcao do estudante for 2, o programa ira calcular o comprimento de onda segundo a lei de wien
    while Student == 2:
     b = int(input('Constante: '))
     t = int(input('Temperatura: '))
     resposta = print(onda1(b,t))
     break



# Enquanto a opcao do estudante for 3,o programa ira calcular a frequencia

    while Student == 3:
     c = 3*10**8
     l = int(input('Comprimento de onda:'))
     resposta = print(freq(c,l))
     break


# Enquanto a opcao do estudante for 4,o programa ira calcular a temperatura

    while Student == 4:
        b = int(input('Constante: '))
        l = int(input('Comprimento de onda: '))
        resposta = print(temperature(b,l))
        break


