# Crie um código em Python que teste se o site PUDIM está acessível pelo computador usado.

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br/')
except urllib.error.URLError:
    print('\033[0;31mERRO! O site não está acessível no momento\033[m')
else:
    print('O site pode ser acessado')

