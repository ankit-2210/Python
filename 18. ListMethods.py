# List Methods :
l1 = [1, 8, 4, 3, 15, 20, 25, 89, 65]  # l1 is a list
print(l1)
print(type(l1))

l1.sort()
print(l1)  # l1 after sorting
l1.reverse()
print(l1)  # l1 after reversing all elements
l1.sort(reverse=True)


list1 = [1, 2, 3, 6, 8, 5, 4]  # list1 is a list

list1.append(7)  # This will add 7 in the last of list
list1.insert(3, 8)  # This will add 8 at 3 index in list
list1.remove(1)  # This will remove 1 from the list
list1.pop(2)  # This will delete and return index 2 value.

print(list1)

m = [100, 200, 330]
list1.extend(m)
print(list1)

l = list1 + m
print(l)
