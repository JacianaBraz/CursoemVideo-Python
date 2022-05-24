# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com
# a tabela abaixo
# Abaixo de 18,5: ABAIXO DO PESO
# Entre 18,5 e 25: PESO IDEAL
# 25 até 30: SOBREPESO
# 30 até 40: OBESIDADE
# Acima de 40: OBESIDADE MÓRBIDA
peso = float(input('Qual o seu peso? '))
altura = float(input('Qual a sua altura? '))
IMC = peso/altura**2

if IMC < 18.5:
    print('Seu IMC é {:.2f}. Você está ABAIXO DO PESO.'.format(IMC))
elif IMC >= 18.5 and IMC < 25:
    print('Seu IMC é {:.2f}. Você está com o PESO IDEAL.'.format(IMC))
elif IMC >= 25 and IMC < 30:
    print('Seu IMC é {:.2f}. Você está com SOBREPESO.'.format(IMC))
elif IMC >=30 and IMC < 40:
    print('Seu IMC é {:.2f}. Você está com OBESIDADE.'.format(IMC))
else:
    print('Seu IMC é {:.2f}. Você está com OBESIDADE MÓRBIDA.'.format(IMC))