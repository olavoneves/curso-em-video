# um programa que leia dois valores, o comprimento do cateto oposto e adjacente de um triangulo retângulo
# calcule e mostre a hipotenusa

import math

print('Hipotenusa de Triângulo Retângulo \n')

catOposto = float(input('Digite o cateto Oposto: '))
catAdjacente = float(input('Digite o cateto Adjacente: '))
hipotenusa = math.sqrt(catOposto**2 * catAdjacente**2)

print(f'Cateto Oposto: {catOposto:>18.0f}! \nCateto Adjacente: {catAdjacente:>15.0f}! \nHipotenusa: {hipotenusa:>22.0f}!')
