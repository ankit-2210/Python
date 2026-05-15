# Class Variables
# Class variables are defined at the class level and are shared among all
# instances of the class. They are defined outside of any method and are
# usually used to store information that is common to all instances of the
# class. For example, a class variable can be used to store the number of
# instances of a class that have been created.
class MyClass:
    class_variable = 0  # class variable

    def __init__(self):
        MyClass.class_variable += 1

    def print_class_variable(self):
        print(MyClass.class_variable)


obj1 = MyClass()
obj2 = MyClass()

obj1.print_class_variable()
obj2.print_class_variable()

# In the example above, the class_variable is shared among all instances of
# the class MyClass. When we create new instances of MyClass, the value of
# class_variable is incremented. When we call the print_class_variable method
# on obj1 and obj2, we get the same value of class_variable.

# Instance Variables
# Instance variables are defined at the instance level and are unique to each
# instance of the class. They are defined inside the init method and are
# usually used to store information that is specific to each instance of the
# class. For example, an instance variable can be used to store the name of an
# employee in a class that represents an employee.


class MyClass1:
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(self.name)


obj3 = MyClass1("John")
obj4 = MyClass1("Jane")

obj3.print_name()
obj4.print_name()

# In the example above, each instance of the class MyClass has its own value
# for the name variable. When we call the print_name method on obj1 and obj2,
# we get different values for name.

# In summary, class variables are shared among all instances of a class and
# are used to store information that is common to all instances. Instance
# variables are unique to each instance of a class and are used to store
# information that is specific to each instance.
