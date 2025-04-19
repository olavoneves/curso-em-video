# ler um ano aleatorio e falar se é bissexto
anoAleatorio = int(input("Digite um ano aleatorio: "))

if anoAleatorio % 400:
    print("Ano Bissexto!")
elif anoAleatorio % 100:
    print("Esse ano não é bissexto!")
elif anoAleatorio % 4:
    print("Ano Bissexto")
else:
    print("Não é bissexto")
