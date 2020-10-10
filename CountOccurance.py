
list = [7,2,3,4,1,15,3]
Search = 3

def searchOccurance(list, number):
    count = 0
    for i in list:
        if(i == number):
            count+=1
    return count

result = searchOccurance(list, Search)
if(result > 0):
    print('Count is : ', result)
else:
    print('Element not fount in the list.')

print('using Inbuilt function : ', list.count(Search))






