class ExampleDictionary(object):

    def __init__(self) -> None:
        pass
    

    def mensaje(value: int) -> None:
        print(f"El valor fue {value}")

    def mi_primer_diccionario(self) -> dict:
        dic = {}
        dic.setdefault("name", "Leo")
        dic.setdefault("surname", "Tortuga")
        # print(dic)
        return dic
    def opciones(self) -> dict:
        dic = dict()
        dic.setdefault(1, mensaje(1))
        dic.setdefault(2, mensaje(2))
        dic.setdefault(3, mensaje(3))
        return dic

example_dictionary = ExampleDictionary()
mi_primer = example_dictionary.mi_primer_diccionario()
mi_primer_II = mi_primer.copy()
print(id(mi_primer_II))
print(id(mi_primer))
print(mi_primer.items())
print(mi_primer.keys())
print(mi_primer.get("name"))
mi_primer.setdefault("edad", 1)
mi_primer.setdefault("name", "leonardo")
mi_primer.pop("name", "Leo") #eliminar el dato
mi_primer.pop("surname") #eliminar el dato

mi_primer.pop("name", "Leo") #eliminar el dato
print(mi_primer.items())
print(mi_primer_II.items())

def mensaje(value: int) -> None:
    return f"El valor fue {value}"

clave = 5
if clave == 1:
    mensaje(1)
elif clave == 2:
    mensaje(2)
elif clave == 3:
    mensaje(3)
elif clave == 5:
    mensaje(5)
elif clave == 6:
    mensaje(6)
elif clave == 7:
    mensaje(7)
else:
    "no valido"

ejemplo_opcione = example_dictionary.opciones()
ejemplo_opcione.setdefault(5, "valor 5")
result = ejemplo_opcione.get(1)