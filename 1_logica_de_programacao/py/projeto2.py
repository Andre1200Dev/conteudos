import random

n_aleatorio = random.randint(1, 100)
print("O computador pensou em um número de 1 a 10.")
acertou = False
while not acertou:
    chute = int(input('Chute um número: '))
    if chute == n_aleatorio:
        print('Parabéns! Você acertou')
        acertou = True
    elif chute < n_aleatorio and chute > 0:
        print('Você errou! O seu chute foi menor que o número que o computador pensou')
    elif chute > n_aleatorio and chute <= 10:
        print('Você errou! O seu chute foi maior que o número que o computador pensou')
    else:
        print('Digite apenas valores entre 1 e 10.')
