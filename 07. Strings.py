# Strings
# String is a data type in Python. Strings in Python programming language
# are arrays of bytes representing a sequence of characters. In simple terms,
# Strings are the combination or collection of characters enclosed in quotes.
#
# Primarily, you will find 3 types of strings in Python :
#
# Single Quote String – (‘Single Quote String’)
# Double Quote String – (“Double Quote String”)
# Triple Quote String – (‘’’ Triple Quote String ‘’’)


# String Functions:
demo = "Aakash is a good boy"
print(demo.endswith("boy"))
print(demo.count("o"))
print(demo.capitalize())
print(demo.upper())
print(demo.lower())
print(demo.find("is"))
# print(demo.find("good","nice"))
print("\n")

mystr = "Harry is a good boy"
print(len(mystr))
print(mystr[::-2])
print(mystr[:-1])

print(mystr.endswith("bdoy"))
print(mystr.count("o"))
print(mystr.capitalize())
print(mystr.replace("is", "are"))


nm = "Ankit"
print(nm[-4:-2])
