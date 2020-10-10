user_input = input("Enter any String :")

reverse_string = user_input[::-1]
if(user_input == reverse_string):
    print("Given String is Palindrome")
else:
    print("It is not Palindrome.")