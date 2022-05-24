# Faça uma função que chama contador(), que recebe três parâmetros: inicio, fim e passo e realize a contagem
# Seu programa tem que realizar três contagens através da função criada.
# De 1 até 10. de 1 em 1
# De 10 até 0, de 2 em 2
# Uma contagem personalizada

def contador(i, f, p):
    print(f'\nContagem de {i} a {f} de {p} em {p}')
    c = i
    if p < 0:
        p *= -1
    if p == 0:
        p += 1
    if i < f:
        while c <= f:
            print(c, end=' ')
            c += p
    else:
        while c >= f:
            print(c, end=' ')
            c -= p


#Programa Principal
contador(0, 10, 1)
contador(10, 0, 2)

inicio = int(input('\nDigite o número que você quer iniciar a contagem: '))
fim = int(input('Digite o número que você quer termimar a contagem: '))
passo = int(input('Digite de quanto em quanto irá variar: '))
contador(inicio, fim, passo)


