try:
    age = int(input("How old are you?"))
except ValueError:
    print("Please rerun and enter a number, text not allowed")
    exit(0)

if age > 18:
    print(f"You can drive at age {age}.")

try:    # code that may throw exception
    file = open("file.txt")
    file.close()
except FileNotFoundError: # if exception
    print("File not found")
else:   # if no exception
    print("No Exception")
finally: #Do this in both the case
    print("connection closed")

try:
    raise ValueError("ValueError")
except ValueError:
    print("ValueError")


