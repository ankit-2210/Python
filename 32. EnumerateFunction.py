# An enumerate is a built-in function that provides an index to data structure elements,
# making iterations through them easier and simpler.


# What enumerate function does is, it assigns an index to every element or value in the object that we want to iterate,
# so we do not have to assign a specific variable for
# incremental function, instead we have to apply a for loop, and our function will start working.


# Syntax
# --> enumerate(iterable, start=0)
# When calling a simple enumeration function, we have to provide two parameters:
# a. The data structure that we want to iterate
# b. The index from where we want to start our iteration


list_1 = ["code", "with", "harry"]
for index, val in enumerate(list_1):
    print(index, val)


# Using Enumerate() on a list with start Index:
# In the below example, the starting index is given as 5. The index of the first item will start from the given starting index.

list_2 = ["Python", "Programming", "Is", "Fun"]
# Counter value starts from 5
result = enumerate(list_2, 5)
print(list(result))

# If we do not provide the index, we want to start the iteration from then it automatically starts its iteration from zero index i.e., the beginning of the data structure.
# Instead of returning a string, the enumerate function returns an object by adding the iterating counter value. We can also convert the enumerator object into a list(), tuple(), set(), and many more.


# Advantages of using Enumerate:
# 1. It is a built-in function
# 2. It makes the code shorter
# 3. We do not have to keep count of the number of iterations
# 4. It makes the implementation of for loop simpler and cleaner
# 5. Lesser code so lessor chances of error and bugs
# 6. We can loop through string, tuple or objects using enumerate
# 7. We can start the iteration from anywhere within the data structure as we have the option of providing the starting index for iteration.


l1 = ["Bhindi", "Aloo", "Chopstricks", "Chowmein"]

# i = 1
# for item in l1:
#     if i%2 is not 0:
#         print(f"Jarvis please buy {item}")
#     i += 1

for index, item in enumerate(l1):
    if index % 2 == 0:
        print(f"{index} Jarvis please buy {item}")
