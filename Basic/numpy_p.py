# import numpy
from numpy import *


#SECTION :      array method

"""

# a = numpy.array([101, 102, 103, 104])
# a = numpy.array([101.1, 102.2, 103.3, 104.4])
# a = numpy.array([101, 102.2, 103, 104.4])
# a = numpy.array(["a", "b", "c", "d"])
a = array(["Aohan", "Ram", "Mahi", "Arunesh"])

print(a)

print(a.dtype)

a[1] = "Salman"

print(a[0])
print(a[1])
print(a[2])
print(a[3])


print()

for i in a:
    print(i)


print()

for i in range(len(a)):
    print(a[i])


print()

i = 0
while i < len(a):
    print(a[i])

    i += 1

"""


#SECTION :      linspace() method

#NOTE:   default

"""

# linspace(start=, stop=, num=50 endpoint=False, retstep=False, dtype=None, axis=0)


# x = linspace(start=1, stop=5, num=5, endpoint=True)
x = linspace(start=1, stop=7, num=5, endpoint=False)

print(x)

print(x.dtype)

print(x[0])
print(x[len(x) - 1])


print()

for i in x:
    print(i)


print()


for i in range(len(x)):
    print(f"{i} = {x[i]}")


print()

i = 0
while i < len(x):
    print(x[i])

    i += 1

print()

i = 0
while i < len(x):
    print(f"{i} = {x[i]}")

    i += 1

    
"""

#SECTION :      logspace()

"""

#NOTE :     default
# logspace(start=, stop=, num=50, endpoint=True, base=10.0, dtype=None, axis=0)

x = logspace(start=1, stop=5, num=5, endpoint=False, base=12.1)

print(x)

"""


#SECTION :      arange()

"""

#NOTE :     default
# arange(start=0, stop=, step=1, dtype=None)

# x = arange(stop=5)
# x = arange(start=1, stop=5)
x = arange(start=0, stop=10, step=2)

print(x)
print(x[1])
print(x.dtype)
print(type(x))


print()

for i in x:
    print(i)

for i in range(len(x)):
    print(f"{i} = {x[i]}")


print()


i = 0
while i < len(x):
    print(f"{i} = {x[i]}")

    i += 1

"""

#SECTION :      zeros()

"""

#NOTE :     default
# zeros(shape=, dtype=float, order="C")


# x = zeros(shape=5, dtype=float)
x = zeros(shape=5, dtype=int)

print(x)
print(x[0])

for i in x:
    print(i)


i = 0
while i < len(x):
    print(x[i])

    i += 1

"""

#SECTION :      ones()

"""

#NOTE :     default
# zeros(shape=, dtype=float, order="C")

# x = zeros(shape=5)
x = zeros(shape=5, dtype=int)

print(x)
print(x[0])

for i in x:
    print(i)

"""


#SECTION :      Mathematical Operations

"""

a = array([1, 2, 3, 4, 5])
b = array([1, 2, 3, 4, 5])

print(a)

# a = a + 5
# a = a - 5
# a = a * 2
# print(a)


c = a + b
print(c)


print()

for i in c:
    print(i)

"""

#SECTION :      Relational or Comparison Operators

"""

a = array([100, 200, 300, 400])
b = array([100, 2000, 3000, 400])

# result = a == b
# result = a > b
# result = a >= b
# result = a <= b
result = a != b

print(result)

"""


#SECTION : any() and all() and where() and nonzero()

"""

a = array([1, 2, 3, 4, 5])
b = array([1, 2, 33, 4, 55])

#!      any()
b = array([11, 22, 3, 44, 55])

#!      all()
# b = array([1, 2, 3, 4, 5])

c = a == b

print(c)
print(any(c))

print(all(c))



#!      where()
#   where(a > b, a, b)
#   a=True   and   b=False
#   if a is greater than b then a result else b

a = array([1, 2, 333, 4, 56])
b = array([1, 22, 33, 4, 55])

result = where(a > b, a, b)

print(result)



#!      nonzero()
#   return non-zero value index

x = array([1, 2, 0, 3, 4, 0, 5, 0])

result = nonzero(x)

print(result)

"""


#SECTION :      Aliasing Array   and   view()

a = array([10, 20, 30, 40, 50])

#!      aliasing
"""
b = a
print(a)
print(b)
print(id(a))
print(id(b))


#!      view()
b = a.view()

a[1] = 100
b[2] = 200

print(a)
print(b)

print(id(a))
print(id(b))

print(a)
print(b)



#!      copy()
b = copy(a)

a[1] = 100
b[2] = 200

print(a)
print(b)

print(id(a))
print(id(b))

"""

