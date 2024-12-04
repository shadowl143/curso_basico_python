try:
    fichero = open("POO/archivoss/index.html")
    print(fichero.readlines())
    for i in fichero.readlines():
        print(i)
    fichero.close()
    
except FileNotFoundError:
    print("archivo no encontrado")

# "c:/Users/Julian/Documents/Sabado 1/curso_basico_python/POO/archivoss/leer_archivos.py"