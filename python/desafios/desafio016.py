# Ler um ãngulo qualquer e mostar os valores de seno, cosseno e tangente

import math

angulo = int(input('Digite um ângulo: '))
print(f'Você digitou {angulo}°')

seno = math.sin(angulo)
cosseno = math.cos(angulo)
tangente = math.tan(angulo)
print(f'Os valores de Seno, Cosseno e Tangente são respectivamente: \n{seno:.0f}, {cosseno:.0f} e {tangente:.0f}')
