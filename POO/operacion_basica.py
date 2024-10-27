
class OperacionesBasicas(object): # una clase base en pyhthon siempre debe heredar de un object sse hace de esta manera respetando la doc de python

    # constructor un contructor siempre debe tener un argumento self el cual dice que se refiere a si mismo
    def __init__(self, number_one: float, number_two:float) -> None:
        # los valores de los argumentos no se podran usar al menos que se cree una variable 
        # dentro del self para ser usada.
        self.number_one = number_one
        self.number_two = number_two
        self.saludo = "hola amigos"
    
    # no es obligatorio poner ni tipo de dato ni variable de retorno pero se recomienda hacerlo en caso de no 
    # los argumentos seran tipo de dato any y si en su cuerpo tiene un return este tambien sera un any si no se expecifico cual es.
    def sumar_dos(self, number_one, number): 
        print(number + number_one)
    
    '''
    Los siguentes son ejemplos de funciones con retorno, todas las funciones dentro un a clase deben contener el argumento self.
    '''
    def sumar(self) -> int:
        print(self.saludo)
        result = self.number_one + self.number_two
        return int(result)

    def restar(self) -> str:
        result = self.number_one - self.number_two
        return result

    def dividir(self) -> float:
        result = self.number_one / self.number_two
        return result

    def multiplicar(self) -> float:
        result = self.number_one * self.number_two
        return result
