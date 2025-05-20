# function overloading not allowed in python
# only function overrding allowed in python

# def wish():
#     print(f"Good Day!")


#  PascalCase - Classes - HelloClass
# snake_case - functions and variables etc - total_amount
# camelCase not recommended

def wish(name):
    print(f"Welcome to Coding {name}")

# wish() Will throw error as wish() is override by wish(name). Python doesn't support function overloading
wish("krishna")


def formate_names(f_name, l_name):
    return f"{f_name} {l_name}"

print(formate_names("Krishna", "Singh"))


def substract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "-": substract,
    "*": multiply,
    "/": divide
}

print(operations["-"](2,1))
print(operations["*"](5,3))



# global variables cannot be modified/used directly in a function
enemies = 10
def increase_enemies():
    enemies = 2
    print(enemies)

increase_enemies()

# global variables cannot be modified/used directly in a function
enemies = 10
def use_global():
    global enemies  # global keyword to use global keyword
    enemies += 1    # Never modify it in local scope, Only read global variables
    print(enemies)

use_global()

# How to avoid modifying global variable, return with modified value, or create new variable
g_enemies = 10
def use_global():
    global g_enemies
    return g_enemies + 1

print(use_global())

# give caps to constants
PI = 3.47
def print_pi():
    print(PI)
print_pi()


class MyClass:
    # id = 0  # skip these values as
    # name = ""

    def __init__(self, id, name):
         # constructor in python
         self.id = id
         self.name = name
         # print(f"New object created with  = {self.id} name = {self.name}")

    def method(self):
        print(f"first python class id = {self.id} name = {self.name}")

my_class_object1 = MyClass(10, "arora")
my_class_object2 = MyClass(1, "Krishna")

my_class_object1.method()
my_class_object2.method()


















