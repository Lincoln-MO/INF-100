#Nome:Lincoln Martins de Oliveira
#Data:02/09/2017 Matricula:90693
#comentario:

p=float(input('peso do lutador 1: '))
if p <= 0:
    print('Peso Invalido!')
if p > 91:
    categoria1='Super Pesado'
elif p > 81:
     categoria1='Peso Pesado'
elif p > 75:
    categoria1='Meio-Pesado'
elif p > 69:
    categoria1='Peso Médio'
elif p > 64:
    categoria1='Meio-Médio'
elif p > 60:
    categoria1='Peso Leve'
elif p > 56:
    categoria1='Peso Pena'
elif p > 52:
    categoria1='Peso Galo'
elif p > 48:
    categoria1='Peso Mosca'
else:
    categoria1='Mosca Ligeiro'
if p > 0:
    print('Categoria: %s' % categoria1 )

p=float(input('peso do lutador 2: '))
if p <= 0:
    print('Peso Invalido!')
if p > 91:
    categoria2='Super Pesado'
elif p > 81:
     categoria2='Peso Pesado'
elif p > 75:
    categoria2='Meio-Pesado'
elif p > 69:
    categoria2='Peso Médio'
elif p > 64:
    categoria2='Meio-Médio'
elif p > 60:
    categoria2='Peso Leve'
elif p > 56:
    categoria2='Peso Pena'
elif p > 52:
    categoria2='Peso Galo'
elif p > 48:
    categoria2='Peso Mosca'
else:
    categoria2='Mosca Ligeiro'
if p > 0:
    print('Categoria: %s' % categoria2 )
print()
if categoria1 == categoria2:
    comp='Sim'
else:
    comp='Não'
print('Podem se enfrentar: %s ' % comp)


