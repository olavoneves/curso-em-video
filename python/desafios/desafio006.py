# um programa que leia o valor em metros e exiba em centimetros e milimetros

value = int(input('Digite um valor em metros: '))
valueCentimetros = value / 100
valueMilimetros = value / 1000

print(f'Você digitou {value} metros, {valueCentimetros} centímetros, {valueMilimetros} milimetros!')