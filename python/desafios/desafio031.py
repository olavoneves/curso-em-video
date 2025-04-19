# ler três numeros e mostrar o maior e o menor
number01 = int(input("Digite um número aleatorio: "))
number02 = int(input("Digite um número aleatorio: "))
number03 = int(input("Digite um número aleatorio: "))

if number01 > number02 and number01 > number03:
    print("Maior: ", number01)
    print("O primeiro número é o maior!")
elif number02 > number01 and number02 > number03:
    print("Maior: ", number02)
    print("O segundo número é o maior!")
else:
    print("Maior: ", number03)
    print("O terceiro número é o maior!")

if number01 < number02 and number01 < number03:
    print("Menor: ", number01)
    print("O primeiro número é o menor!")
elif number02 > number01 and number02 > number03:
    print("Menor: ", number02)
    print("O segundo número é o menor!")
else:
    print("Menor: ", number03)
    print("O terceiro número é o menor!")
