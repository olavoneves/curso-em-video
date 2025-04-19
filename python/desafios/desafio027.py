# ler a velocidade de um carro , se ultrapassar 80km vai dizer que foi multado e vai mostrar a multa ( a multa custa R$7,00 por km acima da velocidade )
# se não ultrapassou tudo ok

velocidadeCarro = int(input("Digite a velocidade do carro em km: "))

if velocidadeCarro > 80:
    velocidadeAcima = velocidadeCarro - 80
    multa = velocidadeAcima * 7
    print("Você foi multado!")
    print("Multa: R$", multa, ",00")
else:
    print("Tudo OK")
