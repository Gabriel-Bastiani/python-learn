def main():
    
    print('Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.\n')
    
    km = float(input('Quantos km percorrido com o carro? ')) * 0.15
    days = int(input('Quantos dias você ficou com o carro? ')) * 60
    
    print(f'Você tera que pagar {km+days}')
    
if __name__ == "__main__":
    main()