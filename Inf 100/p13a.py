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

# gerar matriz A: m x n de valores inteiros aleatórios entre 1 e 10.
# Para isso, use a função random.randint( 1, 10 ).
A = np.empty( (m, n), dtype=int )
...

# Escrever a matriz A na tela e guardar o menor valor
...

# Mostrar posições da matriz onde ocorrem o menor valor
...
