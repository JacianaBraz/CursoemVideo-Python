# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteio() e somapar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar somenta a soma
# entre todos os valores PARES sorteados pela função anterior.

from random import randint


def sorteio(lista):
    a = randint(1, 10)
    b = randint(1, 10)
    c = randint(1, 10)
    d = randint(1, 10)
    e = randint(1, 10)
    lista.append(a)
    lista.append(b)
    lista.append(c)
    lista.append(d)
    lista.append(e)
    print(lista)


def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(soma)


# Função principal

l = str(input('Digite o nome para sua lista: '))
print(f'Sua lista {l} possui valores:')
numeros = []
sorteio(numeros)
print(f'O a soma dos valores PARES da sua lista {l} é:', end=' ')
somapar(numeros)
