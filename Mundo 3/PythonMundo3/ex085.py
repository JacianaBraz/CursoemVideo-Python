# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que maantenha
# separados os valores pares e ímpares e no final mostre os valores pares e ímpares em ordem crescente.

valores = []
par = []
impar = []

for c in range(0,7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        par.append(n)
        par.sort()
    else:
        impar.append(n)
        impar.sort()

valores.append(par[:])
valores.append(impar[:])
print(valores)

