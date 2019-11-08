import random

numeros = []
def numerosAleatorios():
    for i in range(15):
        nAleatorio = random.randint(1, 100)
        numeros.append(nAleatorio)
        numeros.sort()
    return numeros

if __name__ == "__main__":
    print(numerosAleatorios())