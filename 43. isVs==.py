# The is operator compares the identify of two objects
# while the == operator compares the values of the objects.

a = "hello"
b = "hello"

print(a == b)
print(a is b)

a = 5
b = "5"
print(a == b)  # value
print(a is b)  # exact location of object in memory

a1 = [1, 2, 43]
b1 = [1, 2, 43]
print(a1 is b1)
print(a1 == b1)
