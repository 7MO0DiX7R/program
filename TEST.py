import random

comp = random.randrange(1, 20)

while True:
    guess = int(input("guess numb:"))
    print(comp)
    if comp == guess:
        break

print(int(1 or 2))
