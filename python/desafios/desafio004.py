# criar um algoritmo para ler um number e mostrar o dobro, o triplo e a raiz
import math

number = int(input('Digite um número: '))

# para fazer raiz é necessario usar a biblioteca math
print('Seu dobro é: {} \nSeu triplo é: {} \nSua raiz é: {}'.format(number * 2, number * 3, math.sqrt(number) ))