from datetime import datetime as getdate

def main():
    # O código abaixo imprime uma mensagem na tela
    print('Olá, esse é meu primeiro codigo em Python!\nEstou fazendo a primeira aula do curso #04')

    nome = input('Qual seu nome? ')
    idade = input('Qual sua idade? ')    
    peso = input('Qual seu peso? ')

    # O código abaixo imprime as variáveis nome, idade e peso de forma formatada utilizando f-strings
    print(f'\nNome: {nome} \nIdade: {idade} \nPeso: {peso}')

    #Desafio 01
    print('\n' + '#' * 94 + '\n')

    # O código abaixo lê o nome de uma pessoa e mostra uma mensagem de boas-vindas
    print('Desafio 01: Crie um programa que leia o nome de uma pessoa, mostre uma mensagem de boas-vindas e o nome dela.')
    nome2 = input('Digite seu nome: ')
    print('Olá, seja bem-vindo(a) ' + nome2 + '!')

    # Desafio 02
    print('\n' + '#' * 94 + '\n')

    # O código abaixo lê o dia, mês e ano de nascimento de uma pessoa e mostra a data formatada
    print('Desafio 02: Crie um programa que leia o dia, o mes e o ano de nascimento de uma pessoa, mostrando uma mensagem com a data formatada.')
    dia = input('Qual o dia do seu nascimento? ')
    mes = input('Qual o mês do seu nascimento? ')
    ano = input('Qual o ano do seu nascimento? ')
    print(f'Você nasceu no dia {dia} de {mes} de {ano}.')
    
    hoje = getdate(day=getdate.today().day, 
                  month=getdate.today().month, 
                  year=getdate.today().year)    
    if (hoje.day == int(dia) and hoje.month == int(mes)):
        print('Parabéns, hoje é seu aniversário!')
    else: 
        print('Hoje não é seu aniversário.')

    # Desafio 03
    print('\n##############################################################################################\n')
    print('Desafio 03: Crie um script que leia dois números e mostre a soma entre eles.')

    num1 = input('Digite o primeiro número: ')
    num2 = input('Digite o segundo número: ')
    print(f'A soma entre {num1} e {num2} é {int(num1) + int(num2)}.')
    
if __name__ == "__main__": 
    main()

    