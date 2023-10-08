# Programa de velocidade maxima
vmax = 80
valid = False
print("Velocidade máxima permitida:", vmax, "km/h")

while not valid:
    velocidade = int(input('Qual era a sua velocidade? '))
    if velocidade <= vmax and velocidade > 0:
        print('Não houve multa você estava dentro da velocidade permitida!')
        valid = True
    elif velocidade > vmax and velocidade <= vmax + 10 and velocidade > 0:
        print('Você recebeu uma multa leve')
        valid = True
    elif velocidade > vmax + 10 and velocidade <= vmax + 20 and velocidade > 0:
        print('Você recebeu uma multa grave')
        valid = True
    elif velocidade > vmax + 20 and velocidade > 0:
        print('Você recebeu uma multa gravíssima')
        valid = True
    else:
        print('Informe uma velocidade valida!')
