# Crie um programa que leia duas notas de um aluno e calcule sua mádia mostrando uma mensagem ao final, de acordo com a média atingida
# Média abaixo de 5,0: REPROVADO
# Média entre 5,0 e 6,9: RECUPERAÇÃO
# Média 7 ou superior: APROVADO

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1+nota2)/2

if media > 5.0 and media <= 6.9:
    print('Sua média foi de {:.1f}. Você está de RECUPERAÇÃO'.format(media))
elif media >= 7.0:
    print('Sua média foi {:.1f}. Você foi APROVADO'.format(media))
else:
    print('Sua média foi {:.1f}. Você foi REPROVADO'.format(media))