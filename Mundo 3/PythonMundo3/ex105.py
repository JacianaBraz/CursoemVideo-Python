#Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com
# as seguintes informações:
# Quantidade de notas
# A maior nota
# A menor nota
# A média da turma
# A situação (opcional)
# Adicione também as docstrings da função

def notas(*num, situacao=False):
    dados = {}
    dados['total'] = len(num)
    dados['maior'] = max(num)
    dados['menor'] = min(num)
    dados['media'] = sum(num)/len(num)
    if situacao == True:
        if dados['media'] < 6:
            dados['situação'] = 'RUIM'
        elif 7 < dados['media'] >=6:
            dados['situação'] = 'BOM'
        else:
            dados['situacao'] = 'ÓTIMO'
    return dados


#programa principal
resp = notas(10, 9, 6, 5, situacao=True)
print(resp)






