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

# criar e retornar matriz m x n de valores inteiros aleatórios entre a e b
# Para isso, use a função random.randint( a, b ).
def criaMatrizInt( m, n, a, b ):
    ...

# Escrever a matriz M na tela assumindo valores inteiros com espaçamento 4
def escreveMatriz( M ):
    m, n = M.shape  # Obter o número de linhas e colunas de M
    ...

# Retornar o menor valor contido na matriz M
def menorValor( M ):
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

# gerar matriz A: m x n de valores inteiros aleatórios entre 1 e 10
A = criaMatrizInt( m, n, 1, 10 )

# Escrever a matriz A na tela
print('\nMatriz A:')
escreveMatriz( A )

# Pegar o menor valor contido em A
menor = menorValor( A )
print('\nMenor valor:', menor)

# Mostrar posições da matriz onde ocorre o menor valor
print('Posições de ocorrência do valor %d:' % menor )
print('\nLinha   Coluna')
print('--------------')
for i in range(0, m):
    for j in range(0, n):
        if A[i][j] == menor:
            print('%3d%8d' % (i, j))
