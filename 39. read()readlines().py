f = open("myfile1.txt", "rt")
print(f.readlines())

while True:
    line = f.readline()
    if not line:
        break
    print(line)
# print(f.readline())
# print(f.readline())
# print(f.readline())
# content = f.read()
#
for line in f:
    print(line, end="")
# print(content)
# content = f.read(34455)
# print("1", content)
#
# content = f.read(34455)
# print("2", content)
f.close()


# f = open("Ankit.txt", "w")
# a = f.write("Ankit bhai bahut achhe hain\n")
# print(a)
# f.close()

# f = open("Ankit1.txt", "a")
# a = f.write("\nHarry bhai bahut achhe hain\n")
# print(a)
# f.close()


# Handle read and write both
f = open("myfile1.txt", "r+")
print(f.read())
f.write("\nThank you")


f = open("myfile2.txt", "r")
i = 0
while True:
    i = i + 1
    line = f.readline()
    if not line:
        break
    m1 = line.split(",")[0]
    m2 = line.split(",")[1]
    m3 = line.split(",")[2]

    print(f"Marks of student {i} in Maths is {m1}")
    print(f"Marks of student {i} in English is {m2}")
    print(f"Marks of student {i} in SST is {m3}")

f = open("myfile2.txt", "a")
lines = ["\nline 1", "\nline 2", "\nline 3"]
f.writelines(lines)
f.close()
