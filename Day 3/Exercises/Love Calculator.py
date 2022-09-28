print("Welcome to the Love Calulator!")
name1 = input("What is your name> \n")
name2 = input("What is their name> \n")
name3 = str(name1) + str(name2)
name3_lower = name3.lower()

total_true = name3_lower.count("t") + name3_lower.count("r") + name3_lower.count("u") + name3_lower.count("e")
total_love = name3_lower.count("l") + name3_lower.count("o") + name3_lower.count("v") + name3_lower.count("e")

total_score = str(total_true) + str(total_love)

if int(total_score) < 10 or int(total_score) > 90:
    print(f"Your score is {total_score}, you go together like coke and mentos.")
elif int(total_score) < 50 and int(total_score) > 40:
    print(f"Your score is {total_score}, you are alright together.")
else:
    print(f"Your score is {total_score}")