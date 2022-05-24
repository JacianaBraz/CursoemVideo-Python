def aumentar(num=0, pormaximo=0, retorna=False):
    a = num * (1+(pormaximo/100))
    return a if retorna is False else moeda(a)


def diminuir(num=0, porminimo=0, retorna=False):
    d = num - (num * (porminimo/100))
    return d if retorna is False else moeda(d)


def dobro(num=0, retorna=False):
    db = 2*num
    return db if not retorna else moeda(db)


def metade(num=0, retorna=False):
    mt = num/2
    return mt if not retorna else moeda(mt)


def moeda(num=0, m='R$'):
    reais = f'R$ {m}{num:.2f}'.replace('.', ',')
    return reais


def resumo(num=0, pormax=0, pormin=0):
    print(f'O valor em moeda é {moeda(num)}')
    print(f'O aumento de {pormax} % em {moeda(num)} é {aumentar(num, pormax,True)}')
    print(f'A redução de {pormin} % em {moeda(num)} é {diminuir(num, pormin, True)}')
    print(f'O dobro do {moeda(num)} é {dobro(num, True)}')
    print(f'A metade de {moeda(num)} é {metade(num, True)}')

