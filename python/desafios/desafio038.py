nota01 = int(input("Digite a primeira nota: "))
nota02 = int(input("Digite a segunda nota: "))
media = (nota01 + nota02) / 2

if media <= 5:
    print("REPROVADO")
elif media > 5 and media <= 7:
    print("RECUPERAÇÃO")
else:
    print("APROVADO")
