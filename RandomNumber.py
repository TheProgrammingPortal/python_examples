
# Method 1- using random method

import random
num = random.random()
print(num)

# Method 2- using randint method

num = random.randint(10, 20)
print(num)

# Method 3- using randrange method

num = random.randrange(100,200,2)
print(num)

# Method 4- using uniform method

num = random.uniform(50,70)
print(num)

# Method 5- using sample method

numList = random.sample(range(150,250), 15)
print(numList)

# Method 6- using shuffle and choice method

numList = [1,2,3,4,5]
random.shuffle(numList)
print(numList)
print(random.choice(numList))
