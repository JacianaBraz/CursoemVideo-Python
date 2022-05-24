#Refaça o EXERCÍCIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão
# usando while
a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão: '))
c = 0
while c < 10:
    an = a1 + c*r
    c += 1
    print(an, end=" ")