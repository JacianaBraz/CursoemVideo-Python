# Faça um programa que tenha uma função que chama escreva(), que receba um texto qualquer como parâmetro e mostre uma
# função com tamanho adaptável.

def escreva(tex):
    t = len(tex)
    print('~'*t)
    print(tex)
    print('~'*t)


#Programa Pricipal
txt = str(input('Digite o que quer mostrar para o usuário: '))
escreva(txt)

