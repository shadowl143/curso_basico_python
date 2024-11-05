from datetime import date
from threading import Timer



class UsoTimer(object):
    def __init__(self) -> None:
        pass
    
    def week_day(day:int):
        week = dict({1, "lunes"},{2, "martes"}, {3, "miercoles"}, {4, "jueves"},
                     {5, "viernes"}, {6, "sabado"}, {7, "domingo"})
        value = week.get(1)
        print(value)
        keys = week.keys()
        print(keys)
        values = week.values()

# uso_timer = UsoTimer()
# uso_timer.week_day()

_date = date.today()
print(_date.weekday())
print(_date.toordinal())
print(_date.isoformat())
print(_date.fromordinal((_date.isoweekday * 365))) # muestra la fecha segun la cantidad de dias trancurrido
print(_date.isoweekday()) # muestra el dia de la semana 
print(_date.fromisocalendar(2024, 44, 6)) # obtiene una fecha de acuerdo al año, el numero de la semana y el numero del dia de la semana muestra la fecha del calendario

        