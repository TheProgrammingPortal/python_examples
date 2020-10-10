num = int(input("Enter any number :"))

# Method - 1 --> using loop

def cal_factorial(num):
    factorial = 1
    if num == 0 or num == 1:
        return 1
    for i in range(1, num+1):
        factorial = factorial * i
    return factorial

output = cal_factorial(num)
print('Factorial of number  ', num , ' is : ', output)


# Method - 2 --> using inbuilt function from math module

import math
output = math.factorial(num)
print('Factorial of number  ', num , ' is : ', output)

