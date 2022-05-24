# O mesmo professor do desafio anterior quer sorteara ordem de apresentação de trabalho dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

n1 = input('Digite o nome de um aluno: ')
n2 = input('Digite o nome de um aluno: ')
n3 = input('Digite o nome de um aluno: ')
n4 = input('Digite o nome de um aluno: ')
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentação será:', end="")
print(lista)
