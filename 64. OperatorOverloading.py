# Operator Overloading
# Operator Overloading is a feature in Python that allows developers to
# redefine the behavior of mathematical and comparison operators for custom
# data types.

# Why do we need operator overloading?
# Operator overloading allows you to create more readable and intuitive code.
# For instance, consider a custom class that represents a point in 2D space.
# You could define a method called 'add' to add two points together, but using
# the + operator makes the code more concise and readable:

# You can overload an operator in Python by defining special methods in
# your class.

# + : __add__
# - : __sub__
# * : __mul__
# / : __truediv__
# < : __lt__
# > : __gt__
# == : __eq__


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2
print(p3.x, p3.y)
