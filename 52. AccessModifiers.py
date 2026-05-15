# Access Specifiers/Modifiers

# Access specifiers or access modifiers in python programming are used to
# limit the access of class variables and class methods outside of class
# while implementing the concepts of inheritance.
# Types of access specifiers:
# 1. Public access modifier
# 2. Private access modifier
# 3. Protected access modifier


# 1. Public access modifier
# All the variables and methods (member functions) in python are by default
# public. Any instance variable in a class followed by the ‘self’ keyword
# ie. self.var_name are public accessed.
class Student:
    def __init__(self, age, name):
        self.age = age
        self.name = name


obj = Student(21, "Suman")
print(obj.age)
print(obj.name)


# 2. Private access modifier
# By definition, Private members of a class (variables or methods) are those
# members which are only accessible inside the class. We cannot use private
# members outside of class.

# In Python, there is no strict concept of "private" access modifiers like in
# some other programming languages. However, a convention has been established
# to indicate that a variable or method should be considered private by
# prefixing its name with a double underscore (__). This is known as a
# "weak internal use indicator" and it is a convention only, not a strict rule.


class Student1:
    def __init__(self, age, name):
        self.__age = age  # An indication of private variable

    def __funName(self):  # An indication of private function
        self.y = 34
        print(self.y)


class Subject(Student1):
    pass


obj1 = Student1(22, "Suman")
obj2 = Subject


print(obj1._Student1__age)  # Can be accessed directly --> Name mangling
print(obj1.__dir__())

# print(obj1.__age)    # Cannot be accessed directly
# print(obj1.__funName)

# print(obj2.__age)
# print(obj2.__funName)


# 3. Protected access modifier
# In object-oriented programming (OOP), the term "protected" is used to
# describe a member (i.e., a method or attribute) of a class that is intended
# to be accessed only by the class itself and its subclasses. In Python, the
# convention for indicating that a member is protected is to prefix its name
# with a single underscore (_). For example, if a class has a method called
# _my_method, it is indicating that the method should only be accessed by the
# class itself and its subclasses.


class Student2:
    def __init__(self):
        self._name = "Suman"

    def _funName(self):  # protected method
        return "SumanABC"


class Subject2(Student2):  # inherited class
    pass


obj3 = Student2()
obj4 = Subject2()

# calling by object of Student class
print(obj3._name)
print(obj3._funName())
# calling by object of Subject class
print(obj4._name)
print(obj4._funName())
