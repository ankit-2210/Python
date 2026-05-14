# 1. map():
# "A map function executes certain instructions or
# functionality provided to it on every item of an iterable."

# The iterable could be a list, tuple, set, etc.
# It is worth nothing that the output in the case of the map
# is also an iterable i.e., a list. It is a built-in function,
# so no import statement required.

# SYNTAX:
# map(function, iterable)
# A map function takes two parameters:
# a. First one is the function through which we want to
# pass the items/values of the iterable
# b. The second one is the iterable itself

items = [1, 2, 3, 4, 5]
a = list(map((lambda x: x**3), items))
print(a)


# 2. filter():-
# "A filter function in Python tests a specific user-defined condition
# for a function and returns an iterable for the elements and values
# that satisfy the condition or, in other words, return true."

# It is also a built-in function, so no need for an import statement.
# All the actions we perform using the filter can also be performed by using
# a for loop for iteration and if-else statements to check the conditions.
# We can also use a Boolean that could take note of true or false,
# but that would make the process very lengthy and complex.
# So, to simplify the code, we can use the filter function.
#
# SYNTAX:
# filter(function, iterable)
# It also takes two parameters:
# a. First one is the function for which the condition should satisfy
# b. The second one is the iterable

a = [1, 2, 3, 4, 5, 6]
b = [2, 5, 0, 7, 3]
c = list(filter(lambda x: x in a, b))
print(c)


# 3. reduce():
# "Reduce functions apply a function to every item of an iterable and
# gives back a single value as a resultant".

# Unlike the previous two functions (Filter and Map), we have to import the
# reduce function from functools module using the statement:
# from functools import reduce
# We can also import the whole functools module by simply writing

# Import functools
# But in the case of bigger projects, it is not good practice to import
# a whole module because of time restraint.

# SYNTAX:
# reduce(function, iterable)


from functools import reduce

list1 = [1, 2, 3, 4]
a = reduce((lambda x, y: x * y), list1)
print(a)


# ------------------------MAP--------------------------
numbers = ["3", "34", "64"]
numbers = list(map(int, numbers))

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

numbers[2] = numbers[2] + 1
print(numbers[2])


def sq(a):
    return a * a


num = [2, 3, 5, 6, 76, 3, 3, 2]
square = list(map(sq, num))
print(square)

num = [2, 3, 5, 6, 76, 3, 3, 2]
square = list(map(lambda x: x * x, num))
print(square)


# def square(a):
#     return a*a
#
# def cube(a):
#     return a*a*a
#
#
# func = [square, cube]
# num = [2,3,5,6,76,3,3,2]
# for i in range(5):
#     val = list(map(lambda x: x[i], func))
#     print(val)

# -------------------FILTER----------------------

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def is_greater_5(num):
    return num > 5


gr_then_5 = list(filter(is_greater_5, list_1))
print(gr_then_5)

gr_then_5 = list(filter(lambda x: x > 5, list_1))
print(gr_then_5)


# ------------------------REDUCE-----------------------
# from functools import reduce

list1 = [1, 2, 3, 4, 2]
num = reduce(lambda x, y: x * y, list1)
# num = 0
# for i in list1:
#     num = num + i
print(num)
