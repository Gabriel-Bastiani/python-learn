def main():
    

    print(f'Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.')
    
    temperature = int(input('Qual a temperatura em graus Celcius? '))
    convertf = float(temperature * 9/5) + 32 
    #(x °C × 9/5) + 32 = 33,8 °F

    print(f'A temperatura em Fahrenheit é: {convertf:.1f}'
          )
if __name__ == "__main__":
    main()