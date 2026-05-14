# Sets In Python
# Let's start with the basic definition of sets in Mathematics.
# People already familiar with the concept of sets in mathematics know that as per the mathematical definition
# - A set is a collection of well-defined objects and non-repetitive elements that is - a set with 1,2,3,4,3,4,5,2, 2,
# and 3 as its elements can be written as {1,2,3,4,5}
#
# No repetition of elements is allowed in sets.
#
# In Python programming, sets are more or less the same. Let's look at the Python programming definition of sets:
#
# “A set is a data structure, having unordered, unique, and unindexed elements.”


# Set Methods:
# There are already a lot of built-in methods that you can use for your ease and they are easily accessible through the internet.
# You might want to peep into python's official documentation at times as well to check for some updates they might push down the line.
# Some of the methods you can use with sets include union(), discard(), add(), isdisjoint(), etc. and their functionality is the same as in the sets in mathematics.


s = set()
print(type(s))
l = [1, 2, 3, 4]
s_from_list = set(l)
print(s_from_list)
print(type(s_from_list))
s.add(1)
s.add(2)
s.remove(2)
s1 = {4, 6}
print(s.isdisjoint(s1))

s1 = {6, 7, 8}
s1_from_list = set(s1)

s2 = {1, 2, 3, 7}
s2_from_list = set(s2)

print(s1_from_list.union(s2_from_list))
print(s1_from_list.intersection(s2_from_list))
s1_from_list.clear()
print(s1_from_list)
