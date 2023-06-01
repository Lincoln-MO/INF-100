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

# criar e retornar matriz m x n de valores REAIS aleatórios entre a e b
# Para isso, use a função random.randint( a, b ).
def criaMatriz( m, n, a, b ):
    ...

# Escrever a matriz M na tela usando a formatação fmt
def escreveMatriz( M, fmt ):
    ...

# Retornar o maior valor contido no arranjo unidimensional V
def maiorValor( V ):
    ...

# Retornar um arranjo contendo o maior valor de cada linha da matriz M.
def pegaMaxLinhasMatriz( M ):
    ...

# Dividir cada elemento M[i][j] por V[i]
def divideMatVet( M, V ):
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

# gerar matriz A: m x n de valores aleatórios entre 1 e 50
A = criaMatriz( m, n, 1, 50 )

# Escrever a matriz A na tela com formatação '5.0f'
print('\nMatriz A:')
escreveMatriz( A, '%5.0f')
    
# Criar um arranjo M de m itens contendo o maior valor de cada linha de A
M = pegaMaxLinhasMatriz( A )
    
# Dividir cada elemento A[i][j] por M[i] e escrever o resultado na tela
divideMatVet( A, M )
print('\nMatriz A normalizada por linha:')
escreveMatriz( A, '%7.3f')
