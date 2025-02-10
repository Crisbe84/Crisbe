print("BMI Calculator\n\nWanna figure out your total BMI?\nThis is the calculator for you! Please answer the following questions for me to calculate your total Body Mass Index.\n")

height = float(input("What is your height in inches?\n"))
weight = float(input("Now the hard part, I won't look. What is your weight in pounds?\n"))

# Write your code here.
# Calculate the bmi using weight and height.
bmi = (weight*703)/height/height

print("Your total BMI is: ",round(bmi, 2))
