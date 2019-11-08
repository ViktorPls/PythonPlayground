KEYS = {
    'a': 'w',
    'b': 'E',
    'c': 'x',
    'd': '1',
    'e': 'a',
    'f': 't',
    'g': '0',
    'h': 'C',
    'i': 'b',
    'j': '!',
    'k': 'z',
    'l': '8',
    'm': 'M',
    'n': 'I',
    'o': 'd',
    'p': '.',
    'q': 'U',
    'r': 'Y',
    's': 'i',
    't': '3',
    'u': ',',
    'v': 'J',
    'w': 'N',
    'x': 'f',
    'y': 'm',
    'z': 'W',
    'A': 'G',
    'B': 'S',
    'C': 'j',
    'D': 'n',
    'E': 's',
    'F': 'Q',
    'G': 'o',
    'H': 'e',
    'I': 'u',
    'J': 'g',
    'K': '2',
    'L': '9',
    'M': 'A',
    'N': '5',
    'O': '4',
    'P': '?',
    'Q': 'c',
    'R': 'r',
    'S': 'O',
    'T': 'P',
    'U': 'h',
    'V': '6',
    'W': 'q',
    'X': 'H',
    'Y': 'R',
    'Z': 'l',
    '0': 'k',
    '1': '7',
    '2': 'X',
    '3': 'L',
    '4': 'p',
    '5': 'v',
    '6': 'T',
    '7': 'V',
    '8': 'y',
    '9': 'K',
    '.': 'Z',
    ',': 'D',
    '?': 'F',
    '!': 'B',
}

def cifrar(mensaje):
    palabras = mensaje.split(" ")
    cifrarMensaje = []

    for palabra in palabras:
        cifrarPalabra = ""
        for letra in palabra:
            cifrarPalabra = cifrarPalabra + KEYS[letra]
        cifrarMensaje.append(cifrarPalabra)

    return " ".join(cifrarMensaje)

def decifrar(mensaje):
    palabras = mensaje.split(" ")
    decifrarMensaje = []

    for palabra in palabras:
        decifrarPalabra = ""

        for letra in palabra:

            for key, value in KEYS.iteritems():
                if value == letra:
                    decifrarPalabra += key

        decifrarMensaje.append(decifrarPalabra)

    return " ".join(decifrarMensaje)


def run():

    while True:

        command = str(input('''--- * --- * --- * --- * --- * --- * --- * ---

            Bienvenido a criptografia. Que deseas hacer?

            [c]ifrar mensaje
            [d]ecifrar mensaje
            [s]alir
        '''))

        if command == 'c':
            mensaje = str(input("Ingresa el mensaje: "))
            cifrarMensaje = cifrar(mensaje)
            print(cifrarMensaje)
        elif command == 'd':
            mensaje = str(input("Escribe tu mensaje cifrado: "))
            decifrarMensaje = decifrar(mensaje)
            print(decifrarMensaje)
        elif command == 's':
            print('Salir')
        else:
            print('¡Comando no encontrado!')


if __name__ == '__main__':
    print('M E N S A J E S  C I F R A D O S')
    run()