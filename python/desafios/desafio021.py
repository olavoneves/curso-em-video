number = input("Digite um número: ")
if number >= str(0) or number <= str(9999):
    print(f'Você digitou: {number}')
    print(f'''
        unidade: {int(number) // 1 % 10}
        dezena: {int(number) // 10 % 10}
        centena: {int(number) // 100 % 10}
        milhar: {int(number) // 1000 % 10}
    ''')
else:
    print('Você digitou um número negativo ou maior que o permitido no programa')
