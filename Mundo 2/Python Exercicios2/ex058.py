# Melhore o DESAFIO 28 onde o computador pensa um número entre 0 a 10. Só que agora o jogador vai tentar adivinhar até
# acertar, mostrando no final quantos palpites foram necessários para vencer

import random
computador = random.randint(0, 10)
acertou = False
c = 0

while not acertou:
    pessoa = int(input('Digite um número: '))
    c += 1
    print('Você errou tente novamente')
    if pessoa == computador:
        acertou = True
print('Você acertou na {}ª tentativa: o número era {}'.format(c, computador))

