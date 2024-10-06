'''
Este es un ejemplo para utilizar el match.
Las funciones pueden admitir variables que se van a utilizar 
durante el proceso del mismo. A esto se le conoce como una funcion con parametros
'''

def tax_by_level_person(level_person:str, money:int):
    vip_tax = 10
    normal_tax = 20

    match level_person:
        case "vip":
            return money * (1 + (vip_tax/100)) # money * 1 * .10
        case "normal":
            return money * (1 + (normal_tax/100)) # money * 1 * .10
        case _:
            return  money * (1 + (30/100)) 
        
result = input("Escribe el nivel del cliente?")
# todos los datos que ingresa el usuario la funcion input lo lee como str
# es necesario hacer una conversion de dato ya que se van a hacer operaciones aritmeticas.
money = int(input("coloca una cantidad"))

# se hace uso de la funcion con los dos parametros anteriormente usado.
repeat = True
while(repeat):
    show_print = tax_by_level_person(result, money)
    print(show_print)
    option = input("Desea obtener otro impuesto? \n 1.- Si \n 2.- No")
    if(option.lower() =='2'.lower()):
        repeat = not repeat
    elif(option.lower() =='1'.lower()):
        repeat = True
    else:
        print("Se presento un error en el sistema no es posible continuar")
        repeat = False