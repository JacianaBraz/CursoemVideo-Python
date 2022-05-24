# Aprimore o desafio anterior. Mostrando no final:
# A soma de todos os valores pares digitados.
# A soma dos valores da terceira coluna
# O maior valor da segunda linha

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = 0
soma = 0
maior = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}][{coluna}]: '))

for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^8}]', end='')
    print()

for linha in range(0,3):
    for coluna in range(0,3):
        if matriz[linha][coluna] % 2 == 0:
            par += matriz[linha][coluna]

for linha in range(0,3):
    if matriz[linha][2]:
        soma += matriz[linha][2]

for linha in range(0,3):
    for coluna in range (0,3):
        maior = matriz[1][coluna]
        if maior < matriz[1][coluna]:
            maior = matriz[1][coluna]

print(f'A soma dos valores pares é de {par}')
print(f'A soma dos elementos da coluna 3 é {soma}')
print(f'O maior valor da segunda linha é {maior}')


