# o computador pensar em um numero entre 1 e 5 e o usuario descobrir qual numero o computador pensou
# falar se venceu ou não
import random

from time import sleep

numeroSecreto = random.randint(1, 5)

print("-=-" * 30)
print("O computador pensou em um número entre 1 - 5")
print("-=-" * 30)
numeroUsuario = int(input("Tente acertar o número em um chute: "))
print("Processando...")
sleep(2.5)

if numeroSecreto == numeroUsuario:
    print(numeroSecreto, " = ", numeroUsuario)
    print("Você acertou o número secreto!")
else:
    print(numeroSecreto, " != ", numeroUsuario)
    print("Você não acertou o número secreto!")
