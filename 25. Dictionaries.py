# “Python dictionary is an unordered collection of items.
# Each item of the dictionary has a key and value pair/ key-value pair.”


a = {"key": "value", "cow": "mooh"}
print(a["cow"])
# will print "mooh" on the screen


# Dictionary is nothing but key value pairs
d1 = {}
# print(type(d1))
d2 = {
    "Harry": "Burger",
    "Rohan": "Fish",
    "SkillF": "Roti",
    "Shubham": {"B": "maggie", "L": "roti", "D": "Chicken"},
}
d2["Ankit"] = "Junk Food"
d2[420] = "Kebabs"
print(d2)
del d2[420]
print(d2["Shubham"])
d3 = d2.copy()
del d3["Harry"]
d2.update({"Leena": "Toffee"})
print(d2.keys())
print(d2.items())

dictionary = {
    "happy": "The state of being in a good mood",
    "melancholy": "The state of being sad",
    "python": "The language in which this code is written",
    "computer": "The best things",
}

print("The words you can search are: ")

for items in dictionary:
    print(items + ": " + dictionary[items])

for key, value in dictionary.items():
    print(f"{key}: {value}")

print("Search any of those words\n")
searched = input()

for key in dictionary:
    if searched == key:
        print(dictionary[key])


# 2-Solution
# Create a dictionary and take input from the user and return the meaning of the
# word from the dictionary

Dict = {
    "ignore": "refuse to take notice of or acknowledge",
    "abandon": "cease to support or look after",
    "exaggerate": "enlarged or altered beyond normal proportions",
    "prejudice": "preconceived opinion that is not based on reason or actual experience",
}
print("Enter the Word")
Data1 = input()
print(Data1, "means", Dict[Data1])
