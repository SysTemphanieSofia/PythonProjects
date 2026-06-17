import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'q', 'x', 'y' ,'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['!', '#', '$', '%', '&', '(',')','*','+']

print("Welcome to the PyPassword Generator!")

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = []
for pass_letter in range(0,nr_letters):
    choose_letter = random.choice(letters)
    password.append(choose_letter)

for pass_number in range(0,nr_numbers):
    choose_number = random.choice(numbers)
    password.append(choose_number)

for pass_symbols in range(0,nr_symbols):
    choose_symbols = random.choice(symbols)
    password.append(choose_symbols)

combine = "".join(password)
print(f"Your password is: {combine}")