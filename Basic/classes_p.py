#SECTION :      Basic about classes and object
#NOTE :      1 - Example
# class MyClass(object):
#     def hello(self):
#         print("Hello, Arunesh")


# obj1 = MyClass()
# obj1.hello()


#NOTE :      2 - Example
# class MyClass:
#     def __init__(self, last_name):
#         self.first_name = "Arunesh"
#         self.last_name = last_name

    
#     def greeting(self, age):
#         print(f"Hello, {self.first_name} {self.last_name}. Your age is {age}")



#!      without arguments
# obj = MyClass()
# obj.greeting()
# print(obj.first_name)

# print()
# obj.first_name = "Arunesh kumar"

# obj.greeting()
# print(obj.first_name)


#!      with arguments
# obj = MyClass()
# obj.greeting(age=24.6)
# print(obj.first_name)
        
#!      memory location - id()
# firstObj = MyClass(last_name="kumar")
# firstObj.greeting(age=24.6)
# print(firstObj.first_name)
# print(firstObj.last_name)
# print(id(firstObj))

# print()

# secondObj = MyClass(last_name="Ku")
# secondObj.greeting(age=25)
# print(secondObj.first_name)
# print(secondObj.last_name)
# print(id(secondObj))


#SECTION :      Constructor

#NOTE :     1 - Example
# class MyClass:
#     def __init__(self):
#         print("Constructor will call when we are creating class object.")

# obj = MyClass()


#NOTE :     2 - Exmaple
# class MyClass:
#     #!      constructor
#     def __init__(self, first_name, last_name="kumar"):
#         self.first_name = first_name    #!  Instance Variable
#         self.last_name = last_name
    
#     def personInfo(self, age):
#         city = "Bangalore"      #! Local Variable
#         print(f"Hello, {self.first_name} {self.last_name}. Your age is {age} and you are from {city}")
#         print(self.first_name)  #!   Accessing Instance Variable


# firstObj = MyClass(first_name="Arunesh", last_name="Ku")
# firstObj.personInfo(age=24.6)
# print(firstObj.first_name)
# print(firstObj.last_name)

# print()

# secondObj = MyClass(first_name="Arunesh")
# secondObj.personInfo(age=25)
# print(secondObj.first_name)
# print(secondObj.last_name)


#SECTION :      Variable Types ⬇️

#SECTION :     Instance Variable

# class MyClass:
#     def __init__(self):
#         self.first_name = "Arunesh"  #!  Instance Variable
    
#     def hello(self):
#         print(self.first_name)  #!  Accessing Instance Variable


# firstObj = MyClass()
# print(firstObj.first_name)
# print(id(firstObj))

# print()

# seocndObj = MyClass()
# print(seocndObj.first_name)
# seocndObj.first_name = "Ankesh"
# print(seocndObj.first_name)
# print(id(seocndObj))

# print()

# thirdObj = MyClass()
# print(thirdObj.first_name)
# print(id(thirdObj))



#SECTION :     Class Variable | Static Variable


#NOTE :     1 - Example
# class MyClass:
#     cv = "Class Variable"   #!  Class Variable

#     #!      Constructor
#     def __init__(self):
#         self.name = "Arunesh"  #!  Instance Variable

#     #!      Instance Method
#     def get_name(self):
#         print(self.name)  #!  Accessing Instance Variable

#     #!      Class Method
#     @classmethod
#     def is_class_variable(cls):
#         print(cls.cv)       #!   Accessing Class Variable


# firstObj = MyClass()

# firstObj.get_name()
# firstObj.is_class_variable()
# print(firstObj.cv)
# print(MyClass.cv)

# print()

# firstObj.cv = "Updated Class-Variable"
# # MyClass.cv = "Updated Class-Variable"

# print(firstObj.cv)
# print(MyClass.cv)
# firstObj.is_class_variable()



#NOTE :     2 - Example
# class MyClass:
#     info = "Class Variable"

#     @classmethod
#     def get_info(cls):
#         print(cls.info)


# firstObj = MyClass()
# secondObj = MyClass()
# thirdObj = MyClass()

# print(MyClass.info)
# print(firstObj.info)

# print()

# print(MyClass.info)
# print(secondObj.info)

# print()

# print(MyClass.info)
# print(thirdObj.info)

# print()
# print("------------------------------------------------------------")
# print()

