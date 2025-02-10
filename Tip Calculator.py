# Tip Calculator - define Inputs, get total bill, and split amount among part to share total each person would owe
print("Welcome to the tip calculator!\nHere you can calculate how much money each person would owe to chip in for the total bill.\n")

# Inputs
bill = float(input("What was the total bill?\n$"))
tip = int(input('What percentage tip would you like to give? 10 12 15 20\n'))
people = int(input("How many people to split the bill?\n"))

# Total Bill
total_bill = (bill * tip/100 + bill)

# Split up the bill with the squad
amount_per_person = round(total_bill / people, 2)

# Grand total per person
print(f"Each person should pay: ${amount_per_person}")

