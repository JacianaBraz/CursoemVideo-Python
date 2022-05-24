# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disse você deve mostrar para cada
# palavra, quais são suas vogais.

palavras = ('amarelo', 'azul', 'vermelho', 'verde', 'rosa', 'laranja', 'branco', 'preto')
for cor in palavras:
    print(f'\nA palavra {cor} tem: ', end='')
    for letra in cor:
        if letra in 'aeiou':
            print(letra, end='')
