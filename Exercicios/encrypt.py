
import string

POSITIONS_TO_MOVE = 5

def main():


    string_to_encrypt = input("Por favo me de um texto: ") 

    
    texto_encriptado = encrypt_string( string_to_encrypt )

    print(f"O texto encriptado eh: {texto_encriptado}")

    texto_descriptado = decrypt_string( texto_encriptado )

    print(f"O texto inicial eh: {texto_descriptado}")



def encrypt_string(text: str):

    alfabeto = string.printable
    string_to_return = ""
    tamanho_alfabeto = len(alfabeto)
    print(len(alfabeto))

    for letra in text:

        if letra in alfabeto:
           index = alfabeto.index(letra) #49
           new_index = (index + POSITIONS_TO_MOVE) % tamanho_alfabeto
           string_to_return += alfabeto[new_index]
        else:
            string_to_return += letra
        
        #string_to_return = string_to_return + alfabeto[index+POSITIONS_TO_MOVE]
    return string_to_return

   
def decrypt_string(text: str):

    alfabeto = string.printable
    string_to_return = ""
    tamanho_alfabeto = len(alfabeto)

    for letra in text:

        if letra in alfabeto:
            index = alfabeto.index(letra)
            new_index = (index - POSITIONS_TO_MOVE) % tamanho_alfabeto
            string_to_return += alfabeto[new_index]
        else:
            string_to_return += letra
       # string_to_return = string_to_return + alfabeto[index-POSITIONS_TO_MOVE]
 
    return string_to_return

if __name__ == "__main__":
    main()
