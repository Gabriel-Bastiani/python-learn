def main():
   
 n1 =input('Digite o primeiro numero: ')
 n2 =input('Digite o segundo numero: ')
      #print(f'A soma entre {n1} e {n2} é igual a {r}!')
 somar(n1, n2)      
 
def somar(n1, n2):
     # Verifica se os valores são numéricos
     # e converte para float se forem válidos
     if n1.isnumeric() and n2.isnumeric():  
         n1 = float(n1)
         n2 = float(n2)  
         r = n1 + n2
         print(f'A soma entre {n1} e {n2} é igual a {r}!')
     else:  
        print('Por favor, digite apenas números inteiros ou decimais.')
        main() 

 

if __name__ == "__main__":
        main() 
        
       