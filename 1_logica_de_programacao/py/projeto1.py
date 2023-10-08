# Exemplo fatorial de um numero
valid = False
while not valid:  # how use while not in phyton?
    numero = int(input('Fatorial de:'))

    resultado = 1

    if numero >= 1:
        for n in range(1, numero+1):
            resultado *= n
            # resultado *= n eo mesmo que resultado = resultado * n
        print("O resultado é ", resultado)
        valid = True
    else:
        print("Numero invalido, apenas numeros inteiros positivos são validos")
