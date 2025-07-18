from http.client import REQUESTED_RANGE_NOT_SATISFIABLE
from urllib import request
import json
import requests
import math

def main():
    
    desafio5()
    desafio6()
    desafio7()
    desafio8()
    desafio9()
    desafio10()
    desafio11()
    desafio12()
    desafio13()
    desafio14()
    desafio15()
    extra()
    
    


def desafio5():
   
    print("desafio 5: Crie um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.\n")
    
    # O código abaixo lê um número inteiro e calcula o sucessor e antecessor   
    num = int(input("What's your number? "))
    print(f'Seu numero é: {num} e o próximo é: {num+1} e o anterior é: {num-1}\n')
    
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

    
def desafio11():
    
    print(f'faça um programa que leia a largura e altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.\n')

    widht = float(input(f'Qual a largura da parede?'))
    height = float(input(f'Qual a altura da parede?'))
    x = 1
    result = widht * height
    
    print(f'A area total da sua parede é de: {result} \nVocê irá precisar de {result/2} litros de tinta')
    

        
def desafio12():
      
      offer = 5
      
      print(f'faça um programa que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.\n')
      price = float(input('Qual o preço do produto? '))
      print(f'O preço do produto com 5% de desconto é: {price * (1 - offer/ 100)}\n')
        
      #usando função 
      print(f'Fazendo com a função da na mesma:{price - calc(price)}')
      
      #ou dessa forma burra e direta
      print(f'Fazendo de forma burra:{price - (price * 0.05)}')
        
def calc(preco):
      """Calcula 5% de desconto sobre o preço fornecido."""
      preco = preco * 0.05
      return preco

def desafio13():
    
    print(f'faça um programa que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.\n')
    
    salary = float(input('Qaul seu salário?'))
    
    print(f'Parabéns! Você saiu dessa bosta de salário {salary} para {salary + (salary * 0.15)}')

def desafio14():
    
    print(f'Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.\n')
    
    temperature = int(input('Qual a temperatura em graus Celcius? '))
    convertf = (temperature * 9/5) + 32 
    #(x °C × 9/5) + 32 = 33,8 °F
    
    print(f'A temperatura em Fahrenheit é: {convertf:.1f}')

def desafio15():
    
    print('Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.\n')
    
    km = float(input('Quantos km percorrido com o carro? ')) * 0.15
    days = int(input('Quantos dias você ficou com o carro? ')) * 60
    
    print(f'Você tera que pagar R${km+days} de alguel!')
    
def extra():
    
 print(f'Tentativa de calcular a raiz quadrada de um número negativo (erro)\n')
 numero = -9
 try:
  raiz = math.sqrt(numero)
  print(raiz)
 except ValueError as e:
  print(f"Erro: {e}")
  
if __name__ == "__main__":
    main()