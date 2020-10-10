import os

# Method -1
path = "D:/pycharm"
os.mkdir(path)

# Method -1 with exception handling
try:
    os.mkdir(path)
    print("folder created")
except FileExistsError:
    print("file already exists.")


# Method - 2

path = "D:/pycharm/NewFolder"
if not os.path.exists(path):
    os.makedirs(path)
else:
    print("folder already exists.")


# Path join

parent_dir = "D:\\pycharm"
new_dir = "TestFolder"
path = os.path.join(parent_dir, new_dir)
print(path)














