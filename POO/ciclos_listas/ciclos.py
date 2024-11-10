import time
import custom_input as ci
class Ciclos(object):
    def __init__(self) -> None: # this.start
        pass
    
    def start_uno(self):
        value_start = ci.only_number("Ingrese un numero")
        limit = ci.only_number("Ingrese un limite")
        counter = time.time()
        self.recursividad(value_start, limit)
        counter_end = time.time()
        print(counter, counter_end)

     
    def start_dos(self):
        value_start = ci.only_number("Ingrese un numero")
        limit = ci.only_number("Ingrese un limite")
        self.foreach(value_start, limit)

    def recursividad(self, value: int, limit: int):
        if value < limit:
            print(value%2==0)
            value+=1
            self.recursividad(value, limit)

    def foreach(self, value: int, limit: int):
        for value in range(limit):
            print(value)

ciclos = Ciclos()
ciclos.start_uno()
ciclos.start_dos()

# print(id(ciclos))
# print(id(ciclos2))
# print(id(ciclos3))

# print(ciclos is ciclos2)
# print(ciclos is ciclos3)

# a = "hola"
# b = "hola"
# print(a == b)
# print(a is b)

# print(a*100 is b*100)
# print(a*100 == b*100)
