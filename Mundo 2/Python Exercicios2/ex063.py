#Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros termos de uma
# Sequencia de Fibonacci

n=int(input('digite o número de termos da sequencia de fibonacci: '))
t1 = 0
t2 = 1
print(t1, t2, end=" ")
c = 3
while c <= n:
    t3 = t1 + t2
    print(t3, end=' ')
    t1 = t2
    t2 = t3
    c += 1


