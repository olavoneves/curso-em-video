name01 = input('Digite um nome: ')
name02 = input('Digite o sobrenome: ')
nameLastName = name01 + name02

# :> = Centralizar a direita, :< = Centralizar a esquerda, :^ = Centralizar no centro, :=30 = 30 casas de =, :-20 = 20 casas de -
print('Seu nome é {:>30} \nSeu sobrenome é {:>30} \nSeu nome completo é {:=>15} {:=<15}!'.format(name01, name02, name01, name02))

number01 = int(input('Primeiro valor: '))
number02 = int(input('Segundo valor: '))

soma = number01 + number02
multiplica = number01 * number02
divide = number01 / number02
divideInt = number01 // number02
potencia = number01 ** number02

print('A soma vale: {:-^30} \nA multiplicação é: {:-^30} \nA divisão é: {:-^30} \nA divisão inteira é: {:-^30} \nA potencia deles é: {:-^30} \n'.format(soma, multiplica, divide, divideInt, potencia))
print('Obrigado {:=>15} {:=<15}!'.format(name01, name02))
