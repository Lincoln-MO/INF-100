print ('Entre com 3 valores inteiros positivos: ')
a=int(input(''))
b=int(input(''))
c=int(input(''))
d=(c**2)+(b**2)
e=(a**2)+(c**2)
f=(a**2)+(b**2)
if a**2 == d or b**2 == e or c**2 == f:
    teste='formam'
else:
    teste='não formam'
print('Esses valores %s um triângulo pitagórico' %teste)
