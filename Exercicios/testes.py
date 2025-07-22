import random
from random import sample, SystemRandom
import math
import pygame
import keyboard

def main():

    

    print("""
          Faça um programa que leia o nome completo de uma pessoa,
          mostrando em seguida o primeiro e o ultimo nome separadamente.
          EX: Ana Maria de Souza
          Primeiro: Ana
          Último: Souza""")
    
    name = input('Qual o nome completo?  ')
    split = name.split()
    lent = (len(split))
    
    print(f'O primeiro nome é: {split[0]}')
    print(f'O último nome é: {split[lent - 1]}')
    
    
    
if __name__ == "__main__":
    main()
    