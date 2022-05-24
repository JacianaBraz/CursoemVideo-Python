# Escreva um programa que leia o valor em metros e o exiba convertido em centímetros e milímetros
m = float(input('Digite um valor em metros: '))
dm = m*10
cm = m*100
mm = m*1000
km = m/1000
hm = m/100
dam = m/10
print('O valor é {}m. Esse valor corresponde a: {}Km, {}Hm, {}Dam, {:.2f}dm, {:.2f}cm e {:.2f}mm.'.format(m, km, hm, dam, dm, cm, mm))

