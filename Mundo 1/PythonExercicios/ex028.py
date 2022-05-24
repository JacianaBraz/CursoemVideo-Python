# Escreva uma programação que faça o computador 'pensar' em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random

aleatorio = random.randint(0, 5)
usuario = int(input('Digite um número de 0 a 5: '))
if aleatorio == usuario:
    print('Você venceu! O número era: {}'.format(usuario))
else:
    print('Você perdeu! O número que você escolheu foi {} e o número correto era {}.'.format(usuario, aleatorio))


