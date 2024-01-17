#SECTION :      Memory Location

"""
a = 1
print(id(a))

b = 2
print(id(b))

c = 2
print(id(c))

d = a
print(id(d))

a = 10
print(id(a))
"""


#SECTION :      Variables

"""
#NOTE :     valid variable names
x = 11
print(x)

X = 22
print(X)

name10 = "Arunesh"
print(name10)

full_name = "Arunesh kumar"
print(full_name)

fullName = "Aohan"
FullName = "Bohan"
print(fullName)
print(FullName)


#NOTE :     invalid variable names
# and = 33

# if = 10

# 10name = "Arunesh"

# $hey = "hello"

# full name = "Arunesh kumar"

# full-name = "Arunesh kumar"

"""


#SECTION :      data types

"""
#NOTE :       numbers
a = 1
print(a)
print(type(a))

b = "1"
print(b)
print(type(b))

c = -1
print(c)
print(type(c))


#NOTE :       float
a = 1.1
print(a)
print(type(a))



#NOTE :       complex
a = 1 + 1j
# print(a)
print(a + 1)
print(type(a))


#NOTE :       boolean
a = True
print(a)
print(type(a))

b = False

print(True + True)
print(True - True)
print(True - False)
print(False + False)


#NOTE :       strings
a = "Arunesh"
print(a)
print(type(a))




#NOTE :       list
a = [1, 2.2, "Hello", True, ["A", "B"]]

print(a)
print(type(a))
print(len(a))

print(a[0])
print(a[1])
print(a[-1])

a[0] = "Hello, Arunesh"
print(a)
print(a[0])

print()


#NOTE :     tuples
a = (1, 2.2, "Hello", [1, 2], ("a", "b"))

print(a)
print(type(a))
print(len(a))

print(a[0])
print(a[-1])



#NOTE :     range

#   0 1 2 3 4
a = range(5)
print(a)
print(type(a))
print(a[1])

for i in range(5):
    print(i)

#   2=start | 10=end | 2=skip
b = range(2, 10, 2)
print(b)

for i in range(1, 10, 2):
    print(i)

    


#NOTE :     set

#   set unorder, duplicate not allow

a = {1, 2, 1, "string", (1, 2)}
# a = {1, 2, 1, "string", (1, 2), ["a"]}
print(a)
print(type(a))



#NOTE :     set

x = {
    "firstName": "Arunesh",
    "lastName": "kumar",
    "age": 24.6
}

print(x)
print(type(x))

print(x["firstName"])


#NOTE :     Variable rule

# a = 1

a, b = 1, 2

print(a)
print(b)


print()


x = 1
y = 2

print(x)
print(y)

x, y = y, x

print(x)
print(y)



#SECTION :      Operators


#NOTE :     arithemetic operators

print(5 // 2)
print(-5 // 2)




#NOTE :      Comparison Operators

print(5 == 3)
print(5 > 3)
print(5 < 3)
print(5 >= 3)
print(5 <= 3)
print(5 != 3)





#NOTE :      Logical Operators

print(5 > 2 and 2 > 1)
print(5 > 2 and 2 < 1)
print(5 < 2 and 2 > 1)
print(5 < 2 and 2 < 1)

print()

print(5 > 2 or 2 > 1)
print(5 > 2 or 2 < 1)
print(5 < 2 or 2 > 1)
print(5 < 2 or 2 < 1)

print()

print(not(5 < 1))
print(not(5 > 1))


print()

print(5 > 2 and 100)
print(5 > 2 and 50 and 100)
print(5 > 2 and 5 > 1 and 100)

print(5 > 2 or 100)
print(5 < 2 or 51 or 100)





#NOTE :      Bitwise Operators

a = 10
b = 15

print("~a = ", ~a)
print("~b = ", ~b)

print("a&b =", a&b)
print("a|b =", a|b)
print("a^b =", a^b)
print("a<<b =", a<<b)
print("a>>b =", a>>b)



#NOTE :      Membership Operators

string = "In publishing and graphic design a document or a typeface content."

print("doc" in string)
print("docc" in string)
print("docc" not in string)

print("shin" in string)
print("shin" not in string)
print("shinn" not in string)



#NOTE :      Identity Operators

a = 10
b = "10"
c = 10

print(a is b)
print(a is c)

print(a is not b)
print(a is not c)





#NOTE :      Implicit Type conversion
# means -> type convete by complier

a = 5
b = 2
print(a / b)
print(type(a/b))

a = 1
b = 1.1
print(a + b)
print(type(a + b))



#NOTE :      explicit Type conversion
# means -> type converte by prog


a = 5
b = 2
c = a / b
print(c)
print(type(c))

int_c = int(c)
print(int_c)
print(type(int_c))


a = 1.1

print(a)
print(type(a))

int_a = int(a)
print(int_a)
print(type(int_a))


a = "1"
print(a)
print(type(a))

int_a = int(a)
print(int_a)
print(type(int_a))


name = "Arunesh"

print(name)
print(type(name))

tuple_name = tuple(name)
print(tuple_name)
print(type(tuple_name))



names = ["Aohan", "Bohan", "Cohan"]

print(names)
print(type(names))


tuple_names = tuple(names)
print(tuple_names)
print(type(tuple_names))


set_names = set(names)
print(set_names)
print(type(set_names))





#SECTION :      input print()

print("Arunesh kumar")

print('Arunesh kumar')

print("Arunesh", "kumar")

print(10)

print(10.5)

#   default
print("Arunesh", "kumar", sep=" ")

print("Arunesh", "kumar", sep="#")

#   sep= will not work here
print("Arunesh kumar", sep="$")


#   default      end="\n"
print("Arunesh", end=" ")
print("kumar")





a = 1
b = 2
print(a, b)
print(a, b, sep=" ") # default
print(a, b, sep="#")



#NOTE :     input

username = input("Enter your username:\n")
print(username)
print(type(username))



num1 = int(input("Num1 : "))
num2 = int(input("Num2 : "))
result = num1 + num2
print(result)

"""


