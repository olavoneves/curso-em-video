# perguntar a distancia de uma viagem em km
# se a viagem for ate 200km sera cobrado R$0.50 por km
# se a viagem for de maior distancia sera cobrado R$0.45 por km
distanciaViagem = int(input("Digite a distância de uma viagem em KM: "))

if distanciaViagem <= 200:
    passagem = distanciaViagem * 0.50
    print("Você precisa pagar: R$", passagem)
else:
    passagem = distanciaViagem * 0.45
    print("Você precisa pagar: R$", passagem)
