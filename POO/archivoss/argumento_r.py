# fichero = open("POO/archivoss/helloworld.txt", "r")
# print(fichero.read())
# fichero.close()

# with open("POO/archivoss/helloworld.txt", "r") as fichero:
#     linea = fichero.readline()
#     while linea != '':
#         linea = fichero.readline()
#         print(fichero.read())
# with open("POO/archivoss/no existe.txt", "w") as fichero:
#     fichero.write("esta es una nueva linea")
# with open("POO/archivoss/helloworld.txt", "a") as fichero:
#     fichero.write("esta es una nueva linea")
try:
    with open("helloworld.txt", "x") as fichero:
        fichero.write("esta es una nueva linea")
except FileExistsError:
        print("El archivo ya existe")
