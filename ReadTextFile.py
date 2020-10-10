# Method - 1

file = open("myfile.txt","r")
print(file.read(10))
print(file.read(5))
print(file.read())
file.close()

# Method - 2

with open("myfile.txt","r") as f:
    print(f.readline())
    print(f.readline())
    print(f.readline())

# Method - 3

with open("myfile.txt","r") as f:
    print(f.readlines())


with open("myfile.txt","r") as f:
    print(f.readlines(24))


# Method - 4

with open("myfile.txt","r") as f:
    for line in f:
        print(line)




