#SECTION :      basic

# items = {11, "String", 22.5, 11, (11, 22, 33)}

# print(items)
# print(type(items))
# print(len(items))
# print(id(items))


#NOTE :     add new item
# items.add("Arunesh")
# print(items)
# print(id(items))


# items.update([11, 22, 33, 44, 55])
# print(items)
# print(id(items))


#NOTE :     delete element

# print(items)
# print(id(items))

# items.remove("asdfg")
# items.remove("String")

# items.discard("asdfgh")
# items.discard("String")

# print(items)
# print(id(items))


#NOTE :     copy set

# items = {11, 22, 33, 44, 55}

# print(items)
# print(id(items))

# x = items.copy()

# print(items)
# print(id(items)) 


#NOTE :     clear set

# items = {11, 22, 33, 44, 55}

# print(items)
# print(id(items))

# items.clear()

# print(items)
# print(id(items))


#NOTE :         loop

# print(items)
# print()

# #!      for loop
# for item in items:
#     print(item)



#SECTION :      getting set element from user
    
# items = set()

# number_of_elements = int(input("Enter how many elements do you want:\n"))

# for i in range(number_of_elements):
#     element = int(input(f"Enter {i} element:\n"))
#     items.add(element)

# print(items)


#SECTION :      methods

first = {"aohan", "bohan", "cohan", "dohan", "eohan", "fohan"}
seocnd = {"ram", "cohan", "neha", "cohan", "aohan", "noora", "fohan", "niraj"}


#!      intersection
a = first.intersection(seocnd)
print(a)


#!      union
b = first.union(seocnd)
print(b)


c = first.difference(seocnd)
print(c)