# Nome do aluno:
# Matrícula:
# Data:
# (breve comentário dizendo o programa faz)

import imagens

# Retorna o valor mínimo e máximo de pixel encontrado na imagem img
def imgMinMax( img ):
    ...

# Efetua o alargamento de contraste da imagem im1, com base nos
# valores limite pmin e pmax, retornando o resultado na imagem im2
def alargaContraste( im1, im2, pmin, pmax ):
    ...

# Calcula e retorna o RMSE entre as imagens f e g
def RMSE( f, g ):
    ...
    
###--------------------------------------------------------
### O programa não deve ser alterado deste ponto em diante!
###--------------------------------------------------------

im1 = imagens.Imagem('Angelina_2.jpg')
im1.mostrar()

print('Calculando min/max...')
pmin, pmax = imgMinMax( im1 )

print('Alargando contraste...')
im2 = im1.copia()
alargaContraste( im1, im2, pmin, pmax )
im2.mostrar()

# Exibe RMSE entre im1 e im2
print('RMSE entre as imagens 1 e 2: %.1f' % RMSE( im1, im2 ) )
