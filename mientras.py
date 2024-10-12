#uso de ciclos.
'''
Ejemplo del uso  basico para el uso del while.
'''
def example_while():
    counter = 1
    while(counter >= 10):
        print(f"el numero {counter} es un numero par? {counter % 2 == 0}")
        counter += 1
    else:
        print("El contadortermino")

'''
Crea una arbol utilizando el ciclo while.
utilizando una funcion.
'''
def three():
    caracter = "*"
    height = 10
    size = 1
    while(height > 0):
        print(' ' * height + caracter * size + ' ' * height)
        height-=1
        size+=2
    height_tronco = 3
    while(height_tronco>=0):
        print(' ' * 5 + caracter * 10 + ' ' * 5)
        height_tronco -= 1
'''
Creacion de un diamante.
'''
def diamon(heigth:int):
    caracter = "*"
    size = 1
    # se genera la primer parte del diamante, la sintaxis permite omitir los parentesis.
    while heigth > 0:
        print(' ' * heigth + caracter * size + ' ' * heigth)
        heigth -= 1
        size+=2
    # el tamaño que se va a regresar empieza a partir del valor maximo de tamaño.
    while 0 < size:
        print(' ' * heigth + caracter * size + ' ' * heigth)
        heigth += 1
        size -= 2

# el tamaño del diamante es variable.
diamon(2)