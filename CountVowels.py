
# Method - 1 -> using For loop

sentence = input("Enter any string:")
sentence = sentence.lower()
vowel_count = 0
for i in sentence:
    if i == "a" or i == "e" or i == "i" or i == "o" or i =="u":
        vowel_count = vowel_count + 1
print("Total vowel count : ", vowel_count)

# Method - 2 -> using For loop & string function

vowels = "aeiou"
for i in sentence:
    if i in vowels:
        vowel_count = vowel_count + 1
print("Total vowel count : ", vowel_count)

# Method - 3 -> using ASCII method

for i in sentence:
   if ord(i) == 97 or ord(i) == 101 or ord(i) == 105 or ord(i) == 111 or ord(i) == 117:
       vowel_count = vowel_count + 1
print("Total vowel count : ", vowel_count)

# Method - 4 -> using List comphrehension

count = [ i for i in sentence if i in vowels ]
print("Total vowel count : ", len(count))

print("Total vowel count : ", len([ i for i in sentence if i in vowels ]))

