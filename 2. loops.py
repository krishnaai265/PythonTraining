# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

height = 100

if height <= 100:
    print("Your height is less than 100!")
elif height > 100 and height <= 200:
    print("Your height is greater than or equal to 100!")
else:
    print("Your height is greater than 100!")

# condition and, or , not true

list = ["alpha", "beta", "gamma"]
print(list[0])
print(list[-1])

list.append("delta") # add single element
print(list)

list.extend(["yes", "why"]) # extend multiple element
print(list)

list.remove("alpha") # remove element
print(list)

if len(list) >1:      # Empty list
    print("List is not empty")

num_list = [2,5,3,1]
list.sort() # Sort list elements
print(list)

# contains element
if "delta" in list:
    print("delta present in list!")

if "alpha" not in list:
    print("alpha not present in list")

# list inside list
list1 = ["alpha", "beta"]
list2 = ["gamma", "delta"]
list3 = [list1, list2]
print(list3)

for item in list:
    print(item, end=" ") # print in single line

print() # next line

score = [1, 2, 3]
total_score = sum(score)
print(total_score)
print(max(score))
print(min(score))

# default start value 0, upto 9
for i in range(10):
    print(i, end=" ")

print()

# give starting value, upto n-1
for i in range(5, 10):
    print(i, end=" ")

print()

# step size 3
for i in range(10, 19, 3):
    print(i, end=" ")

print()

# sum 1...100
sum = 0
for i in range(101):
    sum += i
print(sum)

def hello_function():
    print("Hello World!")

hello_function()

i =1
j = 5
while i<=j:
    print(i, end=" ")
    i += 1

print()

# In python we can store any datatype inside list and dictionaries

list = [123, "abc", "23"]
print(list)

prog_dic = {
    "for": "Value of for ",
    "while": "Value of while",
    "if": "Value of if statement",
    123: "Its number"
}

print(prog_dic["for"]) # that how we call dictionaries

prog_dic["for"] = "Update for value" # Update dictionary value
print(prog_dic["for"])

for key in prog_dic:  # Travers each key in dictionary
    print(key, prog_dic[key])

# Nesting in Dictionary
travel_dict = {
    "India": ["Kashmir", "Delhi", "Lucknow"],
    "China": ["shanghai"]
}

print(travel_dict["India"])
print(travel_dict["India"][0])

nested_list = [1, 2, [3, 4]]
print(nested_list[2])
print(nested_list[2][0])

# complex dictionaries
complex_dict = {
    "France": {
        "cities_visited": ["paris", "lille"],
        "total_visited": 12
    },
    "Germary": {
        "cities_visited":{}
    }
}
print(complex_dict["France"]["cities_visited"])


# List comprehension
numbers = [1,2,3,4,5]
new_list = []
for item in numbers:
    if item == 5:
        new_list.append(item*10)
print(new_list)

new_list1 = [item*100 for item in numbers if item == 5] # Don't need to use append, by default append it to new_list1
print(new_list1)

new_list2 = []
for item in numbers:
    new_list2.append(item*10)
print(new_list2)

new_list3 = [item+1 for item in numbers]
print(new_list3)

print("END")


































