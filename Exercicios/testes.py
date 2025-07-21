import random
from random import sample, SystemRandom
import math
import pygame
import keyboard

def main():

    

    print("""
          Faça um programa que leia uma frase pelo teclado e mostre:
          Quantas vezes aparece a letra 'A' 
          Em que posição ela aparece a primeira vez
          Em que posição ela aparece a ultima vez""")

    frase = input('Qual a frase?  ')
    
    print(f'A Letra "A" aparece na frase {frase.upper().count('A')}')
    
    
    
if __name__ == "__main__":
    main()
    