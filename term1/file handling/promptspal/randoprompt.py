import random
with open('promptspal.txt', 'r') as prompts:
    for line in prompts:
        separator = "-Let's GO!"
        meow = line.split(separator)
        print(random.choice(meow))
        #print(meow)
