n = input('Digite algo: ')
print('Seu tipo primitivo é: ', type(n)) # falar a class do que o usuário digitou na variavel
print('Is a number: ', n.isnumeric()) # numero
print('Is a alfabetico: ', n.isalpha()) # letras
print('Is aphanumeric: ', n.isalnum()) # numero e letra
print('Is maiusculo: ', n.isupper()) # maiusculo
print('Is minusculo: ', n.islower()) # minusculo
