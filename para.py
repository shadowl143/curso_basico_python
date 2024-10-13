'''
uso de listas de foreach
'''
# esta funcion unicamente va a generar una lista simple
# las listas son un tipo de datos que puede tener mas de una dato en su interior 
# los cuales funcionan por medio de indices. 
def lista_inicio() -> list:
    example_list = [] # la forma de declara una lista es igualar a []
    other_list = list() # segunda forma de declara una lista ambas son valias

    # agregar valores a la lista en python las listas pueden ser de mas de un tipo
    example_list.append(1)
    example_list.append("julian")
    example_list.append(True)
    print("los valores de example list son ", example_list) # concatenar revisar el archivo (inicio.py)

    other_list.append(1)
    other_list.append(2)
    other_list.append(3)
    other_list.append(4)
    print("los valores de other list son " + str(other_list)) # unicamente se pueden concatenar str es necesario realizar una convercion.
    join_list = example_list + other_list # las listas se juntan en una solo
    print(f"los valores de las dos listas son : {join_list}")
    return join_list

def list_managment():
    join_list = [1, 2, 3 , 4, 5, 5, 5] # se crea una lista con valores de inicio
    print(join_list[0]) # se accede al valor por medio de su indice, en un lenguaje de programacion el primer valor es 0
    print(join_list)
    join_list.remove(5) # elimina unicamente la primer concidencia
    print(join_list)
    print(join_list.pop()) # muesta el ultimo elemento de la lista
    join_list.insert(2, 100) # agrega un valor a la lista el primer argumento es el valor el segundo es la posición.
    print(join_list)
    join_list.sort(reverse= True) # funcion que ordena los valores
    print(join_list)

'''
las tuplas son parecidas a las lista la diferencia es que estas no se pueden cambiar son inmutables
'''
def example_tuple():
    tupla = (1, 2, 3, 4)
    # tupla[1] = 2 # esto tira un error  TypeError: 'tuple' object does not support item assignment
    print(tupla[0]) # se muestra por medio de indices.

'''
El for es una funcion ciclomatica se utiliza cuando se conoce el momento en que esta 
debe de detenerse a diferencia del while el cual es controlado por una accion externa, 
'''
def funcion_for():
    for i in range(0, 10):
        print(i)

def for_with_text():
    text = "Hello world"
    text_pass_for = ""
    text_reverse = ""
    for caracter in text:
        print(caracter)
        text_pass_for += caracter

    for caracter in text[::-1]: # con la sentincia del text -1 podemos decirle que inicie a partir del ultimo valor
        print(caracter)
        text_reverse += caracter
    print(text_pass_for)
    print(text_reverse)

# distingue los numero pares e impares de un rango de numero
def par_or_impar(limit: int):
    for i in range(0, limit):
        if i % 2 == 0:
            print(f"El numero {i} es un numero par")
        else:
            print(f"El numero {i} es un numero impar")
            
def show_par_or_impar(limit):
    list_par = []
    list_impar = []
    for i in range(0, limit):
        if i % 2 == 0:
            list_par.append(i)
        else:
            list_impar.append(i)
    print(f"Los numero pares son: {list_par}")
    print(f"Los numero impares son: {list_impar}")

example_tuple()
