# Write your code below this line 👇
print("Hello World")
print("Hello World")


# \n
print("Hello world!\nHello world!\nHello world!")
print("Hello" + " " + "Angela")

# Read input from console And use str to concatenate strings
user_name = input("What is your name?")
pet_name = input("What is your pet name?")
print("Your brand name " + user_name + " "+ pet_name + "!")

print("Your name length is " + str(len(user_name)))

# Naming convention followed by _
my_name ="Angela"
length = len(my_name) # len can be used for string, list, tuple etc
print(length)
lower_name = my_name.lower() # string.upper(), strings are immutable in python
print(lower_name)

name = "Krishna" # start with 0 until len(Krishna)-1
print(name[0] + " "+ name[1])

# Make large number readable
mystery = 734_529.678
print(mystery) # print 734529.678
print(type(mystery)) # print type

# Type casting int, float, bool, str
number = "123"
print(int(number))
str_number = 123
print(str(str_number))

# Python do implicit type casting.
number = 5/3
print(number)  # type here is float
number2 = 5//3   # avoid implicit type casting (remove decimal places)
print(number2)  # type here is int
print(2**3)  # power

# Manipulating decimal places
bmi = (84/1.65) ** 2
print(bmi)
print(int(bmi))
print(round(bmi))
print(round(bmi, 2))

score = 0
score += 1
print(score)

# avoid using str in print
score = 0
height = 1.8
is_winning = True
print(f"Your score is: {score}, Your height is: {height}, Your winning score is: {is_winning}")

print("Welcome to the tip Calculator!")
total_bill = float(input("What was the total bill?"))
tip_amount = int(input("How much tip would you like to give? 10, 12, or 15?"))
num_people = int(input("How may people to split the bill?"))
split_amount = (total_bill+tip_amount)/num_people
rounded_split_amount = round(split_amount,2)
print(f"Each person should pay: ${rounded_split_amount}")




