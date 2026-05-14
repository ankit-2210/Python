a = int(input("enter a\n"))
b = int(input("enter b\n"))

# if a>b: print("A B se bada hai bhai")
print("A B se bada hai bhai") if a > b else print("B A se bade hai bhai")
print("A") if a > b else print("=") if a == b else print("B")
