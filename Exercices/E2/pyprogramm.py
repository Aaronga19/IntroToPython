#--------------------------------------------------------------------------------------
"""
1

x = 2
y = 3

print("x =", x)
print("value of", x, '+', x, "is", (x+x))
print("x =")
print((x+y), "x =", (y+x))
"""
#--------------------------------------------------------------------------------------
"""
2 
rating = int(input("Enter an integer rating between 1 and 10")) 
print("Your number is", rating)
"""
#--------------------------------------------------------------------------------------
""" 
3
grade = 91
if grade >= 90:
    print("congratulations!, Your grade of", grade, "earns you an A in this course")
"""
#--------------------------------------------------------------------------------------
"""
4
print(27.5 + 2)
print(27.5 - 2)
print(27.5 * 2)
print(27.5 / 2)
print(27.5 // 2)
print(27.5 ** 2)
"""
#--------------------------------------------------------------------------------------
"""
5
radius = 2
pi = 3.14159

diameter = 2*radius
circunfer = 2*pi*radius
area = (pi*radius)**2
print("diam = {}, circunferencia = {}, area = {}".format(diameter,circunfer,area))
"""
#--------------------------------------------------------------------------------------
"""
6
numero = int(input("Proporcione un numero real"))
if (numero%2)==1:
    print('this number "{}" is odd'.format(numero))
elif (numero%2)==0:
    print('this number "{}" is even'.format(numero))
"""
#--------------------------------------------------------------------------------------
"""
7
if 1024%4 == 0:
    print("1024 es multiplo de 4")
if 10%2 == 0:
    print("10 es multiplo de 2")
"""
#--------------------------------------------------------------------------------------
"""
8
print('''
        number, square, cube
         {}      {}      {}
         {}      {}      {}
         {}      {}      {}
         {}      {}      {}
         {}      {}      {}
         {}      {}      {}'''
        .format(0,0**2,0**3,
                1,1**2,1**3,
                2,2**2,2**3,
                3,3**2,3**3,
                4,4**2,4**3,
                5,5**2,5**3))
"""             
#-------------------------------------------------------------------------------------
"""
9
#           Devuelve los valores en el codigo ascii
print(ord("B"))
print(ord("C"))
print(ord("D"))
print(ord("b"))
print(ord("c"))
print(ord("d"))
print(ord("1"))
print(ord("2"))
print(ord("$"))
print(ord("*"))
print(ord("+"))
print(ord(" "))
"""
#-------------------------------------------------------------------------------------

"""10
prim = int(input("Ingrese el primer numero: "))
seg = int(input("Ingrese el segundo numero: "))
terc = int(input("Ingrese el tercer numero: "))
lista = [prim, seg, terc]
suma = prim + seg + terc
print("Suma: ",suma)
promedio = suma / 3
print("promedio: ",promedio)
producto = prim * seg * terc
print("producto: ",producto)
smallest = min(lista)
print("MasPeque: ",smallest)
largest = max(lista)
print("MasGrande: ",largest)"""

##-------------------------------------------------------------------------------------
 # 11
prim = int(input("Ingrese el primer numero: "))
seg = int(input("Ingrese el segundo numero: "))
terc = int(input("Ingrese el tercer numero: "))
cuarto = int(input("Ingrese el cuarto numero: "))
quinto = int(input("Ingrese el quinto numero: "))

print(prim, seg, terc, cuarto, quinto, end="   ")