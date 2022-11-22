import random
with open('promptspal.txt', 'r') as prompts:
    for line in prompts:
        meow = line.split()
        print(random.choice(meow))
