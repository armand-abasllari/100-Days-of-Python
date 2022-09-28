# This is a tip calculator. It asks the user for the total bill, the tip percentage, and the number of
# people to split the bill. It then calculates the total tip amount, the total bill, the bill per
# person, and the final amount.
print ("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to gie? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
tip_as_percentage = tip / 100
total_tip_amount = bill * tip_as_percentage
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people 
final_amount = round(bill_per_person,2)
print(f"Each person should pay: $ {final_amount}")