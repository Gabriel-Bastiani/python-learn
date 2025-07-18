import random
from random import sample, SystemRandom
import math
import pygame
import keyboard

def main():

    print('Desafio 19: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.\n')
    
    alunos = []
  
    
    print(f'Forma mais complexa de fazer com for loop\n')
    while len(alunos) < 4:
        aluno = input(f'Digite o nome do aluno {len(alunos)+1}: ')
        if aluno != '': 
         alunos.append(aluno)
        else:
            print('Digite algo!')
            
    escolhido = random.choice(alunos)  # Escolhe um aluno aleatoriamente
    print(f'O aluno escolhido foi: {escolhido}\n')
    
    
    
    """print(f'Forma mais simples de fazer')
    aluno1 = input(f'Digite o nome do aluno ')
    aluno2 = input(f'Digite o nome do aluno ')
    aluno3 = input(f'Digite o nome do aluno ')
    aluno4 = input(f'Digite o nome do aluno ')
    roleta = random.choice([aluno1, aluno2, aluno3, aluno4])
    print(f'O aluno escolhido é {roleta}')"""
    #desafio20(alunos)

    
if __name__ == "__main__":
    main()
 