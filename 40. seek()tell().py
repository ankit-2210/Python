# 1. tell()
# When we are working with python files, there are several ways to present the
# output of a program, it could be in human-readable form or binary form, or
# we use read() function with specified size to read some data.

f = open("myfile1.txt", "r")
print(type(f))
print(f.readline())
print(f.tell())

# Move to the 10th byte in the file
f.seek(5)

# Read the next 5 bytes
data = f.read(5)
print(data)

# 2. seek()
# When we open a file, the system points to the beginning of the file.
# Any read or write will happen from the start. To change the file object’s
# position, use seek(offset, whence) function. The position will compute by
# adding offset to a reference point, and the whence argument selects the
# reference point. It is useful when operating over an open file.
# If we want to read the file but skip the first 5 bytes, open the file,
# use function seek(5) to move to where you want to start reading,
# and then continue reading the file.

# f = open("Ankit1.txt", "r")
# f.seek(5)
# print( f.readline() )


# f = open("Ankit1.txt")
# f.seek(11)
# print(f.tell())
# print(f.readline())
# # print(f.tell())

# print(f.readline())
# # print(f.tell())
# f.close()


with open("sample.txt", "w") as f:
    f.write("Hello World!")
    f.truncate(5)

with open("sample.txt", "r") as f:
    print(f.read())
