# um professor quer sortear 1 entre 4 alunos para apagar a lousa
# fazer um programa que ajude ele, lendo o nome e escrevendo o nome do escolhido

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
alunos = nomeAluno01, nomeAluno02, nomeAluno03, nomeAluno04, nomeAluno05, nomeAluno06, nomeAluno07, nomeAluno08

sorteioAluno = random.choice(alunos)
print(f'O Nome sorteado pelo professor(a) {nomeProfessor} foi o(a) {sorteioAluno}')
