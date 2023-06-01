# Nome do aluno:
# Matrícula:
# Data:
# (breve comentário dizendo o que o programa faz)

import random

print("Jogo 'Adivinhe meu Número'\n")

# Modifique a seguir para que o programa só continue depois que
# o usuário entrar com um valor maior que zero.
limite_superior = int( input('Entre com o limite superior para o sorteio (> 0): '))

# iniciar gerador de números aleatórios para que a sequência fique
# diferente cada vez que o programa é executado.
random.seed()

# gerar valor aleatório n entre 0 e limite_superior
n = random.randint( 0, limite_superior )

print('Acabei de sortear um número entre 0 e %d. Tente adivinha-lo:' % limite_superior )

# Escreva o restante do código abaixo desta linha
