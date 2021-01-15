# Is important the "Pseudocode" and the the "Flowcharts"

                                # FOR CYCLE & RANGE
for character in "Programming":
    print(character, end="  ")

total = 0
for number in [2,-3,0,17,9]:
    total += number
print("\n\ntotal:", total)

for counter in range(10):
    print(counter, end=" ") 
for number in range(5,10):
    print(number, end=" ") #  Delimitar el rango
for number in range(0,10,2):
    print(number, end=" ")  # Delimitar el rango con los pasos colocados
for number in range(10,0,-2):
    print(number, end=" ")  # Lo mismo pero en reversa
for number in range(99,-1,-11):
    print(number, end=" ")   

total = 0
for number in range(2,101,2):
    total += number
print(f"Aqui esta el total: {total}") 
#----------------------------------------------------------------------


"""Class average program with sequencecontrolled repetition."""

                            # initialization phase
total = 0 
grade_counter = 0
grades = [98, 76, 71, 87, 83, 90, 57, 79, 82, 94] 
 
# processing phase
for grade in grades:
    total += grade 
    grade_counter += 1 

# termination phase
average = total / grade_counter
print(f'Class average is {average}')               #--  it's a mode to give format to the string

#----------------------------------------------------------------------
# Some caracteristics about print

print("\n", 10, 20, 30, sep=", ")

#----------------------------------------------------------------------


"""Class average program with sentinelcontrolled iteration."""
                                # initialization phase
total = 0 # sum of grades
grade_counter = 0 # number of grades entered
# processing phase

grade = int(input('Enter grade, -1 to end: '))
# get one grade
while grade != -1:
    total += grade
    grade_counter += 1
    grade = int(input('Enter grade, -1 to end:'))
# termination phase     
if grade_counter != 0:
    average = total / grade_counter
    print(f'Class average is {average:.2f}') # -- We have to consider the number of decimals
else:
    print('No grades were entered')

#----------------------------------------------------------------------

"""Using nested control statements to analyze examination results."""
                                # If else For
                                # initialize variables
passes = 0  # number of passes
failures = 0  # number of failures

# process 10 students
for student in range(10):
    # get one exam result
    result = int(input('Enter result (1=pass, 2=fail): '))

    if result == 1:
        passes = passes + 1
    else:
        failures = failures + 1

# termination phase
print('Passed:', passes)
print('Failed:', failures)

if passes > 8:
    print('Bonus to instructor')

#----------------------------------------------------------------------
                        # Decimal point

amount = 112.31
print(amount)
print(f"{amount:.20f}")
from decimal import Decimal # import decimal.Decimal

principal = Decimal("1000.00")
rate = Decimal("0.05")

print(f"principal: {principal}")
print(f"rate: {rate}")

x =Decimal("10.5")
y = Decimal("2")
print(x+y)
print(x**y)
print(x%y)
print(x//y)
x+=y
print(x)


for amountyear in range(1,11):
    amount = principal*(1+rate)**amountyear
    print(f"{amountyear:>2}{amount:>10.2f}")

#----------------------------------------------------------------------
                        # Breaks y continue para While & For

for number in range(100):
    if number == 10:
        break
    print(number,end=" ")
print("\n")
for number in range(10):
    if number == 5:
        print(f" \nEstamos en el if: {number}")
        continue
    print(number,end=" ")

#----------------------------------------------------------------------
                        # Booleans

gender = 'Female'; age = 70

if (gender == 'Female') and (age >=65):
    print("Senior Female")

semesterAverage=83; finalExam = 95

if semesterAverage >= 90 or finalExam >= 90:
    print("Student gets an A")

grade = 87

if not grade == -1:
    print("The next grade is", grade)
                # Or
if grade != -1:
    print("The next grade is", grade)

#----------------------------------------------------------------------
                        # Intro to Dada Science

grades = [85,93,45,89,85]

print("mean by hand:",sum(grades)/len(grades))

import statistics

print("mean from module imported:", statistics.mean(grades))
print("median from module imported:", statistics.median(grades))
print("mode from module imported:", statistics.mode(grades))

print("sorted grades:",sorted(grades))


