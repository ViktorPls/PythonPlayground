def busquedaBinaria(numeros, numberToFind, lowIndex, highIndex):
    # Primer caso base: El indice bajo es mas alto que el indice alto, por tanto no se encuentra el numero en la lista
    if lowIndex > highIndex:
        return False
    # Agregado el // porqe en python 3 la division de ints puede dar floats. Osea en py3: "a // b = 0" o "a / b = 0.0"
    midIndex = (lowIndex + highIndex) // 2

    # Segundo caso base: Si encontramos o no encontramos el numero en el medio
    if numeros[midIndex] == numberToFind:
        return True
    # Tercer caso base: midIndex es mas alto que numberToFind, entonces nos vamos hacia abajo en la lista. O midIndex es mas bajo por tanto nos vamos para arriba en la lista
    elif numeros[midIndex] > numberToFind:
        return busquedaBinaria(numeros, numberToFind, lowIndex, midIndex - 1)
    else:
        return busquedaBinaria(numeros, numberToFind, midIndex + 1, highIndex)


if __name__ == "__main__":
    numeros = [1, 4, 15, 22, 27, 29, 36, 53, 56, 63, 66, 78, 91, 95, 96, 98]

    numberToFind = int(input("Ingrese un numero: "))

    result = busquedaBinaria(numeros, numberToFind, 0, len(numeros) - 1)

    if result == True:
        print ("El numero {} SI esta en la lista".format(numberToFind))
    else:
        print ("El numero {} NO esta en la lista".format(numberToFind))