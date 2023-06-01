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

# Escrever a matriz M na tela assumindo valores inteiros com formatação fmt
def escreveMatriz( M, fmt ):
    ...

# Retornar a média e o desvio padrão dos valores da matriz M
# Dica: Veja exercícios dos slides da Aula 10
def mediaDesv( M ):
    ...

# Escreve na tela os valores da matriz M que estão fora do intervalo definido
# por [vMin,vMax], mantendo os cabeçalhos, rodapé e formatação mostrados
# no exemplo do Roteiro. Um caractere '<' ou '>' indica se o valor está abaixo
# ou acima do intervalo, respectivamente.
def EscreveValoresForaDoIntervalo( M, vMin, vMax ):
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
escreveMatriz( A, '%4d')

# Pegar a média e desvio padrão dos valores contidos em A
media, dp = mediaDesv( A )
print('\nMédia dos valores de A:  %.3f' % media)
print('Desvio Padrão (DP) de A: %.3f' % dp)
print('Média - DP: %.3f' % (media-dp))
print('Média + DP: %.3f' % (media+dp))
print()

# Mostrar posições da matriz onde os valores são maiores que (media+dp)
# ou menores que (media+dp)
EscreveValoresForaDoIntervalo( A, media-dp, media+dp )
