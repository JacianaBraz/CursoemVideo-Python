# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra 'A'
# Em que posição ela aparece pela primeira vez
# Em que posião ela aparece a última vez
frase = str(input('Digite uma frase: '))
frasemaiuscula = frase.upper()
quantos = frasemaiuscula.count('A')
posicao1 = frasemaiuscula.find('A')
posicaou = frasemaiuscula.rfind('A')
print('A frase é: {}'.format(frase))
print('Nessa frase há {} letras A'.format(quantos))
print('A primeira vez que a letra aparece é na posição {}'.format(posicao1+1))
print('A última vez que a letra aparece é na posição {}'.format(posicaou+1))

