import datetime

anoNascimento = int(input("Digite seu ano de nascimento: "))
idade = datetime.date.today().year - anoNascimento

if idade <= 9:
    print("MIRIM")
elif idade <= 14:
    print("INFANTIL")
elif idade <= 19:
    print("JUNIOR")
elif idade == 20:
    print("SÊNIOR")
else:
    print("MASTER")
