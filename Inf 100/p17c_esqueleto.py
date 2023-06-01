# Nome do aluno:
# Matrícula:
# Data:
# (breve comentário dizendo o programa faz)

import imagens
import math

# Use a mesma função mostrada no slide 18 da Aula 9, apenas mudando
# o input de int para float.
def leiaFloat( msg, vmin, vmax ):
    ...

# Implementa a função f( x, a ), conforme explicado no roteiro
def f( x, a ):
    ...

# Efetua a sobreposição das imagens im1 e im2, considerando o fator 0..1,
# e coloca o resultado dentro da imagem im3
def mergeImagens( im1, im2, im3, a, d ):
    ...

###--------------------------------------------------------
### O programa não deve ser alterado deste ponto em diante!
###--------------------------------------------------------

a = leiaFloat('Entre com a constante "a" (1..100): ', 1, 100 )
d = leiaFloat('Entre com o deslocamento em pixels (-100..100): ', -100, 100 )

im1 = imagens.Imagem('Brad_1.jpg')
im1.mostrar()

im2 = imagens.Imagem('Angelina_1.jpg')
im2.mostrar()

print('Fazendo o "merge" das duas imagens...')
im3 = im1.copia()
mergeImagens( im1, im2, im3, a, d )
im3.mostrar()
