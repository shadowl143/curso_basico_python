# import operacion_basica as o
from operacion_basica import OperacionesBasicas
from operacion_avanzada import OperacionAvanzada

# importacion y uso de una clase a esto se le conoce como instancia de un clase
intance_b = OperacionesBasicas(5.0, 3.0)
print(intance_b.sumar())


# se genera una instancia de operacion avanzada que hereda de una clase padre Operacion basica
operacion_avanzada = OperacionAvanzada(2.0, 3.0, "El resultado es: ")
operacion_avanzada.dividir_resultado_entero(3.0)










'''
Crear dos clases padre e hijo 
la clase padre me tiene que dar el nombre y la edad 
la clase hija me tienen que decir el nombre del padre  y el propio 
se vera reflajo desde el main de la app
'''