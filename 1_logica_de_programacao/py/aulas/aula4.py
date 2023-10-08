# Coleções
preço1 = 23
preço2 = 456
preço3 = 52
# Listas
preços = [23, 456, 52]
# indice   0  1   2
print(preços.index(23))
print(preços[0])
# Exibição Lista
diversidades = [15, 'Felipe', True]
print(diversidades[0])
print(diversidades[1])
print(diversidades[2])
# Exibição Laço de Repetição
for diversidade in diversidades:
    print(diversidade)


idades = [15, 45, 75, 34, 23]
total = 0
for idade in idades:
    total = total + idade
    # how cont elements in phyton
    media = total / len(idades)
print('A soma das', len(idades), 'idades é:', total)
print('A media entre as', len(idades), 'idades é: ', media)
