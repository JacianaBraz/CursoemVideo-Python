# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequencia.
#No final , mostre a listagem de preços, organizando-os de forma tabular

compras =('arroz',10,'feijão',5,'macarrão',3.5,'verduras',8,'batata frita', 20)

print('-'*30)
print('-'*10,'Compras','-'*10)
print('-'*30)
for posicao in range(len(compras)):
    if posicao % 2 == 0:
        print(f'{compras[posicao]:.<25}',end='')
    else:
        print(f'{compras[posicao]:.2f}')