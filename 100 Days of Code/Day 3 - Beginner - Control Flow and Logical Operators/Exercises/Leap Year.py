# The above code is checking whether the year is leap year or not.
year = int(input("Which year do you want to check?"))

if year % 4 == 0:
    if year % 100 == 0 and year % 400 == 0:
        print("Not leap year.")
    else:
        print("leap Year.")
else:
    print("Not leap year.")