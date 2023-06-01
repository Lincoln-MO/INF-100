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

# Escrever a matriz M na tela assumindo valores inteiros com espaçamento 5
def escreveMatriz( M ):
    m, n = M.shape  # Obter o número de linhas e colunas de M
    ...

# Retornar o número de vezes que o valor v é encontrado na matriz M
def contaValor( M, v ):
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

# gerar as matrizes A e B: m x n de valores inteiros aleatórios binários 0 ou 1
A = criaMatrizInt( m, n, 0, 1 )
B = criaMatrizInt( m, n, 0, 1 )

# Escrever as matrizes A e B na tela, calculando a esparsidade de cada uma
print('\nMatriz A:')
escreveMatriz( A )
espA = contaValor( A, 0 ) / (m*n)
print('Esparsidade: %.4f = %.2f%%' % (espA, espA*100) )

print('\nMatriz B:')
escreveMatriz( B )
espB = contaValor( B, 0 ) / (m*n)
print('Esparsidade: %.4f = %.2f%%' % (espB, espB*100) )

print('\nEsparsidade de A – Esparsidade de B = %.4f' % (espA-espB) )
