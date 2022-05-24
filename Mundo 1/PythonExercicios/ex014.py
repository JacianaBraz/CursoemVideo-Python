# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
c = float(input('Qual a temperatura em ºC? '))
print('A temperatura é {}ºC. Isso significa {:.2f}ºF.'.format(c, (c*1.8)+32))
