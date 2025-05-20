file = open("text.txt")
contents = file.read()
print(contents)
file.close()

# r- read, w-write, a- append, r+ - read write
with open("text.txt", "r+") as file1:
    contents1 = file1.read()
    print(contents1)
    contents2 = contents1 + "\nNew Content"
#    file1.write(contents2)

import csv

with open("csv_file.csv", "r") as csv_file:
    csv_contents = csv.reader(csv_file) #csv.reader to read csv file in python
    for data in csv_contents:
        print(data)

# Challenge extract all the names
with open("csv_file.csv", "r") as csv_file1:
    names = []
    csv_contents = csv.reader(csv_file1) #csv.reader to read csv file in python
    for data in csv_contents:
        names.append(data[1])

    print(names)

# dictionary comprehension
student_marks = {
    "Krishna": 90,
    "Anuj": 50,
    "Mehul":60
}
grace = 10
final_score = {key:(score + grace) for key,score in student_marks.items()}
print(final_score)

print("END")