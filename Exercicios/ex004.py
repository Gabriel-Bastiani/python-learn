def main():

# desafio 4 faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
#forma correta de fazer o desafio 4

 leia = input('Digite algo: ')
 print(f'O tipo primitivo desse valor é: {type(leia)}')
 print(f'Só tem espaços? {leia.isspace()}')
 print(f'É um número? {leia.isnumeric()}')
 print (f'É alfabético? {leia.isalpha()}')
 print(f'É alfanumérico? {leia.isalnum()}')
 validar_numero(leia) 
#Aqui estou passando a função validar_numero para verificar se o input é um número



#A função validar_numero verifica se os argumentos passados são números
def validar_numero(*args):

    for var in args:
        if not isinstance(var, (int, float)):
           ### raise ValueError(f"Valor inválido: {var}. Deve ser um número.")
            print(f"Valor inválido: '{var}'. Deve ser um número.")
    
if __name__ == "__main__":
     main()
    