# #ERROR :        both are diff
# # MyClass.info = "Updated Class-Variable"
# firstObj.info = "Updated Class-Variable"

# print(MyClass.info)
# print(firstObj.info)

# print()

# print(MyClass.info)
# print(secondObj.info)

# print()

# print(MyClass.info)
# print(thirdObj.info)



#SECTION :      NameSpace

# class MyClass:
#     #!      class namespace
#     info = "Class Variable NameSpace"

#     @classmethod
#     def get_info(cls):
#         print(cls.info)


# #!      firstObj & secondObj are instance namespace
# firstObj = MyClass()
# seocndObj = MyClass()



#SECTION :      Instance Method

# class MyClass:
#     info = "Class Variable"

#     def __init__(self):
#         self.first_name = "Arunesh"
#         self.last_name = "kumar"
    
#     #!      Instance Method
#     def get_person_details(self, age):
#         print(f"Hello, {self.first_name} {self.last_name}. Your age is {age}")


# firstObj = MyClass()
# firstObj.get_person_details(age=24.6)




#SECTION :      Accessor or Getter Method  and Mutator or Setter Method

# from datetime import datetime

# class Person:
#     def __init__(self, first_name, last_name, birth_year):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.birth_year = birth_year
    
#     def get_full_name(self):
#         return f"{self.first_name} {self.last_name}"

#     def set_age(self):
#         calculate_age = datetime.now().year - self.birth_year
#         self.age = calculate_age
#         return self.age

#     def get_full_details(self):
#         print(f"Hello, {self.get_full_name()}, Your age is {self.age}")


# person = Person(first_name="Arunesh", last_name="kumar", birth_year=1999)

# print(person.get_full_name())
# print(person.set_age())
# print(person.get_full_details())


#SECTION :      Class Method

#NOTE :        1 - Example

# class Mobile:
#     RAM = "16GB"

#     @classmethod
#     def get_class_method(cls):
#         print("Class Method Called...")
    
#     @classmethod
#     def get_details(cls, size, type):
#         cls.type = type
#         print(f"Display Size : {size}")
#         print(f"RAM : {cls.RAM}")
#         print(type)
#         print(cls.type)


# obj = Mobile()

# obj.get_class_method()
# Mobile.get_class_method()
# Mobile.get_details(size=6.5, type="SmartPhone")

# print()

# print(Mobile.type)
# print(Mobile.RAM)



#SECTION :      Static Methods

# class MyClass:
#     @staticmethod
#     def get_info(first_name):
#         print("Static Method Called...")
#         print(first_name)


# obj = MyClass()

# obj.get_info(first_name="Arunesh")


#SECTION :      Passing member of one class to another class

# class Student:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
    
#     def get_full_name(self):
#         return f"{self.first_name} {self.first_name}"


# class Teacher:
#     @staticmethod
#     def get_details(student):
#         print("----- Teacher Class -----")
#         print(f"Student First Name : {student.first_name}")
#         print(f"Student Last Name : {student.last_name}")
#         print(f"Student Full Name : {student.get_full_name()}")

# stu = Student(first_name="Arunesh", last_name="kumar")


# tea = Teacher()

# tea.get_details(student=stu)



#SECTION :      Nested Class

# class Army:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.gn = self.Gun()
    
#     def get_full_name(self):
#         return f"{self.first_name} {self.last_name}"
    
#     class Gun:
#         def __init__(self):
#             self.name = "AK47"
#             self.price = 150000
        
#         def get_gun_info(self):
#             return f"Gun name is {self.name} and gun price is {self.price}"

# arm = Army(first_name="Arunesh", last_name="kumar")

# print(arm.first_name)
# print(arm.get_full_name())

# print()

# print(arm.gn.name)
# print(arm.gn.price)
# print(arm.gn.get_gun_info())



#SECTION :      Inheritence

# class Father:
#     money = 1000

#     def __init__(self, address):
#         self.name = "Zzzzz"
#         self.phone = "8971818410"
#         self.address = address
#         print("Father Class - Constructor")

#     def show(self):
#         print("Parent class - Instance method")
    
#     def p_address(self):
#         print(f"Parent Class - Address : {self.address}")
    
#     @classmethod
#     def show_money(cls):
#         print(f"Parent Class - Money : {cls.money}")
    
#     @staticmethod
#     def stats():
#         print("Parent Class - Static Method")

