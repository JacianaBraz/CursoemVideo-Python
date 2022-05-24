# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase = str(input('Digite uma frase: '))
frase = frase.replace(" ","") #remoção de todos os espaços em branco
frase = frase.upper()
#frase = frase.strip() #tirar os espaços em branco no ínicio e no fim
#palavras = frase.split() #separar palavras de uma frase pelos espaços, montando uma lista
#juntando = ''.join(palavras) #juntar todas as palavras sem espaço
inverso = ''
for letra in range(len(frase)-1, -1, -1):
    inverso += frase[letra]
if inverso == frase:
    print('Temos um palíndromo')
else:
    print('Não é um palíndromo')
