soma = 0
n = 0
peso = float (input('Digite um peso (ou -1 para encerrar): '))
while peso > 0:
    soma = soma + peso
    n = n + 1
    peso = float (input('Digite um peso (ou -1 para encerrar): '))
media = soma / n
print()
print('Número de capivaras:', n )
print('Peso médio: %5.1f kg' % media )
