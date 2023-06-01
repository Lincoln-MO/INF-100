# Nome do aluno:
# Matrícula:
# Data:
# Este programa aplica um filtro simples e três transformadas geométricas
# em uma imagem.

import imagens

# Ler e mostrar a imagem original na tela
im = imagens.Imagem('jardim.jpg')
im.mostrar()

# Pegar o número de linhas (altura) e número de colunas (largura)
# da matriz que representa a imagem
m = im.altura
n = im.largura

# Fazer uma cópia da imagem original para dentro da variável im2,
# e produzir uma imagem apenas com a componente verde e azul, removendo
# todo o vermelho.
im2 = im.copia()
for i in range( 0, m ):
    for j in range( 0, n ):
        r, g, b = im2[i][j]
        im2[i][j] = (0, g, b)
im2.mostrar()