#SECTION :      getting user input

"""

user = int(input("Enter number of elements:\n"))

x = zeros(shape=user, dtype=int)



for i in range(user):
    element = int(input(f"Enter array {i} index value:\n"))
    x[i] = element

print(x)

for i in x:
    print(i)





i = 0
while i < user:
    element = int(input(f"Enter array {i} index value:\n"))
    x[i] = element

    i += 1

print(x)

"""

#SECTION :      Multi-Dimensional Array

"""

a = array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10]
])

print(a)
print(a.dtype)

print(a[0])
print(a[1])

print(a[0][0])
print(a[0][1])
print(a[0][-1])

print(a[1][0])
print(a[1][1])
print(a[1][-1])



a = array([
    ["A", "B", "C", "D", "E"],
    ["a", "b", "c", "d", "e"]
])

print(a)
print(a.dtype)

print(a[0])
print(a[1])

print()

print(a[0][0])
print(a[0][1])

print(a[1][0])
print(a[1][1])

"""


#NOTE :         for loop
"""
a = array([
    [11, 22, 33, 44, 55],
    [111, 222, 333, 444, 555]
])

print(a)

print()

for i in a:
    print(i)

print()

for i in a:
    for j in i:
        print(j)
    print()

print()

for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j])
    print()

print()

for i in range(len(a)):
    print(a[i])

print()

for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j])
    print()

"""

#NOTE :         while loop

"""

a = array([
    [11, 22, 33, 44, 55],
    [111, 222, 333, 444, 555]
])

i = 0
while i < len(a):
    j = 0
    while j < len(a[i]):
        print(a[i][j])

        j += 1
    
    print()

    i += 1

"""

#NOTE :     zeros method ( 2-D Array )

"""

#   3=rows   and   2=columns
a = zeros((3, 2), dtype=int)

print(a)
print(a.dtype)


for i in a:
    for j in i:
        print(j)

"""

#NOTE :         ones method (2-D Array)

"""

a = ones((3, 2), dtype=int)

print(a)
print(a.dtype)


for i in a:
    for j in i:
        print(j)
    print()

"""

#NOTE :     reshape method (2-D Array)

"""

a = array([1, 2, 3, 4, 5, 6, 7, 8])

#   2=rows  and     4=columns
x = reshape(a, (2, 4))

print(a)
print(x)

"""


#NOTE :     flatten

"""

a = array([
    [1, 2, 3, 4],
    [5, 6, 7, 8]
])

b = a.flatten()

print(a)
print(b)

"""


#NOTE :     input from user in 2-D Array

#!      for loop
"""

rows = int(input("Enter numbers of row you want:\n"))
columns = int(input("Enter numbers of column you want:\n"))

a = zeros((rows, columns), dtype=int)

print(a)

for i in range(len(a)):
    for j in range(len(a[i])):
        element = int(input("Enter element:\n"))
        a[i][j] = element


print(a)

"""

"""
#!      while loop

rows = int(input("Enter numbers of row you want:\n"))
columns = int(input("Enter numbers of column you want:\n"))

a = zeros((rows, columns), dtype=int)

print(a)


i = 0

while i < len(a):
    j = 0

    while j < len(a[i]):
        element = int(input("Enter element:\n"))

        a[i][j] = element
    
        j += 1

    i += 1


print(a)

"""

#NOTE :     Slicing 2-D Array

"""

a = array([
    [11, 22, 33],
    [44, 55, 66],
    [77, 88, 99]
])

print(a)
print(a[0])
print(a[0:1])

print()

print(a[0, :])
print(a[0, 1:])

print()

print(a[1, :])
print(a[1, 1:])
print(a[1, :2])

print()

print(a[:, :])
print(a[1:, :])
print(a[:2, :])
print(a[1:, 1:])

"""

#NOTE :     Attributes of Array

a = array([1, 2, 3, 4, 5])

b = array([
    [11, 22, 33],
    [44, 55, 66],
    [77, 88, 99]
])

print(sum(a))
print(sum(b))

print(prod(a))
print(prod(b))

print(sqrt(a))
print(sqrt(b))

"""

print(a.ndim)
print(b.ndim)

print()

print(a.shape)
print(b.shape)

print()

print(a.size)
print(b.size)

print()

print(a.itemsize)
print(b.itemsize)

print()

print(a.dtype)
print(b.dtype)

print()

print(a.nbytes)
print(b.nbytes)


"""

