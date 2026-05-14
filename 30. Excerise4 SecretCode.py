# Write a python program to translate a message into secret code language. Use the rules below
# to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
# now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

import random
import string


def random_chars():
    return "".join(random.choices(string.ascii_letters, k=3))


def encode(word):
    if len(word) >= 3:
        first = word[0]
        word = word[1:] + first
        secret = random_chars() + word + random_chars()
        return secret
    else:
        return word[::-1]


def decode(word):
    if len(word) < 3:
        return word[::-1]
    else:
        word = word[3:-3]
        decoded = word[-1] + word[-1]
        return decoded


choice = input("Enter 'c' for coding or 'd' for decoding: ")
message = input("Enter your message: ")

words = message.split()
res = []
if choice == "c":
    for word in words:
        res.append(encode(word))
    print("Encoded message:", "".join(res))

elif choice == "d":
    for word in words:
        res.append(decode(word))
    print("Decoded message:", "".join(res))

else:
    print("Invalid choice!")
