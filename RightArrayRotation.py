num = [1,2,3,4,5]
shift = 2
def rightArrayRotation(num_array, shift):
    for i in range(0, shift):
        temp = num_array[len(num_array)-1]
        for j in range(len(num_array)-1, 0, -1):
            num_array[j] = num_array[j-1]
        num_array[0]= temp
    return num_array

def printArray(array):
    for i in range(0, len(array)):
        print(array[i], end=' ')

print("Array Before Rotation: ")
printArray(num)
rotated_array = rightArrayRotation(num, shift)
print("\nArray after Right rotation: ")
printArray(rotated_array)



