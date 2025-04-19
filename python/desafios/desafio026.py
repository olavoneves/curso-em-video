# o computador pensar em um numero entre 1 e 5 e o usuario descobrir qual numero o computador pensou
# falar se venceu ou não
import random

numeroSecreto = random.randint(1, 5)

print("O computador pensou em um número entre 1 - 5")
numeroUsuario = int(input("Tente acertar o número em um chute: "))

if numeroSecreto == numeroUsuario:
    print("Você acertou o número secreto!")
else:
    print("Você não acertou o número secreto!")
