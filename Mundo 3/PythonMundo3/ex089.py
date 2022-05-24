# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final mostre o boletim contendo uma média de cada um e permita que o usuário possa mostrar a nota de cada
# aluno individualmente.

dados = []
alunos = []
media = 0
c=0

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Nota 1: ')))
    dados.append(float(input('Nota 2: ')))
    alunos.append(dados[:])
    dados.clear()

    p = str(input('Deseja continuar? S/N '))
    if p in 'Nn':
        break

    c += 1
for i in range(0,c+1):
    media = (alunos[i][1]+alunos[i][2])/2
    print(f'Boletim: {alunos[i]}, média final:{media}')
