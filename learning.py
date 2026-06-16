#Variable Switcheroo
glass1 = "water"
glass2 = "juice"

glass3 = glass1
glass1 = glass2
glass2 = glass3

print(glass1, glass2)

#Modulo
number = int(input("Choose a number: "))

if number % 2 == 0:
    print(f"{number} Even")
else:
    print(f"{number} Odd")

#import random
import random

random_number = random.randint(0,1)

print(random_number)

if random_number == 1:
    print("heads")
else:
    print("tails")

#random.choice()
import random

friends = ["Alice", "Bob","Charlie", "David", "Emanuel"]

select_friend = random.choice(friends)
print(select_friend) 