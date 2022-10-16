# Asking the user to input a list of names separated by a comma. It then splits the string into a list
# of names. It then randomly selects a name from the list and prints it.
import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
names2 = len(names)
s = random.randint (0,names2 -1)
print(f"{names[s]} is going to buy the meal today!")