#SECTION :      Conditional Statements

"""
# if 5 > 2:
if (5 > 2):
    print("5 is greater than 2")

print("Rest of Code")


num = int(input("Enter number:\n"))

if num > 1:
    print(num, "is greater than 1")
    if (num >= 10):
        print(num, "is greater than or equal to 10")



# if 5 > 1 and 10 > 3:
if 5 > 1 or 10 < 3:
    print("Correct Numbers")
else:
    print("Incorrect numbers")





if 5 > 2:
    print("5 is greater than 2")
else:
    print("5 is not greater than 2")


print("5 is not greater than 2") if 5 < 2 else print("5 is greater than 2")



if 10 >= 1:
    if 10 >= 5:
        print("10 is greater or equal to 5")
    else:
        print("10 is not greater or equal to 5")
else:
    print("10 is not greater than 1")





day = input("Enter valid day:\n").lower()

if day == "monday":
    print(f"Today is {day}")
elif day == "tuesday":
    print(f"Today is {day}")
else:
    print(f"Invalid day - {day}")





i = 1

while i <= 5:
    print(i)
    i += 1


print()


i = 2

while i <= 20:
    print(i)

    i += 2
else:
    print("While loop done!")




i = 1

while True:
    if i == 5:
        break

    print(i)

    i += 1

    



i = 1

while i <= 5:
    print(f"{i} : Outer While Loop")
    i += 1

    j = 1

    while j <= 5:
        print(f"\t{j} : Inner While Loop")

        j += 1



# range(0, end_num, step=1) <=> default

a = range(5)
print(a)


for i in range(5):
    print(i)

print()

for i in range(1, 5):
    print(i)

print()


#   1,  1+2=3, 3+2=5, ... 
for i in range(1, 10, 2):
    print(i)




# for i in range(1, 10, 1):
# for i in range(-1, -10, -1):
for i in range(10, 0, -1):
    print(i)


    


for i in "arunesh":
    print(i)



name = "Arunesh kumar"

for i in range(len(name)):
    print(f"{i+1} = {name[i]}")
else:
    print("For Loop Done!")





for i in range(1, 5):
    print(f"{i} : Outer For Loop")

    for j in range(1, 5):
        print(f"\t{j} : Inner For Loop")
    else:
        print("\tInner For Loop Done!")
else:
    print("Outer For Loop Done!")




for i in range(1, 10):

    if i == 3:
        # break
        continue
    print(i)
    

    
"""
