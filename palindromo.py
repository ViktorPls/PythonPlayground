palabra = str(input("Ingrese una palabra: "))

def esPalindromo():
    
    comprobacion = palabra[::-1]

    if palabra == comprobacion:
        print("{} SI es un palindromo.".format(palabra))
    else:
        print("{} NO es un palindromo.".format(palabra))

if __name__ == "__main__":
    esPalindromo()