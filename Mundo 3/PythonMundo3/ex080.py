# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,já na posição correta
# de inserção (sem usar o sort). No final mostre a lista ordenada na tela.

listanum = []

for n in range(0, 5):
    num = int(input('Digite um número: '))
    if n == 0:
        listanum.append(num)
    elif num > listanum[-1]:
        listanum.append(num)
    else:
        posicao = 0
        while posicao < len(listanum):
            if num <= listanum[posicao]:
                listanum.insert(posicao, num)
                break
            posicao += 1
print(listanum)




