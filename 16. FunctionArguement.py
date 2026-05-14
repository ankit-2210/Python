def average(*numbers):  # tuples
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum += i
    print("Average is: ", sum / len(numbers))


average(4, 6, 1, 2)


def name(**name):  # dictionary
    print(type(name))
    print("Hello: ", name["fname"], name["mname"], name["lname"])


name(fname="James", mname="Buchan", lname="Barnes")
