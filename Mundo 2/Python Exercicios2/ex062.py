# Melhore o EXERCÍCIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa vai encerrar
# quando ele disser que quer mostrar 0 termos.

a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão: '))
c = 0
mais = 10
total = 0
while mais != 0:
    total = total + mais
    while c <= total:
        an = a1 + c*r
        c += 1
        print(an, end=' ')
        print()
    mais = int(input('Quantos termos a mais: '))


