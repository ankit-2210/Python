a = input("Enter a number: ")
print(f"Multiplication table of {a} os: ")

try:
    for i in range(1, 11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except Exception as e:
    print(e)


try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("Number is not an integer")
except IndexError:
    print("Index error")
