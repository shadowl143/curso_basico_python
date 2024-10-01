# vamos a ver ejemplos de operadores aritimicos.

sum = 5 + 10 # 15
division = 5 / 2 # 2.5
resta = 10 - 8 # 2
multiplicacion = 5 * 2 # 10
potencia = 3**5 # 3 * 3 * 3 * 3 * 3 = 247
residuo = 10 % 2 # residuo de una division = 0
dision_enteros = 5 // 2 # resultado en enteros sin decimales = 2

print(sum)
print(division)
print(resta)
print(multiplicacion)
print(potencia)
print(residuo)
print(dision_enteros)

'''
Orden en que se ejecutan las operaciones.
1. Resolver las operaciones dentro de paréntesis, corchetes o llaves
2. Resolver los exponentes
3. Resolver las multiplicaciones y divisiones de izquierda a derecha
4. Resolver las sumas y restas de izquierda a derecha
'''

resultado_prioridad = (5 + 6) * (4 * (3*2))/5 + 4 - 2 * 2 ** 3
print(resultado_prioridad) # el resultado es 40.8