nome = input('Digite seu nome completo: ')
print(f'Você digitou o nome: {nome}')

if "Silva" in nome.title():
    print('Silva foi encontrado no nome!')
else:
    print('Silva não foi encontrado!')