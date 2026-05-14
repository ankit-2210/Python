# Lists :
# Python lists are containers used to store a list of values of any data type. In simple words, we can say that a list is a collection of elements from any data type E.g.

list1 = ["harry", "ram", "Aakash", "shyam", 5, 4.85]
for i in list1:
    print(i)


# Lists in Python
#
# []                          # list with no member, empty list
# [1, 2, 3]                   # list of integers
# [1, 2.5, 3.7, 9]            # list of numbers (integers and floating point)
# ['a', 'b', 'c']             # lisst of characters
# ['a', 1, 'b', 3.5, 'zero']  # list of mixed value types
# ['One', 'Two', 'Three']     # list of strings

names = [i * i for i in range(4) if (i % 2 == 0)]
print(names)
