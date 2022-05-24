# Desenvolva um programa que pergunta a distância de uma viagem em Km. Calcule o preço da passagem
# cobrando R$0,50 pela gasolina para viagens de até 2000 Km e R$0,45 para viagens mais longas
distancia = float(input('Qual a distância da sua viagem: '))
if distancia <= 200:
    passagem = distancia*0.5
    print('Você irá viajar {:.2f}Km. O preço da sua passagem será de: R${:.2f}'.format(distancia, passagem))
else:
    passagem = distancia*0.45
    print('Você irá viajar {:.2f}Km. O preço da sua passagem será de R${:.2f}'.format(distancia, passagem))
