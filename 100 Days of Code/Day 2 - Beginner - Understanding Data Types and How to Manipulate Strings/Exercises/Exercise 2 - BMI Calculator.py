# Asking for the user's height and weight and then calculating the BMI.
height = input("What is your height?")
weight = input("What is your weight?")

bmi = (float(weight)) / float(height) ** 2
print (int(bmi))