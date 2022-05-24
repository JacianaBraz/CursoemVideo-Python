# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.Faça um programa que ajude ele,
# lendo o nome deles e escrevendo o nome do escolhido
import random
n1 = input('Digite o nome do aluno: ')
n2 = input('Digite o nome do aluno: ')
n3 = input ('Digite o nome do aluno: ')
n4 = input('Digite o nome do aluno: ')
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O aluno escolhido foi: {}'.format(escolhido))
