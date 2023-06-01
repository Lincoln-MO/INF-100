n_votos = int(input('Entre com o nùmero de votos: '))
n = 0
votob = 0
voton = 0
voto1 = 0
voto2 = 0
voto3 = 0
while n < n_votos:
    voto=int(input())
    if voto == 0:
        votob = votob  + 1
    elif voto == 1:
        voto1 = voto1  + 1
    elif voto == 2:
        voto2 = voto2  + 1
    elif voto == 3:
        voto3 = voto3  + 1
    else:
        voton = voton  + 1
    n = n +1
vitória = 'Chapa 1'
if voto1 < voto2:
    vitória = 'Chapa 2'
if voto1 < voto3:
    vitória = 'Chapa 3'
print('Votos chapa 1: %d' % voto1)
print('Votos chapa 2: %d' % voto2)
print('Votos chapa 3: %d' % voto3)
print('Votos brancos: %d' % votob)
print('Votos nulos  : %d' % voton)
print('== Vitória da %s == ' % (vitória))
     
        
