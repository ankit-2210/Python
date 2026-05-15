# Static Method in Python:
# We know that a static method in Python is treated differently than in other
# languages. Static methods in Python are extremely similar to python class
# methods, but the difference is that a static method is bound to a class
# rather than the objects for that class.
# To define a static method, we use @staticmethod decorator, which is a
# built-in decorator. Also, there is no need to import any module to use
# decorators. Using a static method in a class, we permit it to be accessed
# only by the class objects or inside the class.
#
# There are few limitations related to static methods, such as:
# 1. Unlike, class method a static method cannot alter or change any variable
# value or state of the class.
# 2. Static methods do not have any knowledge related to class.


# Static methods do not require any knowledge related to the class that they
# are built-in. They are only formed in a class so that only the class
# instances can access them. We can use a static method for simple
# functionality that is mostly not related to the class.
# For example, we want to add two numbers together, but we do not want
# our method to be used elsewhere, other than the class, or through its
# instances, so we will create a static method.
# It will not require any information related to class as it only requires
# the numbers it has to add, but it will still fulfill its purpose as it is
# like a personal method that only the class has access to.

# Most of the functionalities of the static methods can be performed using a
# class method. However, we prefer the static method, at places where it could
# work to make our program more efficient and faster as we do not have to pass
# self as a parameter, so the efficiency of the program increases.

# Static methods in Python are methods that belong to a class rather than an
# instance of the class. They are defined using the @staticmethod decorator
# and do not have access to the instance of the class (i.e. self). They are
# called on the class itself, not on an instance of the class. Static methods
# are often used to create utility functions that don't need access to
# instance data.


class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return (
            f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"
        )

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is good " + string)


harry = Employee("Harry", 255, "Instructor")
harry.printdetails()
rohan = Employee("Rohan", 455, "Student")
rohan.printdetails()
karan = Employee.from_dash("Karan-480-Student")

Employee.printgood("Rohan")


class Math:
    @staticmethod
    def add(a, b):
        return a + b


result = Math.add(1, 2)
print(result)  # Output: 3


# Static methods are used when a function:

# belongs logically to a class,
# but does not need object data (self)
# and does not need class data (cls).


# They help in organizing code better.
class Math:

    @staticmethod
    def add(a, b):
        return a + b


print(Math.add(5, 3))


class Student:

    @staticmethod
    def is_adult(age):
        return age >= 18


print(
    Student.is_adult(20)
)  # they immediately understand the function belongs to Student method.
