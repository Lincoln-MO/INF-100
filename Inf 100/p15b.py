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

# Escrever a matriz M na tela assumindo a formatação fmt
def escreveMatriz( M, fmt ):
    m, n = M.shape  # Obter o número de linhas e colunas de M
    ...

# Retornar o maior valor contido na matriz M
def maiorValor( M ):
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
escreveMatriz( A, '%7.1f')

# Pegar o maior valor contido em A
maior = maiorValor( A )
print('\nMaior valor: %.1f' % maior)

# Escrever a matriz A normalizada na tela
A = A / maior
print('\nMatriz A normalizada:')
escreveMatriz( A, '%7.3f')
