number = input("Digite um número: ")
if number >= str(0) or number <= str(9999):
    print(f'Você digitou: {number}')
    print(f'''
        unidade: {(number[3])}
        dezena: {(number[2])}
        centena: {(number[1])}
        milhar: {(number[0])}
    ''')
else:
    print('Você digitou um número negativo ou maior que o permitido no programa')
