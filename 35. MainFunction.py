# What is __name__?
# “A __name__ is a built-in variable that returns us the name of the module being used.


print("__name__ in MainFunctions.py is set to" + __name__)


# What are the Advantages of using if __name__ == “__main__” statement?
# Following are the advantages of using if __name__ == “__main__” statement:

# 1. Using the main in our file, we can restrict some data from exporting to other files when imported.
# 2. We can restrict the unnecessary data, thus making the output cleaner and more readable.
# 3. We can choose what others may import or what they may not while using our module.
#  To summarise the concepts discussed in this tutorial, Modules in Python has a special attribute called __name__. The value of the __name__ attribute is
#  set to __main__ when the module is run as the main program. Otherwise, the value of __name__ is set to the name of the module.
# The if __name__ == “__main__” block prevents the certain code from being run when the module is imported.


import ImportWorks


def printhar(string):
    return f"Ye string harry ko de de thakur {string}"


def add(num1, num2):
    return num1 + num2 + 5


print("aand the name is", __name__)

if __name__ == "__main__":
    print(printhar("Harry1"))
    o = add(4, 6)
    print(o)
    ImportWorks.welcome()
