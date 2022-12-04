# 1
import random

comp = random.randrange(1, 20)

while True:
    guess = int(input("guess numb:"))
    print(comp)
    if comp == guess:
        break

print(int(1 or 2))


# 2
while True:
    year = int(input("Vilket år vill du testa? "))
    if year % 4 == 0:
        print("its a leap year")
    else:
        print("it aint")
