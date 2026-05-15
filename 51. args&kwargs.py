# *args:
# args is a short form used for arguments. It is used to unpack an argument.
# In the case of *args, the argument could be a list or tuple. Suppose that we
# have to enter the name of students who attended a particular lecture.
# Each day the number of students is different, so positional arguments would
# not be helpful because we can not leave an argument empty in that case.
# So the best way to deal with such programs is to define the function using
# the class name as formal positional argument and student names with
# parameter *args. In this way, we can pass student's names using a tuple.

# Note that the name args does not make any difference, we can use any other
# name, such as *myargs. The only thing that makes a difference is the Asterisk(*).


# **kwargs:
# The full form of **kwargs is keyword arguments. It passes the data to the
# argument in the form of a dictionary. Let's take the same example we used
# in the case of *args. The only difference now is that the student's
# registration, along with the student's name, has to be entered.
# So what **kwargs does is, it sends argument in the form of key and value
# pair. So the student's name and their registration both can be sent as a
# parameter using a single ** kwargs statement.


def function_name_print(a, b, c, d, e):
    print(a, b, c, d, e)


function_name_print("Harry", "Rohan", "SkillF", "Hammad", "Shivam")


def funargs(normal, *args, **kwargs):
    print(normal)
    for item in args:
        print(item)
    print("\nNow I would like to introduce some of our heroes: ")
    for key, value in kwargs.items():
        print(f"{key} is a {value}")


har = ["Harry", "Rohan", "SkillF", "Hammad", "Shivam", "The Programmer"]
normal = "I am a normal argument and the students are: "
kw = {
    "Rohan": "Monitor",
    "Harry": "Fitness Instructor",
    "SkillF": "Python",
    "Shivam": "The Cook",
}

funargs(normal, *har, **kw)


def greet(func):
    def mfx(*args, **kwargs):
        print("Good Morning")
        func(*args, **kwargs)
        print("Thank You")

    return mfx


@greet
def hello():
    print("Hello World")


@greet
def add(a, b):
    print(a + b)


hello()
# greet(add)(1, 2)
add(1, 2)
