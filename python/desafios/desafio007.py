# faça um programa que leia um number inteiro qualquer e mostre na tela a sua tabuada

number = int(input('Digite um número inteiro: '))
numberTabuada = f'{number}x1 = {number * 1} \n{number}x2 ={number * 2} \n{number}x3 ={number * 3} \n{number}x4 ={number * 4} \n{number}x5 ={number * 5} \n{number}x6 ={number * 6} \n{number}x7 ={number * 7} \n{number}x8 ={number * 8} \n{number}x9 ={number *9} \n{number}x10 ={number * 10}'

print(f'A tabuada de {number} é: \n{numberTabuada}')