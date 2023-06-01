# Nome do aluno:
# Matrícula:
# Data:
# (breve comentário dizendo o programa faz)

import imagens

# Use a mesma função mostrada no slide 18 da Aula 9, apenas mudando
# o input de int para float.
def leiaFloat( msg, vmin, vmax ):
    ...

# Efetua a sobreposição das imagens im1 e im2, considerando o fator 0..1,
# e coloca o resultado dentro da imagem im3
def sobrepoeImagens( im1, im2, im3, fator ):
    ...

# Calcula e retorna o RMSE entre as imagens f e g
def RMSE( f, g ):
    ...
    
###--------------------------------------------------------
### O programa não deve ser alterado deste ponto em diante!
###--------------------------------------------------------

f = leiaFloat('Entre com o percentual para a imagem 1 (0..1): ', 0, 1 )

im1 = imagens.Imagem('Brad_1.jpg')
im1.mostrar()

im2 = imagens.Imagem('Angelina_1.jpg')
im2.mostrar()

print('Fazendo a sobreposição das duas imagens...')
im3 = im1.copia()
sobrepoeImagens( im1, im2, im3, f )
im3.mostrar()

print('RMSE entre as imagens 1 e 3: %.1f' % RMSE( im1, im3 ))
print('RMSE entre as imagens 2 e 3: %.1f' % RMSE( im2, im3 ))
