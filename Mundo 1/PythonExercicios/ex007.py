# Desenvolva um programa que leia as duas notas de um aluno, calcula e mostra sua média
nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
soma = nota1+nota2
media = soma/2
print('Suas notas foram: {:.2f} e {:.2f}. E a média entre elas foi de {:.2f}'.format(nota1, nota2, media))
