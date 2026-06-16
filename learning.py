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