import sys
from numpy import *



#NOTE :         1

# def calculate(num1=1, num2=1, operator="+"):
#     if operator == "+":
#         print(f"{num1} + {num2} = {num1 + num2}")
#     elif operator == "-":
#         print(f"{num1} - {num2} = {num1 - num2}")
#     elif operator == "*":
#         print(f"{num1} * {num2} = {num1 * num2}")
#     elif operator == "/":
#         print(f"{num1} / {num2} = {num1 / num2:.2f}")
#     else:
#         print("Invalid data")

# calculate(num1=5, num2=3, operator="+")
# calculate(num1=5, num2=3, operator="-")
# calculate(num1=5, num2=3, operator="*")
# calculate(num1=5, num2=3, operator="/")
# calculate(num1=5, num2=3, operator="**")
# calculate(num2=50, num1=10, operator="*")
# calculate()
        

#NOTE :         2
# def aFun(x, y):
#     add = x + y
#     sub = x - y
#     return add, sub

# result = aFun(10, 5)
# print(result)

# add, sub = aFun(10, 5)
# print(add)
# print(sub)



#NOTE :         3

# def firstFun():
#     print("First Fun - First Line")

#     def secondFun():
#         print("Second Fun")
    
#     secondFun()
#     print("First Fun - Last Line")



# firstFun()


#NOTE :         4

# def firstFun(fun):
#     print("First Fun")
#     fun()

# def secondFun():
#     print("Second Fun")

# firstFun(secondFun)


# def firstFun(fun):
#     return "First Fun " + fun()
    
# def secondFun():
#     return "Second Fun"

# print(firstFun(secondFun))




#NOTE :         5

# def outerFun():
#     def innerFun():
#         return "Inner Fun"
#     print("Outer Fun")
#     return innerFun

# fun = outerFun()
# print(fun())

# def firstFun(fun):
#     print("First Fun")
#     return fun()


# def secondFun():
#     return "Seocnd Fun"

# fun = firstFun(secondFun)

# print(fun)

#NOTE :         6

# def fun(x, y):
#     print(x)
#     print(y)

# fun(1, 2, 3)

# def fun(x, *args):
#     print(x)
#     print(args)
#     print(args[0])
#     print(args[1])

# fun("AA", "B", "C")


# def fun(*args):
#     print(args)

#     sum = 0

#     for i in args:
#         sum += i
    
#     print(sum)

# fun(1, 2, 3, 4, 5)




#NOTE :         7

# def fun(x, **kwargs):
#     print(x)
#     print(kwargs)

#     print(kwargs["firstName"])
#     print(kwargs["lastName"])
#     print(kwargs["age"])

#     print()

#     for i in kwargs:
#         print(i)
    
#     print()

#     for key, value in kwargs.items():
#         print(f"{key} = {value}")


# fun(x="Hello", firstName="Arunesh", lastName="kumar", age=24.6, city="Bangalore")



#SECTION :      lambda

# def fun(a):
#     print(a)
# fun(1)

# first = lambda x : print(x)
# first(1)

# second = lambda x, y: x + y
# print(second(1, 2))

# third = lambda x=10, y=5: (x + y, x - y)

# add, sub = third(100, 50)
# print(add)
# print(sub)

# a, b = third()
# print(a)
# print(b)


# (lambda x : print(x + 1))(10)


#SECTION :      Local and Global Variables

#NOTE :     1

#!  global variable
# a = 0

# print(a)
# print()

# def fun():
#     global a
#     a = 50
#     print(a)

#!  local variable
#     b = 1
#     print(b)

# fun()

# print()
# print(a)


#NOTE :     2

# a = 10
# b = 20

# print(a)
# print()


# def fun():
#     a = 50
#     print(a)
#     x = globals()["a"]
#     print(x)
# fun()

# print()
# print(a)


#SECTION :      Recursion

# a = 0

# def fun():
#     global a
#     a = a + 1
#     print(f"{a} : Fun Call")
#     fun()

# # fun()
    
# import sys

# print(sys.getrecursionlimit())

# sys.setrecursionlimit(10)

# print(sys.getrecursionlimit())


#SECTION :      Pass or Call by Object

# def fun(x):
#     print(f"x = {x} | id = {id(x)}")
#     x = 50
#     print(f"x = {x} | id = {id(x)}")

# fun(10)

# print()

# x = 20
# fun(x) 



# def fun(arr):
#     print(f"Array = {arr} | id = {id(arr)}")
#     arr.append(10)
#     print(f"Array = {arr} | id = {id(arr)}")


# items = [11, 22, 33]
# print(f"items = {items} | id = {id(items)}")
# fun(items)
# print(f"items = {items} | id = {id(items)}")


#SECTION :      decorators

# def decorator(fun):
#     def inner():
#         print("First line")
#         fun()
#         print("second line")
#     return inner


# @decorator
# def fun():
#     print("Normal Function")


# # result = decorator(fun=fun)
# # result()
    
# # fun()
# # print()
# # fun()
    


# def calculateDecorator(num):
#     def inner():
#         print("Starting Line\n")

#         x = num()
#         print(x + 10)

#         print("\nEnding Line")
#     return inner


# @calculateDecorator
# def add():
#     return 10


# # add()


# def checkNumberDecorator(num):
#     def inner():
#         if num() > 0:
#             return True
#         else:
#             return False
#     return inner


# def checkDataType(num):
#     def inner():
#         if type(num()) == int:
#             return True
#         else:
#             return False
#     return inner


# @checkNumberDecorator
# @checkDataType
# def num():
#     return "1"

# print(num())



#!      pass array to function

# def fun(arr):
#     print(arr)
#     print(type(arr))
#     print(arr.dtype)

#     print()

#     for i in arr:
#         print(i)

# a = array([11, 22, 33])

# fun(arr=a)




#SECTION :      Generator

def a_fun(x, y):
    yield x
    yield y

a, b = a_fun(10, 20)
print(a)
print(b)

print()

result = a_fun(11, 22)
print(result)
print(type(result))

print(next(result))
# print(next(result))

print()

for i in list(result):
    print(i)