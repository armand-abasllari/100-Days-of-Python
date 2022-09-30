# This is a for loop that iterates through the range of 1 to 101. The if statement checks if the
# number is divisible by 3 and 5. If it is, it prints FizzBuzz. If it is not, it checks if the number
# is divisible by 5. If it is, it prints Buzz. If it is not, it checks if the number is divisible by
# 3. If it is, it prints Fizz. If it is not, it prints the number.
for i in range (1,101):
    if i % 5 != 0 and i % 3 != 0:
        print(i)
    elif i % 5 == 0 and i % 3 == 0:
        print("FizzBuzz")  
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 ==0:
        print("Fizz")