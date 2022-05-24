# Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai peguntar quantos jogos serão
# gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint

palpites = []
numeros = []

pergunta = int(input('Quantos palpites você quer fazer?'))
for n in range(0,pergunta):
    for c in range(0, 6):
        numeros.append(randint(0,60))
    palpites.append(numeros[:])
    numeros.clear()
print(palpites)