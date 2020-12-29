file_to_read ="ReadData.txt"
write_to_file="WriteData.txt"

# Reading a file
file = open(file_to_read,"r")
data = file.read()
file.close()

# Writing to a file
with open(write_to_file,"a") as file:   # with method auto closes the file object
    file.write(data)
print('completed')


