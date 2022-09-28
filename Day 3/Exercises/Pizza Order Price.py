print ("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S,M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese> Y or N ")

small_pizza = 15
medium_pizza = 20
large_pizza = 25
p_small = 2
p_large = 3
cheese = 1

if size == "S":
    if add_pepperoni == "Y" and extra_cheese == "Y":
        print  (f"Your final bill is: $ {small_pizza + p_small + cheese }")
    elif add_pepperoni == "Y" and extra_cheese == "N":
        print  (f"Your final bill is: $  {small_pizza + p_small }")
    elif add_pepperoni == "N" and extra_cheese == "Y":
        print  (f"Your final bill is: $  {small_pizza + cheese}")
    elif add_pepperoni == "N" and extra_cheese == "N":
        print  (f"Your final bill is: $  {small_pizza}")
elif size == "M":
    if add_pepperoni == "Y" and extra_cheese == "Y":
        print  (f"Your final bill is: $  {medium_pizza + p_large + cheese }")
    elif add_pepperoni == "Y" and extra_cheese == "N":
        print  (f"Your final bill is: $  {medium_pizza + p_large }")
    elif add_pepperoni == "N" and extra_cheese == "Y":
        print  (f"Your final bill is: $  {medium_pizza + cheese}")
    elif add_pepperoni == "N" and extra_cheese == "N":
        print  (f"Your final bill is: $  {medium_pizza}")
else:
    if add_pepperoni == "Y" and extra_cheese == "Y":
        print  (f"Your final bill is: $  {large_pizza + p_large + cheese }")
    elif add_pepperoni == "Y" and extra_cheese == "N":
        print  (f"Your final bill is: $  {large_pizza + p_large }")
    elif add_pepperoni == "N" and extra_cheese == "Y":
        print  (f"Your final bill is: $  {large_pizza + cheese}")
    elif add_pepperoni == "N" and extra_cheese == "N":
        print  (f"Your final bill is: $  {large_pizza}")
