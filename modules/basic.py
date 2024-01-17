from datetime import datetime

#SECTION :      testing

#!      variable      
variable = "Variable"


#!      dict
my_dict = {
    "first_name": "Arunesh",
    "last_name": "kumar",
    "age": 24.6
}


#!      list
names = ["Aohan", "Bohan", "Cohan", "Dohan"]


#!      tuple
items = (1, 2, 3, 4, 5)


#!      set
groups = {"First", "Second", "Third"}


#!      function
def full_name(first_name, last_name):
    return f"{first_name} {last_name}"


#!      class

class MyClass:
    def __init__(self, first_name, last_name, birth_year, city):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.city = city
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_age(self):
        return datetime.now().year - self.birth_year

    def get_address(self, country):
        return f"{self.city}, {country}"





def test():
    print("basic.py = Testing")