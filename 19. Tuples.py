# Tuples in Python:
# A tuple is an immutable data type in Python. A tuple in python is a collection of elements enclosed in () (parentheses).
# Tuple once defined can’t be changed i.e. its elements or values can’t be altered or manipulated.

# Tuples in Python :
a = ()  # It's an example of empty tuple
x = (1,)  # Tuple with single value i.e. 1
tup1 = (1, 2, 3, 4, 5)
tup1 = ("harry", 5, "demo", 5.8)
print(type(a))

for it in tup1:
    print(it)

# Swapping of two numbers :
a = 10
b = 15
print(a, b)  # It will give output as: 10 15
a, b = b, a
print(a, b)  # It will give output as: 15 10

# Tuple Operation
countries = ("Spain", "India", "England")
temp = list(countries)
temp.append("Russia")
temp.pop(2)
countries = tuple(temp)
print(countries)


# Practice
grocery = ["Harpic", "vim bar", "deodrant", "Bhindi", "Lollypop", 56]
# print(grocery[5])
numbers = [2, 7, 9, 11, 3]
numbers.remove(9)
# numbers.pop()
# numbers.sort()
# numbers = []
# numbers.reverse()
# numbers.append(1)
# numbers.append(72)
# numbers.append(5)
# numbers.insert(2, 67)
# print(numbers)
# 3, 11, 9, 7, 2
# print(numbers)
# numbers[1] = 98
# print(numbers)
# Mutable - can change
# Immutable - cannot change
# tp = (1,)
# print(tp)
a = 1
b = 8
a, b = b, a
# temp = a
# a = b
# b = temp
print(a, b)
