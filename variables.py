# uso de variables.

'''
Las buenas practicas en python dicen que las variables en minusculas en caso de ser mas de una 
palabra estas deben separarse por un _,
una variable es un tipo de dato que puede cambiar su valor durante el proceso.
'''
# primer forma en que se puede declarar una variable, toma el tipo de dato dependiendo del valor que se le da
name = "julian" # tipo da datos string se utiliza para variables de tipo texto
number = 1 # tipo de dato numerico se utiliza cuando se necesita hacer operaciones aritmeticas
money = 12.50 # cuando el numero es decimales tiene se llama flotante
estado = True # las variables de tipo boleandas solo tienen dos valores True or False

'''
para ver el tipo de una variable se utiliza la funcion type y para mostrar en pantalla
la funcion type.
'''
print(f"El tipo de dato: {type(name)} tiene un valor de {name}")
print(f"El tipo de dato: {type(number)} tiene un valor de {number}")
print(f"El tipo de dato: {type(money)} tiene un valor de {money}")
print(f"El tipo de dato: {type(estado)} tiene un valor de {estado}")

# si las variables no tienen un valor se le puede especificar directamente para despues darle un valor
score:float
surname:str
result: int
turn:float
active:bool

# print(score) #NameError: name 'score' is not defined (no tiene un valor y muestra un error)
score = money # la variable tiene el mismo valor que money
print(score)
money = 120.90
print(score) # score guardar el valor de money 
print(money) # money cambio su valor pero score aun mantiene el valor de score
