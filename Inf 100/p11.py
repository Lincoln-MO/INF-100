# Nome do aluno:
# Matrícula:
# Data:
# (breve comentário dizendo o que o programa faz)

from math import pi, sin, cos, exp
import numpy as np
import plot

# Define a quantidade de pontos nos gráficos e cria os arranjos vx e vy.
# Obs.: essas 3 linhas não precisam ser copiadas para a montagem dos
# outros gráficos.
n = 1000
vx = np.empty( n )
vy = np.empty( n )

# Gráfico do "Peixe"

# Ângulo t (de "tetha") irá variar entre 0 e 1,1*pi
t1 = 0
t2 = 1.1*pi
dt = (t2 - t1) / n  # dt = "delta t" entre cada par de pontos
# Faça t = ângulo inicial t1 
t = t1
for i in range( 0, n ):  # para cada ponto do gráfico...
    vx[i] = t                        # Faça x(t) = t
    vy[i] = sin( t ) * cos( 200*t )  # Faça y(t) = seno(t) * cos( 200t )
    t = t + dt  # Calcula o próximo t 
     
# Plota os pontos do gráfico
plot.plot( vx, vy, 'Peixe', 'x', 'y' )

