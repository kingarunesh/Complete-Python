#SECTION:       basic diff

# a = 1
# print(a)
# print(type(a))

# print()

# b = (1)
# print(b)
# print(type(b))

# print()

# c = (1,)
# print(c)
# print(type(c))



# items = (1, 2, 3)
# print(items * 4)


#SECTION :      tuple

# items = (1, 2.2, "String", [1, 2], {"key": "value"}, {"a", "b", "c"}, (1, 2))

# print(items)
# print(type(items))

# print(items[0])
# print(items[1])
# print(items[-1])




#NOTE :     for loop

# for item in items:
#     print(item)

# print()

# for i in range(len(items)):
#     print(f"{i} : {items[i]}")



#NOTE :     while loop

# print()

# i = 0
# while i < len(items):
#     print(f"{i} : {items[i]}")

#     i += 1


#SECTION :     slicing tuple

# items = (11, 22, 33, 44, 55, 66)

# for i in range(len(items)):
#     print(f"{i} : {items[i]}")

# print()

# print(items)

# print()

# print(items[:])
# print(items[1:])
# print(items[:5])
# print(items[1:5])
# print(items[-3:])
# print(items[-1:])
# print(items[::2])


#SECTION:       concatenation

# a = (1, 2, 3)
# b = (11, 22, 33)

# c = a + b

# print(c)


#SECTION :      modifying tuple elements

# items = (11, 22, 33, 44, 55)

# print(items)

# list_items = list(items)

# list_items[1] = "Hello"

# updated_items = tuple(list_items)

# print(updated_items)


# print(id(items))
# print(id(updated_items))


#SECTION :      delete tuples

# items = (11, 22, 33, 44, 55)

# print(items)
# print(id(items))

# list_items = list(items)

# del list_items[1]

# items = tuple(list_items)

# print(items)

# print(id(items))


#SECTION :      getting tuple element input from user

# items = []

# num_of_elements = int(input("Enter how many elements do you want?\n"))

# for i in range(num_of_elements):
#     element = int(input(f"Enter {i} index value:\n"))
#     items.append(element)

# items = tuple(items)

# print(items)


#SECTION :      Aliasing Tuples

# items = (11, 22, 33, 44)

# x = items

# print(items)
# print(x)

# print(id(items))
# print(id(x))



#SECTION :      copy tuples

# items = (11, 22, 33, 44)

# # a = items[:]
# a = items[:2]

# print(id(items))
# print(id(a))


#SECTION :      nested tuple


#NOTE :      1 - Type
# items = (11, 22, (33, 44, 55), 66, (77, 88), 99)

# print(items)
# print(type(items))
# print(len(items))


# print(items[0])
# print(items[2])
# print(items[2][1])


#!      for loop
# for item in items:
#     if type(item) == tuple:
#         for i in item:
#             print(i)
#     else:
#         print(item)

# print()

# for i in range(len(items)):
#     if type(items[i]) == tuple:
#         for j in range(len(items[i])):
#             print(f"{i} {j} : {items[i][j]}")
#     else:
#         print(f"{i} : {items[i]}")

#!      while loop
# print(items)
# print()

# i = 0

# while i < len(items):
#     if type(items[i]) == tuple:
#         for j in range(len(items[i])):
#             print(f"{i} {j} : {items[i][j]}")
#     else:
#         print(f"{i} : {items[i]}")
#     i += 1



#NOTE :      2 - Type
# items = ((11, 22, 33), (44, 55), (66, 77, 88, 99))

# print(items)
# print(type(items))
# print(len(items))

# print(items[0])
# print(items[0][1])


#!      for loop
# for i in items:
#     for j in i:
#         print(j)


#!      while loop
# i = 0
# while i < len(items):
#     j = 0
#     while j < len(items[i]):
#         print(f"{i} {j} : {items[i][j]}")
#         j += 1
#     print()
#     i += 1


#SECTION :      passing tuples in functions

# def fun(tup):
#     print(tup)


# items = (11, 22, 33, 44)

# fun(tup=items)