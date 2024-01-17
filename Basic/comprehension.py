#SECTION :      List Comprehension

#NOTE :     List Comprehension
#!      1 - Example
# items = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# x = []
# for i in items:
#     x.append(i + 1)
# print(x)

# xx = [i + 1 for i in items]
# print(xx)


#!      2 - Example
# a = []
# for i in range(10):
#     a.append(i + 1)
# print(a)

# x = [i + 1 for i in range(10)]
# print(x)

#!      3 - Example
# x = []
# for i in range(1, 21):
#     if i % 2 == 0:
#         x.append(i)
# print(x)

# even_numbers = [i for i in range(1, 21) if i % 2 == 0]
# print(even_numbers)

#!      4 - Example
# div_by_2_3 = [i for i in range(1, 21) if i % 2 == 0 if i % 3 == 0]
# print(div_by_2_3)


#!      5 - Example
# x = []
# for i in range(20):
#     if i % 2 == 0:
#         x.append(i)
#     else:
#         x.append("_")
# print(x)

# c_if_else = [i if i % 2 == 0 else "_" for i in range(20)]
# print(c_if_else)


#!      6 - Example

# marks = [23, 64, 24, 68, 45, 96, 23, 54, 82, 62]

# pass_students = [i for i in marks if i >= 60]
# print(pass_students)



#SECTION :      Set Comprehension

#!      1 - Example
# items = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
# new_items = set()
# for i in items:
#     new_items.add(i + 1)
# print(new_items)

# set_comp = {i + 1 for i in items}
# print(set_comp)

#!      2 - Example
# x = set()
# for i in range(10):
#     x.add(i + 1)
# print(x)

# a = {i + 1 for i in range(10)}
# print(a)
# print(type(a))

#!      2 - Example
# a = set()
# for i in range(20):
#     if i % 2 == 0:
#         a.add(i)
# print(a)

# b = {i for i in range(20) if i % 2 == 0}
# print(b)

#!      3 - Example
# a = set()
# for i in range(20):
#     if i % 2 == 0:
#         a.add(i)
#     else:
#         a.add(i * 1000)
# print(a)

# b = {i if i % 2 == 0 else i * 1000 for i in range(20) }
# print(b)



#SECTION :      Dictionary Comprehension

#!      1 - Exmaple
# a = {}
# for i in range(1, 6):
#     a[i] = i * 1000
# print(a)

# b = {i : i * 1000 for i in range(1, 6)}
# print(b)



#!      2 - Exmaple
# a = {}
# for i in range(1, 11):
#     if i % 2 == 0:
#         a[i] = i * 1000
# print(a)

# b = {i : i * 1000 for i in range(1, 11) if i % 2 == 0}
# print(b)



#!      3 - Exmaple
a = {}
for i in range(1, 11):
    if i % 2 == 0:
        a[i] = i * 1000
    else:
        a[i] = "_"
print(a)

b = {i : i * 1000 if i % 2 == 0 else "_" for i in range(1, 11)}
print(b)