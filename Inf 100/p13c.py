# Nome do aluno:
# Matrícula:
# Data:
# (breve comentário dizendo o programa faz)

import random
import numpy as np

# Ler o valor de m. O programa deve assegurar que esse valor seja maior que zero.
...

# Ler o valor de n. O programa deve assegurar que esse valor seja maior que zero.
...

# iniciar gerador de números aleatórios para que os valores sejam
# os mesmos cada vez que o programa é executado.
random.seed(0)

# gerar matriz A: m x n de valores inteiros aleatórios binários 0 ou 1
# Para isso, use a função random.randint( 0, 1 ).
A = np.empty( (m, n), dtype=int )
...

# gerar matriz B: m x n de valores inteiros aleatórios binários 0 ou 1
# Para isso, use a função random.randint( 0, 1 ).
B = np.empty( (m, n), dtype=int )
...

# Escrever as matrizes A e B na tela, calculando a esparsidade de cada uma
...

# Escrever a diferença entre as duas esparsidades
...
