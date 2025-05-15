import datetime

anoNascimento = int(input("Digite seu ano de nascimento: "))
idade = datetime.date.today().year - anoNascimento

if idade < 18:
    print(idade)
    print("Ainda vai se alistar")
elif idade == 18:
    print(idade)
    print("Hora de se alistar")
else:
    print(idade)
    print("Já passou o tempo de se alistar")
