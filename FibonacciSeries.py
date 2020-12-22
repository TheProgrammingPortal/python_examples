# python program to print the Fibonacci series upto n terms

num = int(input("Enter any number :"))
n1, n2 = 0, 1
sum = 0
if num <= 0:
    print('Please enter number greater than 0')
else:
    for i in range(0, num):
        print(sum, end=" ")
        n1 = n2
        n2 = sum
        sum = n1 + n2

print('completed..')

