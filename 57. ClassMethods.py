# What are Python Class Methods?
# A class method is a type of method that is bound to the class and not the
# instance of the class. In other words, it operates on the class as a whole,
# rather than on a specific instance of the class. Class methods are defined
# using the "@classmethod" decorator, followed by a function definition.
# The first argument of the function is always "cls," which represents the
# class itself.

# Why Use Python Class Methods?
# Class methods are useful in several situations. For example, you might want
# to create a factory method that creates instances of your class in a
# specific way. You could define a class method that creates the instance and
# returns it to the caller.


# How to Use Python Class Methods
# To define a class method, you simply use the "@classmethod" decorator before
# the method definition. The first argument of the method should always be
# "cls," which represents the class itself. Here is an example of how to
# define a class method:


class ExampleClass:
    @classmethod
    def factory_method(cls, argument1, argument2):
        return cls(argument1, argument2)


# In this example, the "factory_method" is a class method that takes two
# arguments, "argument1" and "argument2." It creates a new instance of the
# class "ExampleClass" using the "cls" keyword, and returns the new instance
# to the caller.


class Employee:
    company = "Apple"

    def show(self):
        print(f"The name is {self.name} and company is {self.company}")

    @classmethod
    def changeCompany(cls, newCompany):
        cls.company = newCompany


e1 = Employee()
e1.name = "Suman"
e1.show()
e1.changeCompany("Testa")
e1.show()
print(Employee.company)
