#----------------------------------------------------------------------
                                    # 1
"""passes = 0
failures = 0  

# process 10 students
lista = [0,1,2,3,4,5,6,7,8,9]

for student in lista:

    print("estudiante:", student)
    result = int(input('Enter result (1=pass, 2=fail): '))
    
    if result == 1:
        passes = passes + 1 
    
    elif result == 2:
        failures = failures + 1
    
    else:
        print("Numero invalido")

print('Passed:', passes)
print('Failed:', failures)

if passes > 8:
    print('Bonus to instructor')
#
paso = 0
total = 0
nopaso = 0
valor = 0
while valor != 1 or valor != 2:
    valor = int(input("Ingrese el estado (1=aprobar, 2 = reprobar, 3=  finish): "))
    if valor == 1:
        paso += 1
        total  += 1
    elif valor == 2:
        nopaso += 1
        total += 1
    elif valor == 3:
        break
    else:
        print("Numero invalido")

print('Passed:', paso)
print('Failed:', nopaso)
if paso == 80% total:
print('Total:', total)"""
#----------------------------------------------------------------------
                            # 2
"""a = b = 7
print(f'a =  {a} \nb =  {b}')"""
#----------------------------------------------------------------------
                            # 3
"""for row in range(10):
    for column in range(10):
        print("<" if row % 2 == 1 else ">", end=" ")
    print()"""
#----------------------------------------------------------------------
                            # 4
"""for row in range(2):
    for column in range(7):
        print("@" if row % 2 == 1 else "@", end="")
    print() """
#----------------------------------------------------------------------
                            # 5
"""if number1 == number2:
    print(number1, 'is equal to', number2)
else:
    print("it isn't")

if number1 < number2 or number2 > number1:
    print(number1, 'is less than', number2)

if number1 <= number2 or number2 >= number1:
    print(number1, 'is less than or equal to', number2)"""
#----------------------------------------------------------------------
                            # 6 
"""print("What's your problem? ")
input("...  ")
answer = input("Have you had this problem before(Yes or No?")
if answer == "Yes":
    print("Well")
if answer == "No":
    print("Well, you have it now")"""
#----------------------------------------------------------------------
                            # 7
"""
print("number  square  cube")
for row in range(5):
    row += 1
    for column in range(3):
        column += 1
        
        if row % 2 == 1:
            print(f"{row**column:>6}", end=" ")
        else:
            print(f"{row**column:>6}", end=" ")
    print()
    """
#----------------------------------------------------------------------
                                        # 8
"""lista = []                            
while len(lista) <= 2:
    numero = int(input("Ingrese el número: "))
    lista.append(numero)
    print("Asi va la lista", lista)
print(f"La lista completa es ===== {lista} ======")
suma = lista[0] + lista[1] + lista[2]
print("Suma: ",suma)
promedio = suma / len(lista)
print("promedio: ", promedio)
producto = lista[0] * lista[1] * lista[2]
print("producto: ",producto)
smallest = min(lista)
print("MasPeque: ",smallest)
largest = max(lista)
print("MasGrande: ",largest)"""
#----------------------------------------------------------------------
                                         # 9
"""inp = []
while len(inp) <= 4: 
    dig = int(input("Ingrese un número: "))
    inp.append(dig)

print(inp, end="   ")

print("|// = ", 2//2, "| % =", 4%2, "|/ =", 1/2)"""
#----------------------------------------------------------------------                             # 10 CHULADA

p = 1000
r = 0.07
años = int(input("Cuantos años de estimacion? "))
for years in range(años):
    years += 1
    amount = p*(1 + r)**years
    print(f"Año: {years:>3} | Se tiene la cantidad de: {round(amount,2):>10} - USD")
    if years % 10 == 0:
        print("====================================================")

#----------------------------------------------------------------------
                                        # 11
"""
gas = 0 
average = []
while gas != -1:
    gas = float(input("Cuanto combustible has utilizado? [lts] (-1 para terminar) "))   
    if gas == -1:
        break                              
    distance = float(input("Cuanta distancia recorriste? [mts] "))
    result = round(distance/gas,6)
    print("Las millas/galon para este tanque fueron: ", result)
    average.append(result)
    
print("Promedio entre las totales: ",sum(average)/len(average))
"""
#----------------------------------------------------------------------
                                        # 12
"""
#num = int(input("Cual es el número factorial que desea? "))
def factor(num):
    for n in range(num):
        fact=1
        for m in range(1, n+2):
            fact *= m    
    return fact
        #print("\n\tEl número factorial es: ",fact)
print(factor(5))
"""
#----------------------------------------------------------------------
                                        # 13
"""
print("Pi =", 4-(4/3)+(4/5)-(4/7)+(4/9)-(4/21)-(4/530))
"""
#----------------------------------------------------------------------
                                        # 14
"""
e = 1
f = 0
for n in range(10): 
    n += 1
    e += (1/factor(n))
print("e =",e)
"""
#----------------------------------------------------------------------
                                        # 15
"""
for row in range(10):
    row += 1
    for column in range(1):
        column += 1
        if row < 3:
            print("*", end=" ")
        elif row < 5:
            print("* *", end=" ")
        elif row < 7:
            print("* * *", end=" ")

    
    print()
"""
#----------------------------------------------------------------------
