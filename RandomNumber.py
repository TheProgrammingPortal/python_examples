
import random
num = random.random()
print(num)

num = random.randint(10, 20)
print(num)

num = random.randrange(100,200,2)
print(num)

num = random.uniform(50,70)
print(num)

numList = random.sample(range(150,250), 15)
print(numList)

numList = [1,2,3,4,5]
random.shuffle(numList)
print(numList)
print(random.choice(numList))
