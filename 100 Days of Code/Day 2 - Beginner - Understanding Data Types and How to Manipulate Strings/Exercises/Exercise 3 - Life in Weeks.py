# Asking the user for their age, then it is calculating how many days, weeks, and months they have
# left until they are 90 years old.
age = input("What is your current age?")
years_left = 90 - int(age)
days = years_left * 365
weeks = years_left * 52
months = years_left * 12
life_left = f"You have {days} days, {weeks} weeks, and {months} months left."
print(life_left)