for i in range(6):
    print(i)
    if i == 4:
        break
else:
    print("no i")


for x in range(5):
    print("Iteration no {} in for loop".format(x + 1))
else:
    print("Else block in loop")
print("Out of loop")
