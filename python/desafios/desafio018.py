# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos
# programa que leia o nome dos alunos e mostre a ordem sorteada

import random

nomeProfessor = input('Digite o nome do Professor(a): ')
nomeAluno01 = input('Digite o nome do aluno 01: ')
nomeAluno02 = input('Digite o nome do aluno 02: ')
nomeAluno03 = input('Digite o nome do aluno 03: ')
nomeAluno04 = input('Digite o nome do aluno 04: ')
nomeAluno05 = input('Digite o nome do aluno 05: ')
nomeAluno06 = input('Digite o nome do aluno 06: ')
nomeAluno07 = input('Digite o nome do aluno 07: ')
nomeAluno08 = input('Digite o nome do aluno 08: ')
alunos = [nomeAluno01, nomeAluno02, nomeAluno03, nomeAluno04, nomeAluno05, nomeAluno06, nomeAluno07, nomeAluno08]

random.shuffle(alunos)
print(f'O professor(a) {nomeProfessor} \nFez um sorteio para ver a ordem dos trabalhos! \n{alunos}')
