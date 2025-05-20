# def function_name(arguments):
#     return expression

# lambda arguments: expression

# calculate square of numbers
x = 5
square = lambda x: x * x
print(square(x))

# Add 2 numbers, use : instead of =
sum = lambda x,y: x + y
print(sum(2,3))

# list(tuples) sorting based on key
students = [("aaa", 20), ("ccc", 17), ("bbb", 19)]
sorted_students = sorted(students)
print(sorted_students)

# sort list(tuples) based on second element
students = [("aaa", 20), ("ccc", 17), ("bbb", 19)]
sorted_students = sorted(students, key=lambda x:x[1])
print(sorted_students)

# sort list(tuples) based on second and third element only
students = [('John', '20', '90'), ('Jony', '17', '93'), ('Jony', '17', '91'), ('Json', '21', '85'), ('Tom', '19', '80')]
sorted_students = sorted(students, key=lambda x:(int(x[1]), int(x[2])))
print(sorted_students)

# sort list(tuples) based on first, second and third element only
students = [('John', '20', '90'), ('Jony', '17', '93'), ('Jony', '17', '91'), ('Json', '21', '85'), ('Tom', '19', '80')]
sorted_students = sorted(students, key=lambda x:(x[0], int(x[1]), int(x[2])))
print(sorted_students)

# filter and map with lambda
#sorted(values, keys=lambda)
# filter(lambda, values)
# map(lambda, values)

print("----map---")
numbers = [1,2,3,4]
square = list(map(lambda x: x*x, numbers))
print(square)

print("----filter---")
numbers = [1,2,3,4]
square = list(filter(lambda x: x%2==0, numbers))
print(square)

print("----map conversion---")
# map - iterate each element of list to convert datatype
number = ['1','2','3','4']
square = list(map(int, number))
print(square)

print("----map mathematical operations---")
# map - mathematical operations lambda is mandatory
numbers = [1,2,3,4]
square = list(map(lambda x: x*x, numbers))
print(square)







