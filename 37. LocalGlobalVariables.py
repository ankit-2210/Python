# 1. Local Variable:-
# A variable that is declared inside a function or loop is called a local variable.
# In the case of functions, when we define a variable within a function, its scope lies within the function only. It is accessible from the point where it is defined until the end of the function. It will exist for as long as the function is executing. Local variables cannot be accessed outside the function. The parameter names in the function, they behave like a local variable.

# def sum():
#     a = 10  # local variable cannot be accessed outside the function
#     b = 20
#     sum = a + b
#     print(sum)

# print(a)  # this gives an error

# 2. Global Variable:-
# On the other hand, a global variable is easier to understand; it is not declared inside the function and can be accessed anywhere within a program. It can also be defined as a variable defined in the main body of the program. Any function or loop can access it. Its scope is anywhere within the program.

a = 1  # global variable

# def print_Number():
#
#             b=a+1;
#             print(b)

# print_Number()


l = 10  # Global


def function1(n):
    # l = 5 #Local
    m = 8  # Local
    global l
    l = l + 45
    print(l, m)
    print(n, "I have printed")


function1("This is me")
# print(m)


x = 89


def harry():
    x = 20

    def rohan():
        global x
        x = 88

    # print("before calling rohan()", x)
    rohan()
    print("after calling rohan()", x)


harry()
print(x)
