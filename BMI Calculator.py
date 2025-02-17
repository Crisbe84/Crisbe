print("BMI Calculator\n\nWanna figure out your total BMI?\nThis is the calculator for you! Please answer the following questions for me to calculate your total Body Mass Index.\n")

height = float(input("What is your height in inches?\n"))
weight = float(input("Now the hard part, I won't look. What is your weight in pounds?\n"))

# Calculate BMI
bmi = (weight * 703) / (height ** 2)

# Display result
print(f"Your total BMI is: {round(bmi, 2)}")

# Determine BMI category
if bmi < 18.5:
    print("You are Underweight.")
elif 18.5 <= bmi <= 24.9:
    print("You have a Normal weight.")
else:
    print("You are Overweight.")
