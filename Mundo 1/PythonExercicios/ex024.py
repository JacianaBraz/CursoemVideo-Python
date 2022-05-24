# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com "SANTO"
cidade = str(input('Digite o nome da cidade: '))
cidadeinicio = cidade.upper()
cidadeinicio = cidadeinicio.split()

if cidadeinicio[0] != 'SANTO':
    print('A cidade não começa com Santo.')
else:
    print('A cidade começa com Santo.')
