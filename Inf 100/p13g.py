# Nome do aluno:
# Matrícula:
# Data:
# (breve comentário dizendo o programa faz)

import random
import numpy as np

# Ler o valor de m.
# O programa deve assegurar que esse valor seja maior que zero e par.
...

# Ler o valor de n.
# O programa deve assegurar que esse valor seja maior que zero e par.
...

# iniciar gerador de números aleatórios para que os valores sejam
# os mesmos cada vez que o programa é executado.
random.seed(0)

# gerar matriz A: m x n de valores inteiros aleatórios entre 0 e 10
# Para isso, use a função random.randint( 0, 10 ).
A = np.empty( (m, n), dtype=int )
...

# Escrever a matriz A na tela
...
    
# Calcular a soma do quadrante superior esquerdo de A
...

# Calcular a soma do quadrante inferior direito de A
...
