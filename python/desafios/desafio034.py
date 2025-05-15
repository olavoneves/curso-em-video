valorCasa = int(input('Digite o valor da casa: '))
salario = float(input("Digite o salário do comprador: "))
anos = int(input("Em quantos anos ele vai pagar: "))
mes = anos * 12
valorCasaMensal = valorCasa / mes

if salario - 0.3 > valorCasaMensal:
    print("Empréstimo permitido")
else:
    print("Empréstimo negado")
