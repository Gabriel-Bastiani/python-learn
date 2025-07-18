from math import ceil, sqrt, trunc
import math
import random
import emoji
import pygame
import keyboard

def main():
    aula08()
    desafio16()
    desafio17()
    print('Obrigado por usar o programa! 🍆')
    
 
   
 
def aula08():
    print(emoji.emojize('Bem-vindo ao programa de exercícios! 🍆 \U0001f628'))

    
    print('Aula 08: Funções e Módulos\n')
    num = int(input('numero? '))
    raiz = sqrt(num)
    print(f'A Raiz de {num} é {ceil(raiz)}') #ceil arredonda o valor
    
    numrand = random.randint(1, 10) #gera um número inteiro aleatório entre 1 e 10
    print(f'O número aleatório gerado é: {numrand}')

def desafio16():
    print('Desafio 16: Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.\n')
    
    print('forma simples de fazer convertendo em int\n')
    num = float(input('Digite um número: '))
    print(f'A parte inteira de {num} é {int(num)}\n') 
    
    print('forma diferente de fazer usando *trunc*\n')
    print(f'A parte inteira de {num} é {trunc(num)}\n') #trunc remove a parte decimal do número

def desafio17():
    print('Desafio 17: Crie um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.\n')
    
    cateto_oposto = float(input('Digite o comprimento do cateto oposto: '))
    cateto_adjacente = float(input('Digite o comprimento do cateto adjacente: '))
    
    
    hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)  # Calcula a hipotenusa usando o teorema de Pitágoras
    print(f'O comprimento da hipotenusa é: {hipotenusa:.2f}\n')

def desafio18():
    
    print(f'Faça um programa que leia um ângulo qualquer e motre na tela o valor do seno, cosseno e tangente desse ângulo.')
    
    ang = float(input('Qual valor do ângulo? '))
    print(f'Angulo informado: {ang}')
    ang_r = math.radians(ang)
    print(f'Angulo convertido para radiano: {ang_r}')
    
    sen = math.sin(ang_r)
    cos = math.cos(ang_r)
    tan = math.tan(ang_r)
    
    print(f'O seno é {sen:.2f}\nO Consseno é: {cos:.2f}\nA Tangente é: {tan:.2f}')
    
    
    
def desafio19():
    
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
    desafio20(alunos)

def desafio20(alum):#Vou usar a mesma lista de alunos que ja tem ali em cima
    print('Desafio 20: O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.\n')
    
    ordem_alunos = []

 #A lista ordem_alunos vai começar em 0. Depois que rodar o 1 while, ja vai ter uma informação, com isso a validação IF fara mais sentido. 
    while len(ordem_alunos) < len(alum):
        
        roll = random.choice(alum)
        # Valida se a informação gerada naquele momento do roll ja existe na lista ordem_alunos, se não, ele adiciona. Se for a mesma informação, ele não adiciona e faz o while novamente pq o len ainda é menor.
        if roll not in ordem_alunos:
            ordem_alunos.append(roll)
            
    
    print(f'Ordem de alunos a apresentar: ', ', '.join(['Aluno: ' + ordem for ordem in ordem_alunos]))
    
def desafio21():
    
   pygame.mixer.init()
   pygame.mixer.music.load('H:/coisas/sons/Sons/Musicas/poze-ingles.mp3')
   pygame.mixer.music.play()

   print("Pressione A tecla 'P' para parar a música...")

   while pygame.mixer.music.get_busy():
    if keyboard.is_pressed('P'):  # qualquer tecla
        pygame.mixer.music.stop()
        break

   pygame.mixer.quit()

    
if __name__ == "__main__":
    main()
    
    