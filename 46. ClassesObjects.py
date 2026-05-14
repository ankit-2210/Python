# Python is a powerful programming language that supports the object-oriented
# programming paradigm. In object-oriented programming, the program splits
# into self-contained objects. Each object is representing a different part of
# the application which can communicate among themselves.
# We will be discussing classes and objects in more detail  in the next
# tutorial i.e, Creating Our First Class In Python. The primary focus of this
# tutorial is to give you the understanding of Object-Oriented
# Programming or in short form OOP. A programming technique that
# requires the use of objects and classes is known as OOP.
# Object-Oriented Programming is based on the principle of writing reusable
# code that can be accessed multiple times by the user


# What is Python Class And Object?
# Ans:- A class is a collection of objects, and an object is defined as an
# instance of class possessing attributes. The object is an entity that has
# state and behavior. A class has all the similar attributes, like if we have
# a class students, then it will only consist of students related data, such
# as subjects, names, attendance ratio, etc.

# Along with classes and objects, you will learn many new terminologies
# related to OOP in further tutorials. Some of these terminologies are:
# 1. Instances
# 2. Constructor
# 3. Methods
# 4. Abstraction
# 5. Inheritance
# By using oop, we can divide our code into many sections known as classes.
# Each class holds a distinct purpose or usage. For example, if we have
# created a class named "Books" then all the attributes it possesses should
# be related to books such as the number of pages, publishing date or price, etc.
# There is no limit to the number of classes we can create in a program.
# Also, one class can be easily accessible by another, and we can also
# restrict the access of a class so other classes can not use its functions.
# This concept comes in handy while working on bigger projects. All the
# employees are given separate tasks to work on the classes they have been assigned.
# And after they are done with their contribution, the classes can be combined
# as a whole to form a complete project. So, now you can understand that to
# become a successful programmer, you must master the concept of OOP.


# Classes - Template
# Object - Instance Of the Class

# DRY - Do not repeat Yourself

# get_no_of_films(table)


# Defining a Class in Python
# As in function, definitions begin with the keyword def, class begins with a class keyword.
#
# class MyClass:
#     '''This is a docstring.'''
#     pass

# A class is a blueprint from which objects are created.
# Creating a new class creates a new type of object which allows the
# new instances of that type to be made. Each class instance has attributes
# attached so that it could maintain its state.
# Class instances can also have methods that are defined by
# its class for modifying its state.

# Let us understand the concept of class through an example.
# Suppose we have to create a program that requires the data of all
# the individuals in a school. We will create three different classes,
# one for students, one for teaching staff,
# and one for accounting officers and others. The separation of the class
# is based on attributes because a teacher’s attributes are different from
# students, and both have different attributes from the members of account
# officers. Although many attributes are the same, such as name, age, address, etc.
# but the teacher also has an attribute salary that the student does not or an
# attribute, number of classes that the accounts officers do not possess.
# So, now we have an understanding of how and on what basis we form different classes

# Classes are not like function, so we do not have to use the keyword
# define to create a class; instead, we use the keyword Class along with the
# name of the class. Also, we do not call a class as a whole; instead,
# we use an object to access its different attributes.
# We can assign new values and can also overwrite the previous values
# with the help of an object. In short, an object gives us permission to access the whole class. We can access variables in a class, like:
# Object_name.variable_name = “abc”


# Creating Object:
#       Creating an object of a class is rather easy and simple.
#       Suppose we have a class named Student. We can create an object of it by these certain lines of code:
#
# Stu1 = Student()
# Stu2 = Student()
# Here we have created two objects of class Student.
# We can access every item in student using these objects.
# There is no restriction on the number of objects a class may have,
# and also there is no limit to the number of classes a program may have.
#
# An object consists of :
#  a. The State, which is represented by attributes of an object which reflects the properties of an object.
#  b. Methods of an object, which represents the behavior of the object and the response of an object with other objects.
#  c. Identity, which gives a unique name to an object, so that one object can interact with other objects.
#


class Student:
    pass


harry = Student()
larry = Student()

harry.name = "Harry"
harry.std = 12
harry.section = 1
larry.std = 9
larry.subjects = ["hindi", "physics"]
print(harry.section, larry.subjects)


# The self parameter is a reference to the current instance of the class,
# and is used to access variables that belong to the class.


class Person:
    name = "Ankit"
    phone = "123456"

    def info(self):
        print(f"{self.name} and {self.phone}")


a = Person()
print(a.name, a.phone)
a.info()

b = Person()
b.name = "Aman"
b.phone = "12345678"
b.info()
