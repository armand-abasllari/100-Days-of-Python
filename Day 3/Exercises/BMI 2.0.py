# Asking for the user's height and weight and then calculating the BMI.
height = float(input("Enter your height in m:?"))
weight = float(input("Enter your weight in kg?"))

bmi_rounded = weight / height ** 2
bmi= round(bmi_rounded)
if bmi < 18.5:
    print("Your BMI is 18, you are underweight.")
elif bmi > 18.5 and bmi < 25:
    print (f"Your BMI is {int(bmi)}, you have a normal weight.")
elif bmi > 25 and bmi < 30:
    print (f"Your BMI is {int(bmi)}, you are slightly overweight.")
elif bmi > 30 and bmi < 35:
    print (f"Your BMI is {int(bmi)}, you are obese.")
else:
    print (f"Your BMI is {int(bmi)}, you are clinically obese.")