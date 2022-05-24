# Faça um programa que tenha uma função chamada area(), que receba as dimensões de um terreno retangular
# (largura e comprimento) e mostre a área do terreno.
def area(largura,comprimento):
    a = largura*comprimento
    print(f'A largura do terreno é {largura} m, o comprimento é {comprimento} m e a área é {a:.2f} m²')


#Programa Principal
l = float(input('Digite a largura do terreno: '))
c = float(input('Digite o comprimento do terreno '))
area(l, c)




