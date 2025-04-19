# perguntar o salario e calcular o aumento
# salario maior que R$1250,00 aumento de 10%
# se o salario for menor então aumenta 20%
salario = int(input("Digite o salário: "))

if salario > 1250:
    aumento = (salario * 10) / 100
    novoSalario = salario + int(aumento)
    print("Seu salário agora é de: R$", novoSalario, ",00")
else:
    aumento = (salario * 20) / 100
    novoSalario = salario + int(aumento)
    print("Seu salário agora é de: R$", novoSalario, ",00")
