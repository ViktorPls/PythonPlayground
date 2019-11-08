# IMPORTAMOS MODULO RANDOM
import random

palabra = 0

# CONSTANTE DE LISTAS CON ASCCI ARTS
IMAGENES_AHORCADO = ['''

   +---+
   |   |
       |
       |
       |
       |
=========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

# PALABRAS POR DEFECTO
WORDS = [
    'sillon',
    'amigo',
    'pana',
    'exterminio',
    'pentakill',
]

#                    Juego 

def elegirPalabra():
    indiceElegido = random.randint(0, len(WORDS) -1) # El -1 es porque las listas comeinzan de 0. De esta forma evito el error 'stdin'. 
    return WORDS[indiceElegido]

def interfazDeJuego(palabraEscondida, intentos):
    print(IMAGENES_AHORCADO[intentos])
    print("")
    print("")
    print(palabraEscondida)
    print("")
    print( "= - = - = - = - = = - = - = - = - = = - = - = - = - =")

def run():
    # Declaramos la variable que contiene la palabra a adivinar y le asignamos el valor de la funcion elegirPalabra()
    palabra = elegirPalabra()
    # Armamos la interface para la palabra
    palabraEscondida = [" - "] * len(palabra)
    intentos = 0

    while True:
        interfazDeJuego(palabraEscondida, intentos)
        letraActual = str(input("Elegí una letra: "))

        indicesLetra = [] #para almacenar los indices de las letras adivinadas
        # Iteramos sobre la longitud de la palabra 
        for i in range (len(palabra)): 
          if palabra[i] == letraActual:
            indicesLetra.append(i)

        if len(indicesLetra) == 0:
          intentos += 1
          if intentos == 6:
            interfazDeJuego(palabraEscondida, intentos)
            print("La palabra era {}".format(palabra))
            print("Perdiste bro! :(")
            break
        else:
          for i in indicesLetra:
            palabraEscondida[i] = letraActual

          indicesLetra = []

        try:
          # Buscamos si hay " - " para comprobar si faltan letras o no
          palabraEscondida.index(" - ")
        except ValueError:
          # ValueError se usa porque si no encuentra " - " lanza error y rompe el programa xd // osea en el caso que no haya - controlamos el error
          print("")
          print("GANASTE! La palabra es {}".format(palabra))
          break

if __name__ == "__main__":
    print ("B I E N V I D O S  A  A H O R C A D O S")
    run()