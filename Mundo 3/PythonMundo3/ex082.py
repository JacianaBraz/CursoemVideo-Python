# Crie um programa que vai ler vários números e colocar numa lista. Depois disso, crie duas listas extras que vão conter
# apenas os valores pares e os valores ímares digitados respectivamente. No final mostre o conteúdo da três listas geradas.

numeros = []
par = []
impar = []

while True:
    n = int(input('Digite um número: '))
    numeros.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    r = str(input('Deseja continuar? S/N '))
    if r in 'Nn':
        break
print(numeros)
print(par)
print(impar)