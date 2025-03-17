# programa que leia o salário de alguem e aumentar 15% do salário dele e exibir para ele

salarioInicial = float(input('Digite seu salário: R$'))
salarioDesconto = (salarioInicial * 15) / 100
salarioFinal = salarioInicial + salarioDesconto

print(f'Após você fazer seu trabalho muito bem, irá receber um aumento de 15% \nSeu novo salário é: {salarioFinal:.2f}')
