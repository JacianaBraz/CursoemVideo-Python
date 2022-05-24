#REFAÇA O DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulos serão formados|:
# EQUILÁTERO: 3 lados iguais
# ISÓCELES: 2 iguais
# ESCALENO: nenhum igual
reta1 = float(input('Digite o comprimento de reta: '))
reta2 = float(input('Digite o comprimento da segunda reta: '))
reta3 = float(input('Digite o comprimento da terceira reta: '))
if reta1+reta2 > reta3 and reta1 + reta3 > reta2 and reta2+reta3 > reta1:
    print('Pode formar triângulo.')
    if reta1 == reta2 and reta3 != reta1 or reta2 == reta3 and reta1 != reta3 or reta1 == reta3 and reta2 != reta1:
        print('O triângulo formado é isóceles')
    elif reta1 == reta2 and reta2 == reta3 and reta3 == reta1:
        print('O triângulo formado é equilátero.')
    else:
        print('O triângulo formado é escaleno.')
else:
    print('Não pode formar triângulo.')