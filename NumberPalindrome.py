
number = int(input("Enter any number :"))

# Method - 1 --> using detailed logic

original = number
reverse = 0

while(number>0):
    digit = number % 10
    reverse = reverse * 10 + digit
    number = number // 10

if original == reverse:
    print('Number is palindrome.')
else:
    print('Number is not palindrome.')


# Method - 2 --> using string slice technique

number = str(number)
reverse = number[::-1]

if number == reverse:
    print('Number is palindrome.')
else:
    print('Number is not palindrome.')
