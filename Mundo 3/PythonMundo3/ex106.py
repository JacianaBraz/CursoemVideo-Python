# Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer
# Quando o usuário digitar a palavra FIM, o programa se encerrará.
# OBS.: Use cores

from time import sleep

c = ('\033[m', #sem cores
     '\033[0;30;41m', #vermelho
     '\033[0;30;42m', #verde
     '\033[0;30;43m', #amarelo
     '\033[0;30;44m', #azul
     '\033[0;30;45m', #roxo
     '\033[7;30m' #branco
     )


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(comando)
    print(c[0], end='')
    sleep(1)


def titulo(msg, cor=0):
    tamanho = len(msg)
    print(c[cor],end='')
    print('~'*tamanho)
    print(msg)
    print('~'*len(msg))
    print(c[0], end='')
    sleep(0.5)




comando = 0
while True:
    titulo('SISTEMA DE AJUDA', 2)
    comando = str(input("Função ou Biblioteca >> "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO', 1)

