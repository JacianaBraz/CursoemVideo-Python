# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso de zero a vinte.
# Seu programa deverá ler um número, pelo teclado (entr 0 e 20) e mostrá-lo por extenso

extenso = ('um','dois','três','quatro','cinco','seis', 'sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove',
'vinte')
num = int(input('Digite um número de 1 a 20: '))
print(extenso[num-1])