# class Son(Father):
#     def __init__(self, address, country):
#         super().__init__(address=address)
#         self.city = "Delhi"
#         self.name = "Aohan"
#         self.country = country
#         print("Child Class - Constructor")

#     def display(self):
#         print("Child Class : Instance Method")
    
#     def get_country(self):
#         print(f"Child Class - Address : {self.country}")
    
#     def get_address(self):
#         print(f"Child Class - Country : {self.address}")

# child = Son(address="Noida", country="India")

# print("--------------- Parent Class Data Calling ---------------")
# print(child.name)
# print(child.phone)
# print(child.address)
# child.show()
# child.p_address()
# child.show_money()
# child.stats()

# print("--------------- Child Class Data Calling ---------------")
# print(child.city)
# print(child.name)
# print(child.country)
# child.display()
# child.get_country()
# child.get_address()


#SECTION :      Multi-Level Inheritance

# class Father:
#     def __init__(self):
#         print("----- Father-Class : Constructor -----")

#     def f_method(self):
#         print("Father-Class Method")


# class Son(Father):
#     def __init__(self):
#         super().__init__()
#         print("----- Son-Class : Constructor -----")

#     def s_method(self):
#         print("Son-Class Method")


# class GrandSon(Son):
#     def __init__(self):
#         super().__init__()
#         print("----- GrandSon-Class : Constructor -----")

#     def gs_method(self):
#         print("Grand-Son Class Method")


# gs = GrandSon()

# print()

# gs.gs_method()
# gs.s_method()
# gs.f_method()


#SECTION :      Hierachical Inheritance

# class Father:
#     def __init__(self):
#         print("Father-Class : Constructor")

#     def f_method(self):
#         print("Father-Class Method")

# class Son(Father):
#     def __init__(self):
#         super().__init__()
#         print("Son-Class : Constructor")

#     def s_method(self):
#         print("Son-Class Method")

# class Daughter(Father):
#     def __init__(self):
#         super().__init__()
#         print("Daughter-Class : Constructor")

#     def d_method(self):
#         print("Daughter-Class Method")


# beta = Son()
# print()
# beta.s_method()
# beta.f_method()

# print("\n\n\n\n")

# beti = Daughter()
# print()
# beti.d_method()
# beti.f_method()


#SECTION :      Multi-Level Inheritance & Method Resolution Order

# class Father:
#     def __init__(self):
#         super().__init__()
#         print("Father-Class : Constructor")

#     def f_method(self):
#         print("Father-Class : Method")

# class Mother:
#     def __init__(self):
#         super().__init__()
#         print("Mother-Class : Constructor")

#     def m_method(self):
#         print("Mother-Class : Method")

# class Son(Father, Mother):
#     def __init__(self):
#         super().__init__()
#         print("Son-Class : Constructor")

#     def s_method(self):
#         print("Son-Class : Method")


# s = Son()

# print("\n\n")

# s.s_method()
# s.f_method()
# s.m_method()


#SECTION :      Polymorphism

#NOTE :         Duck Typing

# class Duck:
#     def walk(self):
#         print("Thapak Thapak Thapak Thapak")

# class Horse:
#     def walk(self):
#         print("Tabdak Tabdak Tabdak Tabdak")

# class Cat:
#     def talk(self):
#         print("Meow Meow Meow Meow")


# def myFun(object):
#     if hasattr(object, "walk"):
#         object.walk()
#     elif hasattr(object, "talk"):
#         object.talk()

# d = Duck()
# myFun(object=d)


# h = Horse()
# myFun(object=h)


# c = Cat()
# myFun(object=c)


#SECTION :      Method OverLoading

# class MyClass:
#     def sum(self, a):
#         print("First Sum Method", a)
    
#     def sum(self):
#         print("Second Sum Method")


# obj = MyClass()

# obj.sum(10)



#SECTION :      Method Overring and Method with Super()

# class Add:
#     def sum(self, x, y):
#         print(f"Add : {x + y}")


# class Multi(Add):
#     def sum(self, a, b):
#         # super().sum(10, 5)
#         super().sum(x=a, y=b)
#         print(f"Multi : {a * b}")

# m = Multi()
# m.sum(a=10, b=20)



#SECTION :      Operator Overloading

print(10 + 10)
print(int.__add__(10, 10))


print("Arunesh" + "kumar")
print(str.__add__("Arunesh", "kumar"))


# import sys
# print(sys.version_info)