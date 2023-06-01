# Nome do aluno:
# Matrícula:
# Data:
# (breve comentário dizendo o programa faz)

import imagens

# Efetua a operação matricial im3 = | im1 - im2 |, ou seja,
# coloca na imagem im3 a diferença entre as imagens im1 e im2.
def difImagens( im1, im2, im3 ):
    ...
    
# Retorna o valor máximo de pixel encontrado na imagem img.
def maxPixel( img ):
    ...
    
# Efetua um "alargamento de contraste" para a imagem img.
def alargaContraste( img ):
    ...
    
# Retorna o número de pixels iguais a zero encontrado na imagem img.
def contaZeros( img ):
    ...
    
im1 = imagens.Imagem('Brad_0.jpg')
im1.mostrar()

im2 = imagens.Imagem('Brad_80.jpg')
im2.mostrar()

print('Calculando a diferença entre as duas imagens...')
im3 = im1.copia()
difImagens( im1, im2, im3 )
im3.mostrar()

print('Calculando o "alargamento de contraste" da diferença...')
alargaContraste( im3 )
im3.mostrar()

print('Calculando a semelhança entre as imagens...')
nz = contaZeros( im3 )
ident = nz/(im1.altura * im1.largura) * 100
print('As imagens im1 e im2 são idênticas em %.2f%% dos pixels.' % ident )

