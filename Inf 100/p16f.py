# Nome do aluno:
# Matrícula:
# Data:
# (breve comentário dizendo o programa faz)

import random
import numpy as np

# Defina aqui uma função de nome leiaIntParPositivo, semelhante à mostrada no
# slide 17 da Aula 9. Mas, em vez de receber os parâmetros 'min' e 'max' e
# lidar com o intervalo [min..max], a função deve apenas verificar se o
# valor é par e maior que zero, conforme mostrado no exemplo do Roteiro.
def leiaIntParPositivo( msg ):
    ...

# criar e retornar matriz m x n de valores inteiros aleatórios entre a e b
# Para isso, use a função random.randint( a, b ).
def criaMatrizInt( m, n, a, b ):
    ...

# Escrever a matriz M na tela assumindo valores inteiros com formatação fmt
def escreveMatriz( M, fmt ):
    ...

# Retornar a submatriz da matriz inteira M compreendida entre as
# linhas i1 e i2 (inclusive) e as colunas j1 e j2 (inclusive)
def submatriz( M, i1, i2, j1, j2 ):
    ...

###--------------------------------------------------------
### O programa não deve ser alterado deste ponto em diante!
###--------------------------------------------------------

# Ler o valor de m
m = leiaIntParPositivo('Entre com o número de linhas da matriz: ')

# Ler o valor de n
n = leiaIntParPositivo('Entre com o número de colunas da matriz: ')

# iniciar gerador de números aleatórios para que os valores sejam
# OS MESMOS sempre que o programa for executado.
random.seed( 0 )

# gerar matriz A: m x n de valores inteiros aleatórios entre 0 e 10
A = criaMatrizInt( m, n, 0, 10 )

# Escrever a matriz A na tela
print('\nMatriz A:')
escreveMatriz( A, '%5d')

# Obter e escrever na tela o quadrante superior esquerdo de A
B = submatriz( A, 0, m//2-1, 0, n//2-1 )
print('\nQuadrante superior esquerdo:')
escreveMatriz( B, '%5d')

# Obter e escrever na tela o quadrante inferior direito de A
C = submatriz( A, m//2, m-1, n//2, n-1 )
print('\nQuadrante inferior direito:')
escreveMatriz( C, '%5d')

# Calcular e escrever na tela a soma dos dois quadrantes
C = B + C
print('\nSoma dos dois quadrantes:')
escreveMatriz( C, '%5d')
