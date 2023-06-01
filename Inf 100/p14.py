# Nome do aluno:
# Matrícula:
# Data:
# Este programa aplica uma série de filtros em uma imagem, modificando a cor
# dos pixels.

import imagens

def aplicaFiltro( imagem, filtro ):
    im2 = imagem.copia()
    m = im2.altura
    n = im2.largura
    for i in range( 0, m ):
        for j in range( 0, n ):
            r, g, b = im2[i][j]
            r, g, b = filtro( r, g, b )
            im2[i][j] = (r, g, b)
    im2.mostrar()

# Esta função retorna a "luminância" correspondente aos componentes r,g,b
def luminancia( r, g, b ):
    return int( 0.299 * r + 0.587 * g + 0.114 * b )

# retornar apenas as componentes verde e azul, zerando a vermelha
def filtroGB( r, g, b ):
    return 0, g, b
    
im = imagens.Imagem('rgb.jpg')
im.mostrar()

aplicaFiltro( im, filtroGB )
