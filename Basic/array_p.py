# import array
# rolls = array.array("i", [101, 102, 103, 104])

from array import *


"""
rolls = array("i", [101, 102, 103])

print(rolls)

print(rolls[0])
print(rolls[1])
print(rolls[2])

print()

for i in rolls:
    print(i)


print()

for i in range(len(rolls)):
    print(rolls[i])

print()


i = 0
while i < len(rolls):
    print(rolls[i])
    i += 1

    
"""


#SECTION :      methods

#NOTE :     append
"""
marks = array("i", [24, 53, 14, 64, 23])

for i in marks:
    print(i)

print()

marks.append(24)
marks.append(82)

i = 0
while i < len(marks):
    print(marks[i])
    i += 1



salary = array("i", [])
length_salary = int(input("Enter salary array length:\n"))

#!   using of for loop
# for i in range(length_salary):
#     new_salary = int(input("Enter salary for array:\n"))
#     salary.append(new_salary)


#!   using of while loop
i = 0
while i < length_salary:
    new_salary = int(input("Enter salary for array:\n"))
    salary.append(new_salary)
    i += 1

print(salary)

"""

#NOTE :         insert method

"""
numbers = array("i", [1, 2, 3])

print(numbers)

numbers.insert(1, 99)
numbers.insert(3, 72)
numbers.insert(30, 72)

print(numbers)

"""

#NOTE :     pop() and pop(n)

"""
numbers = array("i", [1, 2, 3, 4, 5, 6])

print(numbers)

numbers.pop()

numbers.pop(1)
numbers.pop(0)

print(numbers)

"""

#NOTE :         remove() and index(pos)

"""
numbers = array("i", [11, 22, 33, 44, 55])

print(numbers)

numbers.remove(22)
numbers.remove(33)
print(numbers)

print(numbers.index(11))
print(numbers.index(33))
print(numbers.index(55))

"""

#NOTE :     reverse() and extend()

"""
numbers = array("i", [1, 2, 3, 4, 5])
print(numbers)
numbers.reverse()
print(numbers)




num1 = array("i", [1, 2, 3, 4, 5])
num2 = array("i", [6, 7, 8, 9, 10])

print(num1)
print(num2)

num1.extend(num2)

print(num1)
print(num2)

"""

#NOTE :         slicing

numbers = array("i", [1, 2, 3, 4, 5, 6, 7, 8, 9])

print(numbers)

print(numbers[0:5])
print(numbers[:5])

print(numbers[:])
print(numbers[5:])

print(numbers[1 : 8 : 2])
print(numbers[8 : 0 : -2])

print()

for i in numbers[len(numbers):0:-1]:
    print(i)