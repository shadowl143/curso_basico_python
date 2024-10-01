# En es el repaso de python.
# para comentarios de una sola linea.

'''
nosotros podemos escribir 
comentarios en mas de una linea.

Trabajar con concatenacion. es juntar variables o textos en una sola linea o sentencia este siempre sera un string.
'''

print('hello ' + 'world')

print(type("hello" + '1'))

print("hello" + '1')
# esta es la forma correcta de usar variables en paython declarar
hello ='hello'
world = 'world'
hello_world = "hello world"

## no es buena practica en python
Hello = 'HELLO'
WORLD = "world"
## aqui terminan las malas practicas.
print("%s %s" % (Hello, WORLD))
print("{}{}".format(hello, world))
print("{1}{0}".format(hello, world))
print(hello, world)
print(f"{hello} {world}")


