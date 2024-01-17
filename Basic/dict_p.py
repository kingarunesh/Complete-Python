#SECTION :      basic

# info = {
#     "first_name": "Arunesh",
#     "last_name": "kumar",
#     "age": 24.6,
#     "city": "Bangalore"
# }


# print(info)
# print(type(info))
# print(len(info))
# print(info["first_name"])


# print()


# first = {
#     101: "First",
#     102: "Seocnd",
#     "hello": "Hello, Arunesh"
# }

# print(first)
# print(first[101])
# print(first["hello"])




# items = {
#     "first_name": "Arunesh",
#     "last_name": "kumar",
#     "age": 24.6,
#     "city": "Bangalore"
# }

# print(items)
# print(id(items))
# print()


#!      edit item
# items["city"] = "Delhi"



#!      add new item
# items["phone"] = "8971818410"



#!      delete item
# del items["city"]


#!      delete dict
# del items


#!      clear dict
# items.clear()


#!      copy dict
# x = items.copy()

# print(x)
# print(id(x))



#!      check key exits or not
# print("first_name" in items)
# print("home" in items)
# print("address" in items)
# print("address" not in items)


#!      get dict items
# print(items["first_name"])
# print(items.get("first_name"))
# print(items.get("asdfghj", "Invalid Key"))


#!      items()
# print(items.keys())
# print(items.values())
# print(items.items())

# print()

# for key in items.keys():
#     print(key)

# print()

# for value in items.values():
#     print(value)

# print()

# for key, value in items.items():
#     print(f"{key} : {value}")



#!      pop()

# items.pop("first_name")
# x = items.pop("sdfgh", "Invalid Key")
# print(x)

# print(items)
# print(id(items))



#SECTION :      gettingdict items from user

# my_dict = {}

# number_of_elements = int(input("Enter how many numbers of element do you want:\n"))

# for i in range(number_of_elements):
#     key = input(f"Enter {i} key:\n")
#     value = input(f"Enter {key} value:\n")

#     my_dict[key] = value


# print(my_dict)