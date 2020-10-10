sentence = "my name is roshan"
substring = "john"

def SearchString(substring):
    result = sentence.find(substring) #start index, last index
    if(result == -1):
        print("Given substring not found.")
    else:
        print("substring found at index : ", result)

SearchString(substring)



