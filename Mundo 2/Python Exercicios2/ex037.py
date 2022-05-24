# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher a base de conversão.
# 1 binário
# 2 octal
# 3 hexadecimal

num = int(input('Digite um número: '))
convertido = str(input('Qual tipo de conversão você quer? Binario, octal ou hexadecimal '))

if convertido == 'binario':
    num2 = format(num, 'b')
    print('O valor binário do número {} é {}'.format(num, num2))
elif convertido == 'octal':
    num2 = format(num, 'o')
    print('O valor octal do número {} é {}'.format(num, num2))
else:
    num2 = format(num, 'x')
    print('O valor hexadecimal do número {} é {}'.format(num, num2))
