from http.client import REQUESTED_RANGE_NOT_SATISFIABLE
from urllib import request
import json


def main():
    
    
    
    
    print("Welcome to the Exercise program!\n")

def desafio5():
   
    print("desafio 5: Crie um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.\n")
    
    # O código abaixo lê um número inteiro e calcula o sucessor e antecessor   
    num = int(input("What yor number? "))
    print(f'Seu numero é: {num} e o próximo é: {num+1} e o anterior é: {num-1}')
    
def desafio6():
    
    print('desafio 6: Crie um programa que leia um numero e mostre na tela o dobro, triplo e raiz quadrada.\n')
    
    num = int(input("Digite um número: "))
    print(f'O dobro de {num} é {num*2}\n O triplo de {num} é {num*3} \n A Raiz de {num} é {num ** (1/2):.2f}\n') 
    
def desafio7():
    
    print(f'desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.\n')
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    media = (nota1 + nota2) / 2
    print(f'A média do aluno é: {media:.1f}\n')

def desafio8():
    
    print('Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.\n')
    num = float(input('Qual a medida em metros?'))
    print(f'{num} metros convertido em centimetros fica: {num * 100:.1f}cm. E em milímetros fica {num * 1000:.1f}mm')

def desafio9():
    
    print('Faça um programa que leia um numero inteiro e mostre a tabuada dele\n')
    
    num = int(input('Qual o numero que você que saber a tabuada? '))
    repeat = 10
    
    for x in range(repeat):
        
     print(f'{num} x {x+1} = {num * (x+1)}')
    
def desafio10():
    
    import requests
    
    print(f'crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.\n')
    
    money = float(input('Quanto de dinheiro vc tem, seu fodido? '))
    cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL") 
    cotacoes = cotacoes.json()
    cotacao_dolar = cotacoes['USDBRL']["bid"]
    #cotacao_euro = cotacoes['EURBRL']["bid"]
    #cotacao_bitcoin = cotacoes['BTCBRL']["bid"]

    print(f"\n Cotação do Dólar Americano/Real Brasileiro. R$1 = ${cotacao_dolar}.\n")
    #print("\n Cotação do Euro/Real Brasileiro: ", cotacao_euro)
    #print("\n Cotação do Bitcoin/Real Brasileiro: ", cotacao_bitcoin)
    #print("\n Cotações sem formatação: \n",cotacoes)
    print(f'Com {money} você pode comprar {money / float(cotacao_dolar):.1f} dólares americanos.\n')
    

    

        
        


if __name__ == "__main__":
    main()
    desafio5()
    desafio6()
    desafio7()
    desafio8()
    desafio9()
    desafio10()