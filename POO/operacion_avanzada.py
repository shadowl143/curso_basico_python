from operacion_basica import OperacionesBasicas #importacion del archivo que se va usar

'''
Ejemplo de clase hija "OperacionAvanzada" y una clase padre el cual heredara las funciones y atributos 
a la clase y hija sin necesidad de generar una instancia.
'''
class OperacionAvanzada(OperacionesBasicas):
    def __init__(self, number_one: float, number_two: float, hello:str) -> None:
        self.text = hello
        super().__init__(number_one, number_two)

    def dividir_resultado_entero(self, other_number: float) -> None:
        sumar = self.sumar()
        print(f"{self.text} {sumar // other_number}")
        print(sumar / other_number)


    def exponentes(self, other_number: float) -> None:
        sumar = self.sumar()
        print(f"{self.text} {sumar ** other_number}")
        print(sumar / other_number)