#SECTION :      basic
# items = ["String", 1, 1.5]

# print(items)
# print(id(items))
# print(items[0])
# print(items[-1])

# items[1] = 11

# print(items)
# print(id(items))


# x = list()
# print(x)
# print(type(x))

# print()

# y = list("Arunesh")
# print(y)
# print(type(y))

# print()

# z = list("12345")
# print(z)
# print(type(z))

# print()

# xx = list(range(5))
# print(xx)
# print(type(xx))


#!  list concatenation
# a = [1, 2, 3]
# b = [11, 22, 33]

# c = a + b

# print(c)


#!      repetition of list
# a = [1, 2, 3]
# print(a * 3)

# b = ["a", "b", "c"]
# x = b * 2

# print(id(b))
# print(id(x))


#!      Aliasing List
# a = [11, 22, 33, 44, 55]

# b = a

# a[0] = "A"

# print(a)
# print(id(a))

# print(b)
# print(id(b))


#!      copy list

#   1 - method
# a = [11, 22, 33]

# print(a)
# print(id(a))

# print()

# b = a.copy()

# a[0] = "A"

# print(a)
# print(id(a))

# print(b)
# print(id(b))


#       cloning list
# a = [11, 22, 33]

# b = a[:]

# print(a)
# print(id(a))

# print(b)
# print(id(b))



#SECTION :      loop
# items = ["a", "b", "c", "d", "e"]

# for i in items:
#     print(i)

# print()

# for i in range(len(items)):
#     print(f"{i} : {items[i]}")


# i = 0
# while i < len(items):
#     print(f"{i} : {items[i]}")
#     i += 1


#SECTION :      getting list item from users

# items = []

# print(items)


# length_items = int(input("Enter list length:\n"))

# for i in range(length_items):
#     item = int(input(f"Enter index of {i} : value\n"))
#     items.append(item)


# print(items)




#SECTION :      methods

# items = ["a", "b", "c", "d", "e"]

#!  append
# print(items)
# print(id(items))

# items.append("f")

# print(items)
# print(id(items))


#!      insert method
# print(items)
# print(id(items))

# items.insert(1, 11)

# print(items)
# print(id(items))


#!      pop()   and   pop(index)

# print(items)
# print(id(items))

# items.pop()
# x=items.pop()
# print(x)

# items.pop(0)
# items.pop(-1)
# x = items.pop(-1)
# print(x)

# print(items)
# print(id(items))


#!      remove

# print(items)
# print(id(items))

# items.remove("b")

# print(items)
# print(id(items))


#!      index

# print(items)
# print(id(items))

# x = items.index("c")
# print(x)

# print(items)
# print(id(items)) 


#!      reverse

# print(items)
# print(id(items))

# items.reverse()

# print(items)
# print(id(items))


#!      extend
# a = [1, 2, 3]
# b = [11, 22, 33]

# print(id(a))
# print(id(b))

# a.extend(b)

# print(a)
# print(b)

# print(id(a))
# print(id(b))


#!      count
# items.append("b")
# items.append("a")
# items.append("c")
# items.append("b")
# items.append("a")
# print(items)

# a = items.count("a")
# a = items.count("A")

# print(a)


#!      sort

# items = ["b", "d", "a", "e", "c"]
# items = [3, 2, 5, 1, 4]
# items = [1, "a", "2", 3]

# print(items)
# print(id(items))

# items.sort()

# print(items)
# print(id(items))


#!      clear

# print(items)
# print(id(items))

# items.clear()

# print(items)
# print(id(items))


#SECTION :      List Slicing

#NOTE :     1-D list slicing
# items = [11, 22, 33, 44, 55, 66, 77, 88, 99]

# for i in range(len(items)):
#     print(f"{i} : {items[i]}")

# print()

# print(items[:])

# print(items[2:])

# print(items[:2])

# print(items[1:5])

# print(items[-2:])

# #   default
# print(items[0:len(items):1])

# print(items[::2])

# print(items[1::2])
# print(items[1:8:2])
# print(items[:8:2])

# print(items[-7:-1])



#NOTE :         nested list slicing

# items = [
#     ["a", "b", "c"],
#     ["aa", "bb", "cc"],
# ]

# print(items)

# print(items[0])
# print(items[0][1])

# print()

# print(items[0][:])
# print(items[0][1:])
# print(items[0][:2])
# print(items[0][1:2])
# print(items)

# for i in items:
#     print(i)

# print()

# for i in items:
#     for j in i:
#         print(j)

#SECTION :      Nested List

#!      1 - Type
# x = [44, 55]
# a = [11, 22, 33, x]

# print(a)



#!      2 - Type
# items = [11, 22, [33, 44, 55]]

# print(items)
# print(items[0])
# print(items[-1][1])

# items[-1][1] = "Hello"
# print(items)

# print()

# for i in items:
#     print(i)


#!      3 - Type
# items = [[11, 22, 33], [44, 55]]

# print(items)

# items[1][0] = "Hello"

# print(items)


#NOTE :     nested list loop

#!      for loop

# #   1 - Type
# # items = [11, 22, [33, 44, 55]]
# items = [11, 22, [33, 44, 55], 66, 77, [88, 99]]


# #   without index
# for i in items:
#     if type(i) == list:
#         for j in i:
#             print(j)
#     else:
#         print(i)


# print()


# #       with index
# for i in range(len(items)):
#     if type(items[i]) == list:
#         for j in range(len(items[i])):
#             print(f"{j+i} : {items[i][j]}")
#     else:
#         print(f"{i} : {items[i]}")


# items = [1, 2, [3, 4], 5, [6, 7], [8, 9]]

# total = 0

# for i in items:
#     if type(i) == list:
#         for j in i:
#             total += j
#     else:
#         total += i

# print(total)




#!      while loop

# items = [11, [22, 33, 44], [55], 66, [77, 88], 99]

# i = 0
# while i < len(items):
#     if type(items[i]) == list:
#         for j in range(len(items[i])):
#             print(items[i][j])
#     else:
#         print(items[i])

#     i += 1


#SECTION :      passing list to function

# def fun(items):
#     print(items)

#     print()

#     for i in items:
#         print(i)

# items = [11, 22, 33, 44]

# fun(items=items)



#SECTION :      list functions

#NOTE :     filter()

# marks = [34, 26, 75, 62, 47, 83, 72, 71, 63, 89]


# #!      marks greater or equal to 60 filter
# def passing_marks(mark):
#     if mark >= 60:
#         return True

# result = filter(passing_marks, marks)
# print(result)
# print(type(result))

# print()
# result_a = list(filter(passing_marks, marks))
# print(result_a)
# print(type(result_a))

# print()

# for i in result:
#     print(i)


# print()

#!      marks greater or equal to 80

# topper = list(filter(lambda mark : mark >= 80, marks))
# print(topper)
# print(type(topper))


#NOTE :     map function

# items = [11, 22, 33]

# def add_items(item):
#     return item * 2

# # result = map(add_items, items)
# result = list(map(add_items, items))
# print(result)
# print(type(result))



#NOTE :     reduce

# from functools import reduce

# items = [1, 2, 3, 4, 5]

# result = reduce(lambda prev, next : prev + next, items)
# print(result)





