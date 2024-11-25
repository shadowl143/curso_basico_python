try:
   # import mate #ModuleNotFoundError
   import math
except ModuleNotFoundError:
    print("la plibreria mate no se encuentra")
finally:
    print("Finally")

# es_una_suma = 0

def dividir_con_erro(number: int, other_number: int) -> None:
    
    try:
        internal_1 = number
        internal_2 = other_number
        result = internal_1 / internal_2 #ZeroDivisionError
        print(result)
    except ZeroDivisionError:
        print(f"no se puede divivir entre zero {internal_1} / {internal_2}")
    finally:
        try:
            print(result)
        except NameError:
            print("El resultado tiene un error no se puede mostrar")
try:

    edad = int(input("ingrese edad"))
except ValueError:
    print("El dato ingresado no es numero")
