"""
def cube(x):
    '''Calculate the cube of x'''
    x = x ** 3 
    return x
print(f"The cube of 2 is:", cube(2))"""

#------------------------------------------------------------------------------------------------------------
"""
def mistery(x):
    y = 0 
    for value in x:
        y+=value**2
    return y
print(f"La suma de los cuadrados de esta lista es: {mistery(x=[1,2,3,4,5])}")"""

#------------------------------------------------------------------------------------------------------------
"""
def seconds_since_midnigth(hrs,minut,sec):
    hours_in_seconds = (hrs)*(60*60)
    minutes_in_seconds = (minut*60)
    return hours_in_seconds+minutes_in_seconds+sec
print(f"Han pasado: {int(seconds_since_midnigth(1,60,2))} segundos.")
"""
#------------------------------------------------------------------------------------------------------------
"""
import datetime as dt
print(dt.datetime.today())
"""
#------------------------------------------------------------------------------------------------------------
"""print(round(8.536841))"""

#------------------------------------------------------------------------------------------------------------
grados = float(input("Inserte temperatura en 'Celcius':"))
def celciusToFarenheit(Celcius):
    Far = (9/5)*Celcius+32
    return round(Far,3)
print(f"{grados} grados Celcius son: {celciusToFarenheit(grados)} grados Farenheit")