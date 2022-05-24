# Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área
# e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta 2 m².
l = float(input('Qual a largura da parede (em metros): '))
h = float(input('Qual a altura da parede (em metros): '))
a = l*h
tinta = a/2
print('A largura da sua parede é de {}m e a altura é de {}m. A área total a ser pintada é de {:.2f}m². O total de '
      'tinta necessário é {:.2f} litros'.format(l, h, a, tinta))
