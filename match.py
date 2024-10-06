def example_match(level_person:str, money:int):
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
money = int(input("coloca una cantidad"))
show_print = example_match(result, money)
print(show_print)