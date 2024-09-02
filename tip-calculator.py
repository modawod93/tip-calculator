print ("Welcome to the tip calculator!")

subtotal = float(input("What is the total bill? EGP "))
tip = int(input ("How much tip would you like to give? 10%, 12%, or 15%? "))
tip /= 100
total = int(subtotal + tip)
people = int(input("How many people to split the bill? "))
split = round ((total / people), 2)

splitted = (f"Each person should pay: EGP {split}")

print(splitted)
print ("Have a nice day!")