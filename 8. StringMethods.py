# Strings are immutable

a = "!!Ankit !!"
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("!"))

print(a.replace("Ankit", "John"))
print(a.split(" "))

blog = "introduction to jS"
print(blog.capitalize())
print(blog.center(20))
print(len(blog.center(20)))
print(a.count("!"))

str = "Welcome to !!!"
print(str.endswith("!!!"))
print(str.find("to"))

str1 = "Welcome"
print(str1.isalpha())
