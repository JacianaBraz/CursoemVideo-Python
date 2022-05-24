def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print('\033[0;31mERRO! TENTE NOVAMENTE!\033[m')
        else:
            valido = True
            return float(entrada)


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um valor inteiro válido\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[0;31mProcesso interrompido pelo usuário\033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError,TypeError):
            print('\033[0;31mERRO!Digite um número\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[0;31mUsuário interrompeu o processo\033[m')
            return 0
        else:
            return n

