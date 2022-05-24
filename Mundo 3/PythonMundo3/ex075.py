# Desenvolva um programa que leia quatro valores pelo tecado e guarde-os numa tupla. No final mostre:
# Quantas vezes apareceu o número 9
# Em que posição foi digitado o primeiro valor 3
# Quais foram os pares

total=0
a = int(input('Digite um número: '))
b = int(input('Digite um número: '))
c = int(input('Digite um número: '))
d = int(input('Digite um número: '))
numeros = (a, b, c, d)
print('A quantidade de números 9 é: {}'.format(numeros.count(9)))
print('A posição do número 3 é {}'.format(numeros.index(3)+1))
for n in numeros:
    if n%2==0:
        total+=1
print(f'O total de números pares é {total}')

