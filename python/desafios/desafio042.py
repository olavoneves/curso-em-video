import random

opcoes = ["Pedra", "Papel", "Tesoura"]
print(opcoes)
jogador01 = input("Escolha sua jogada: ")
print(jogador01)
jogador02 = random.choice(opcoes)
print(jogador02)

if jogador01 == "Pedra" == jogador02 or jogador01 == "Papel" == jogador02 or jogador01 == "Tesoura" == jogador02:
    print("EMPATE")
elif jogador01 == "Pedra" and jogador02 == "Tesoura":
    print("JOGADOR 01 VENCEU")
elif jogador02 == "Pedra" and jogador01 == "Tesoura":
    print("JOGADOR 02 VENCEU")
elif jogador01 == "Papel" and jogador02 == "Pedra":
    print("JOGADOR 01 VENCEU")
elif jogador02 == "Papel" and jogador01 == "Pedra":
    print("JOGADOR 02 VENCEU")
elif jogador01 == "Tesoura" and jogador02 == "Papel":
    print("JOGADOR 01 VENCEU")
elif jogador02 == "Tesoura" and jogador01 == "Papel":
    print("JOGADOR 02 VENCEU")
