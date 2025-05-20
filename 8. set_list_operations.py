# Let's have all available operation in python

# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1 | set2)  # Output: {1, 2, 3, 4, 5}
print(set1.union(set2))  # Same result

print(set1 & set2)  # Output: {3}
print(set1.intersection(set2))  # Same result

print(set1 - set2)  # Output: {1, 2} (Elements in set1 but not in set2)
print(set1.difference(set2))  # Same result

print(set1 ^ set2)  # Output: {1, 2, 4, 5}
print(set1.symmetric_difference(set2))  # Same result

print(2 in set1)  # Output: True
print(6 not in set1)  # Output: True

set1.add(6)  # Adds 6
set1.remove(3)  # Removes 3
set1.discard(10)  # No error if 10 isn’t in the set
print(set1)

set1.clear()  # Empties the set
print(set1)  # Output: set()

small_set = {1, 2}
big_set = {1, 2, 3, 4}

print(small_set <= big_set)  # Output: True (small_set is subset)
print(big_set >= small_set)  # Output: True (big_set is superset)

frozen = frozenset([1, 2, 3])
# frozen.add(4)  # Error! Cannot modify frozenset.
print(frozen)  # Output: frozenset({1, 2, 3})


print("----------------LIST----------------")
# PLEASE NOTE + OPERATOR not in set
# + OPERATOR PRESENT IN LIST

list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = list1 + list2  # Output: [1, 2, 3, 4, 5, 6]

list1 = [1, 2]
result = list1 * 3  # Output: [1, 2, 1, 2, 1, 2]

numbers = [1, 2, 3, 4, 5]
print(3 in numbers)  # Output: True
print(6 not in numbers)  # Output: True


numbers = [1, 2, 3]
numbers.append(4)  # Output: [1, 2, 3, 4]

numbers.extend([5, 6, 7])  # Output: [1, 2, 3, 4, 5, 6, 7]

numbers.insert(1, 100)  # Output: [1, 100, 2, 3, 4, 5, 6, 7]

numbers.remove(3)  # Output: [1, 100, 2, 4, 5, 6, 7]
popped_value = numbers.pop(1)  # Removes element at index 1
print(numbers)  # Output: [1, 2, 4, 5, 6, 7]
del numbers[0]  # Deletes first element
print(numbers)  # Output: [2, 4, 5, 6, 7]

numbers = [3, 1, 4, 2]
print(sorted(numbers))  # Output: [1, 2, 3, 4] (Returns a new list)
numbers.sort()
print(numbers)  # Output: [1, 2, 3, 4] (Modifies in-place)

numbers.reverse()  # Output: [4, 3, 2, 1]

squared = [x**2 for x in range(5)]
print(squared)  # Output: [0, 1, 4, 9, 16]

print("--------------------DICTIONARIES-------------")
data = {"Alice": 25, "Bob": 30, "Charlie": 35}
print(data["Alice"])  # Output: 25
print(data.get("David", "Not Found"))  # Output: Not Found
data["David"] = 40  # Adds a new key-value pair
data["Alice"] = 26  # Updates an existing value
del data["Bob"]  # Removes 'Bob' from the dictionary
data.pop("Charlie")  # Removes 'Charlie' and returns its value (35)

for key in data:
    print(key)  # Outputs each key

for value in data.values():
    print(value)  # Outputs each value

for key, value in data.items():
    print(key, value)  # Outputs each key-value pair

print(list(data.keys()))  # Output: ['Alice', 'David']

print(list(data.values()))  # Output: [26, 40]

print(list(data.items()))  # Output: [('Alice', 26), ('David', 40)]

data.update({"Eve": 28, "Frank": 33})  # Adds new entries

sorted_dict = dict(sorted(data.items())) # Sort by Key

sorted_dict = dict(sorted(data.items(), key=lambda x: x[1])) # Sort by Value

print("Alice" in data)  # Output: True

print(26 in data.values())  # Output: True








