# Nome do aluno:
# Matrícula:
# Data:
# (breve comentário dizendo o programa faz)

import random
import numpy as np

# Defina aqui uma função de nome leiaIntPositivo, semelhante à mostrada no
# slide 17 da Aula 9. Mas, em vez de receber os parâmetros 'min' e 'max' e
# lidar com o intervalo [min..max], a função deve apenas verificar se o
# valor é maior que zero ou não, conforme mostrado no exemplo do Roteiro.
def leiaIntPositivo( msg ):
    ...

# criar e retornar matriz m x n de valores reais aleatórios entre a e b
# Para isso, use a função random.uniform( a, b ).
def criaMatrizFloat( m, n, a, b ):
    ...

# Escrever a matriz M na tela assumindo com formatação fmt
def escreveMatriz( M, fmt ):
    ...

# Retornar o maior valor contido na matriz M
def maiorValor( M ):
    ...

# Retornar o menor valor contido na matriz M
def menorValor( M ):
    ...

# Retornar a matriz de valores reais soma das matrizes M1 e M2
def somaMatriz( M1, M2 ):
    ...

###--------------------------------------------------------
### O programa não deve ser alterado deste ponto em diante!
###--------------------------------------------------------

# Ler o valor de m
m = leiaIntPositivo('Entre com o número de linhas da matriz: ')

# Ler o valor de n
n = leiaIntPositivo('Entre com o número de colunas da matriz: ')

# iniciar gerador de números aleatórios para que os valores sejam
# OS MESMOS sempre que o programa for executado.
random.seed( 0 )

# gerar matriz A: m x n de valores reais aleatórios entre 0 e 250
A = criaMatrizFloat( m, n, 0, 250 )

# Escrever a matriz A na tela
print('\nMatriz A:')
escreveMatriz( A, '%9.1f')

# Pegar o menor e o maior valor contido em A
menor = menorValor( A )
maior = maiorValor( A )
print('\nMenor valor: %.1f' % menor)
print('Maior valor: %.1f' % maior)

# Escrever a matriz A normalizada na tela
B = A / (maior - menor)
print('\nB = A / (maior - menor):')
escreveMatriz( B, '%9.3f')

C = somaMatriz( A, B )
print('\nC = A + B:')
escreveMatriz( C, '%9.3f')
