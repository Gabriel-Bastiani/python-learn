import math
def main():
  
    
    print(f'Fase 9 - Manipulando cadeia de textos\n')
    
    frase = 'Curso em Video Python'
    print(f'Frase: {frase}')
    
    
    print('='*50)
    print(' '*13,'Fatiamento de string')
    print('='*50)
            #0123456789
    
    print(f"""Qual tamanho da frase '{frase}' Tamanho: {len(frase)}""")
    print('Quantas letras (o) possuem entre a posição 0 e 12? ',frase.count('o',0,13))
    print('Qual posição começa as letras (deo): ',frase.find('deo'))
    print('Quando buscado algo que não existe na string, ele mostra o valor -1 ',frase.find('Android'))
    print('Curso' in frase) # aqui ele valida se existe a palavra 'Curso' na frase (True or false)
    print(frase[9:21:2]) #Aqui ele vai começar da string 9 até a 20 (pq vai ate a posição 21) pulando de 2 em 2
    print(frase[:5]) # começa do 0 até a letra da posição 5 (o inverso tambem funciona 5:)
    print(frase[9::3])#Vai começar na posição 9 e vai ate o final pulando de 3 em 3

    print('='*50)
    print(' '*13,'Transformação de string')
    print('='*50)
    
    print('Trocar a Palavra (Python) para (Android): ',frase.replace('Python','Android') )
    print('Deixar a frase tudo em maiusculo: ',frase.upper())
    print('Deixar a frase tudo em minusculo: ',frase.lower())
    print('Deixar a frase tudo em minusculo e deixa somente a primeira letra maiusculo: ',frase.capitalize()) # o .title() faz a mesma coisa, mas de palavra em palavra
    print('.strip() remove todos os espaços inuteis de uma string ex:   Aprenda Python  \n Se colocar .rstrip() ele remove somente os ultimos espaços .lstrip remove os primeiros')
    print(f"""Contando quantos 'O' maiusculo tem quando toda a frase foi convertida pra maiusculo: {frase.upper().count('O')}""")
    
    print('='*50)
    print(' '*13,'Divisão de string')
    print('='*50)
    
    
    print(f'.split() Basicamente separa cada palavra da frase e coloca cada uma dela em uma nova lista ex: {frase.split()}')
    print('.join() coloca o caracterer que eu passar entre cada letra, cada posição: ',('-'.join(frase)) )
    
    dividido = frase.split()
    print(f'Peguei a frase dividida com split, mostro a letra da posição 3 da divisão 0 que é Curso: {dividido[0][3]}')
    print('+'*50)
    
def desafio22():
    
    print(f"""Crie um programa que leia o nome completo de uma pessoa e mostre:
          O nome com todas as letras maiúsculas
          O nome com todas as letras minúsuclas
          Quantas letras ao todo (sem considerar espaços)
          Quantas letras tem o primeiro nome""")
    
    name = input('Qual seu nome?')
    print(f'Seu nome com todas as letras maiúsculas: {name.upper()}')
    print(f'Seu nome com todas as letras minúsculas: {name.lower()}')
    print('-'*50)
    namelen = name.replace(' ','')
    print(f'Seu nome possue {namelen.count('')-1} Letras')
    #123456789
    #Gabriel Valverde 16 com o espaço
    namediv = name.split()
    print(f'Seu primeiro nome possue {namediv[0].count('')-1} Letras')
    print('-'*50)
    
def desafio23():
    print(f"""Faça um programa que leia um número de 0 a 9999 e mostre na tela um dos digitos separados
          Ex: Digite um numero: 1834
          
          Unidade: 4
          Dezena: 3
          Centena: 8
          Milhar: 1""")
    
    number = int(input('Qual o numero entre 0 e 9999? '))
    
    print(f"""
          Unidade: {number % 10}
          Dezena: {(number // 10) % 10}
          Centena: {(number // 100) % 10}
          Milhar: {number // 1000}""")
    
    numero = input("Digite um número de 0 a 9999 a ser fatiado por str: ")

    if len(numero) > 4 or not numero.isdigit() or int(numero) < 0:
     print("Número inválido.")
    else:
     numero = numero.zfill(4) # zfill() é um método de string que preenche uma string com zeros à esquerda para atingir um determinado comprimento
     unidade = numero[3]
     dezena = numero[2]
     centena = numero[1]
     milhar = numero[0]

    print("Unidade:", unidade)
    print("Dezena:", dezena)
    print("Centena:", centena)
    print("Milhar:", milhar)

def desafio24():
    
    print(f'Crie um programa que leia o nome da cidade e se ela começa ou não com o nome "Santo"')
    
    city = input('Qual a cidade? ').title()
    
    citydiv = city.split()
    print(f'Começa com "Santo"? {'Santo' in citydiv[0]}')
    
    #Tratando a resposta
    if 'Santo' in citydiv[0]:
        print('Sim! A cidade começa com o nome "Santo" ')
    else:
        print('Não! A cidade não começa com o nome "Santo"')
        
def desafio25():
    
    print('Crie o programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.')
    
    name = input('Qual o nome da pessoa?  ').title()
    print(f'Tem "Silva no nome? {'Silva' in name}')
    
    if 'Silva' in name:
        print('Sim! Tem "Silva" no nome')
    else:
        print('Não! Não tem "Silva" no nome')
    
def desafio26():
    print("""
          Faça um programa que leia uma frase pelo teclado e mostre:
          Quantas vezes aparece a letra 'A' 
          Em que posição ela aparece a primeira vez
          Em que posição ela aparece a ultima vez""")

    frase = input('Qual a frase?  ')
    
    print(f'A Letra "A" aparece na frase {frase.upper().count('A')}')
    
if __name__ == "__main__":
    main()