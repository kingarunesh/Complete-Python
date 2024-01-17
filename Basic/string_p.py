#SECTION :       basic
# a = "Hello, Arunesh"
# print(a)

# b = 'Hello, Arunesh'
# print(b)

# c = """
#     Hello,
#     Arunesh
# """
# print(c)

# d = '''
#     Hello,
#     Arunesh
# '''
# print(d)

# e = "We can run 'Python' in VS Code"
# print(e)

# f = 'We can run "Python" in VS Code'
# print(f)

# g = "We can run \"Python\" in VS Code"
# print(g)

# h = 'We can run \'Python\' in VS Code'
# print(h)

# i = "We can run\tPython\tin VS Code"
# print(i)


#SECTION :      memory location
"""

a = "Arunesh kumar"
b = "Arunesh kumar"
print(id(a))
print(id(b))

c = a
print(id(c))

d = "Python"
print(id(d))

"""

#SECTION :      index

"""
a = "Arunesh kumar"

print(a[0])
print(a[1])
print(a[-2])

"""


#SECTION :      length

"""
a = "Arunesh kumar"
print(len(a))

"""


#SECTION :      loop

# a = "Arunesh kumar"

# for i in a:
#     print(i)

# print()

# for i in range(len(a)):
#     print(a[i])

# print()

# i = 0
# while i < len(a):
#     print(a[i])

#     i += 1


#SECTION :      Immutable String

#   you can reasign string but can not change char

"""
a = "Arunesh"
print(a)


#!      reasign
a = "kumar"
print(a)


#!      mutate
a[0] = "H"
print(a)

"""

#SECTION :      Repetition and Concatenation and Comparing

#!      Repetition

# print("$" * 10)

# a = "Arunesh"

# print(a)

# print(a * 5)

# print(a[0:2] * 5)
# print(a[1:5] * 5)

#!      Concatenation

# print("Arunesh" + "kumar")

# first_name = "Arunesh"
# last_name = "kumar"
# full_name = first_name + " " + last_name
# print(full_name)

# print("Arunesh" + last_name)
# print("Arunesh" , last_name)


#!      comparing
# a = "Arunesh"
# b = "Arunesh"
# c = "arunesh"

# print(a == b)
# print(a == c)

# a = "A"
# b = "B"

# print(a == b)

# print(a < b)
# print(a > b)





# print("%d" % 233)


#SECTION :      C Style Formatting

"""

print("%d" % 123)
print("%d %d" % (123, 456))
print("%d     %d" % (123, 456))
print("%f" % 123.456)
print("%f %f" % (123.456, 10.1))
print("%f" % 123.456789)
print("%f" % 123.4567891)
print("%s" % "Arunesh")
print("%s %s" % ("Arunesh", "kumar"))
print("%d %s" % (123, "Arunesh"))
# print("%d %s" % ("Arunesh", 123))
print("%s" % 123)
# print("%d" % "Arunesh")
print("%(name)s %(age)d" % {"name": "Arunesh", "age": 24.6})
print("%(name)s %(age)d" % {"age": 24.6, "name": "Arunesh"})

print()

print("%d" % 123)
print("%          d       Hello" % 123)
print("%+d" % 123)

print()

print("%10d" % 123)
print("%09d" % 123)
print("%.3f" % 123.456)
print("%.9f" % 123.456)
print("%9.2f" % 123.456)
print("%09.2f" % 123.456)
print("%9.2f" % 123456789.1234567)

"""

#SECTION :      Format Method

"""

print("{}".format(10))
print("{}".format("Arunesh"))
print("{} {}".format("Arunesh", "kumar"))

print("{0}".format(12))
print("{1} {0}".format(12, 11))

print("{num}".format(num=10))
print("{first_name} {last_name}".format(last_name="kumar", first_name="Arunesh"))

print()

print("{}".format(10))
print("{:d}".format(10))
print("{0:d}".format(10))
print("{num:d}".format(num=11))


print()


a = (11, 22, 33)
print("{0[0]} {0[2]}".format(a))

b = {
    "name": "Arunesh kumar",
    "age": 24.6
}

print("{0[name]} {0[age]}".format(b))
print("{0[name]:s} {0[age]:f}".format(b))
print("{info[name]:s} {info[age]:f}".format(info=b))
print("{name} {age}".format(**b))

"""


#SECTION :      f-string

"""

a = 10
b = 20.12
c = "Arunesh"

print(f"{a} {b}")
print(f"{a}           {b}")

print(f"{c} {a} {b}")


salary = 1234567654322345

print(f"{salary:,}")
print(f"{salary:_}")

"""

#SECTION :      string methods

"""

print("arunesh kumar".upper())

print("ARUNESH KUMAR".lower())

print("arunesh kumar".title())

print("arunesh kumar".swapcase())

print("ARUNESH KUMAR".swapcase())

print()

print("arunesh".isupper())
print("Arunesh".isupper())
print("ARUNESH".isupper())

print()

print("arunesh".islower())
print("Arunesh".islower())
print("ARUNESH".islower())

print()

print("arunesh kumar".istitle())
print("Arunesh kumar".istitle())
print("arunesh Kumar".istitle())
print("Arunesh Kumar".istitle())

print()

print("arunesh123".isdigit())
print("123arunesh".isdigit())
print("arunesh123kumar".isdigit())
print("12345".isdigit())

print()

print("arunesh123".isalpha())
print("123arunesh".isalpha())
print("arunesh123kumar".isalpha())
print("12345".isalpha())
print("arunesh".isalpha())

print()

print("arunesh123".isalnum())
print("123arunesh".isalnum())
print("arunesh123kumar".isalnum())
print("12345".isalnum())
print("arunesh".isalnum())

print()

print(" arunesh ".isspace())
print(" ".isspace())
print("          ".isspace())


print("         arunesh")
print("         arunesh".lstrip())
print("         arunesh         ".lstrip())

print("arunesh          ")
print("arunesh          ".rstrip())
print("         arunesh          ".rstrip())

print("         arunesh".strip())
print("arunesh      ".strip())
print("     arunesh     ".strip())


a = "arunesh kumar"
print(a.replace("a", "#"))

b = "arunesh kumar"
print(b.split(" "))

c = ["A", "r", "u", "n", "e", "s", "h"]
print("".join(c))




a = "We can run Python in VS-Code"

print(a.startswith("we"))
print(a.startswith("We"))

print(a.endswith("code"))
print(a.endswith("Code"))


"""