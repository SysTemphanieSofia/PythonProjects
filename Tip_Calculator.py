print("Welcome to the tip calculator!")
ask_bill = float(input("What was the total bill? "))
ask_tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

percentage = (ask_tip/100) + 1
computation = (ask_bill * percentage)/5
round_off = round(computation, 2)

print(f"Each person should pay: ${round_off}")