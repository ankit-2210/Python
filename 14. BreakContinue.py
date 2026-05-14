while True:
    inp = int(input("Enter a Number\n"))
    if inp > 100:
        print("Congrats you have entered a number greater than 100\n")
        break
    else:
        print("Try again!\n")
        continue


for i in range(1, 12):
    if i == 10:
        print("Skip")
        continue
    print("5 X", i, "=", 5 * i)
