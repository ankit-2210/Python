# Create a program capable of displaying questions to user like KBC.

# Use List data type to store the questions and their correct answers.
# Display the final amount the person is taking home after playing the game.


list = [
    "What is the capital of India?",
    "Choose an option: ",
    "a. delhi",
    "b. kolkata",
    "c. mumbai",
    "d. jaipur",
]
correct = "a"
for i in list:
    print(i)

print("You have 3 chances!!")
i = 0
flag = False
while i < 3:
    a = input("Enter your options: ")
    if a == correct:
        print("You won the game")
        flag = True
        break
    else:
        print(3 - i - 1, "chances more")
    i += 1

if flag == False:
    print("You lose the game")
