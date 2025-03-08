import random
result = random.random()
print(result)
result = random.randint(1, 50)
print(result)
result = random.choice(["red", "blue", "green", "black", "yellow"])
print(result)
fruits = ["apple", "banana", "plum", "orange"]
result = fruits
random.shuffle(fruits)
print(result)