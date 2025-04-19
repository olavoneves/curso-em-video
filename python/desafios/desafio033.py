# ler três retas
# responder para o usuariose elas podem ou não formar um triângulo
reta01 = int(input("Digite a 1º reta: "))
reta02 = int(input("Digite a 2º reta: "))
reta03 = int(input("Digite a 3º reta: "))

if reta01 + reta02 == reta03 or reta02 + reta03 == reta01 or reta01 + reta03 == reta02:
    print("Esse triângulo existe!")
else:
    print("Esse triângulo não existe!")
