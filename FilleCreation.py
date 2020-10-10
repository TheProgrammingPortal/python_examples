
# method - 1
file = open("myfile.txt","w")
file.write("data inside file.")
file.close()

# method - 2
with open("myfile.txt","w") as file:
    file.write("data inside file.")

# method - 3
try:
    file=open("myfile.txt","r")
except IOError:
    print("Error : Filename or file path is incorrect.")
finally:
    print("exiting...")


