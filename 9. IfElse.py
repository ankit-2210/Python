# var1 = 6
# var2 = 56
# var3 = int(input())
# if var3>var2:
#     print("Greater")
# elif var3==var2:
#     print("Equal")
# else:
#     print("Lesser")

# list1 = [5, 7, 3]
# print(15 not in list1)
# if 15 not in list1:
#     print("No its not in the list")

# Quiz
print("What is your age?")
age = int(input())

print(age > 12)
print(age == 18)
print(age != 19)

if age < 18:
    print("You cannot drive")
elif age == 18:
    print("We will think about you")
else:
    print("You can drive")


# no of guesses 9
# print no of guesses left
# No of guesses he took to finish
# game over

n = 18
number_of_guesses = 1
print("Number of guesses is limited to only 9 times: ")
while number_of_guesses <= 9:
    guess_number = int(input("Guess the number :\n"))
    if guess_number < 18:
        print("you enter less number please input greater number.\n")
    elif guess_number > 18:
        print("you enter greater number please input smaller number.\n ")
    else:
        print("you won\n")
        print(number_of_guesses, "no.of guesses he took to finish.")
        break
    print(9 - number_of_guesses, "no. of guesses left")
    number_of_guesses = number_of_guesses + 1

if number_of_guesses > 9:
    print("Game Over")


a = int(input("enter a\n"))
b = int(input("enter b\n"))

# if a>b: print("A B se bada hai bhai")
print("B A se bada hai bhai") if a > b else print("A B se bade hai bhai")
