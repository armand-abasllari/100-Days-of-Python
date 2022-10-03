#Write your code below this line 👇
def prime_checker(number):
    some_number = int(0)

    for i in range(1,n):
        if n % i == 0:
            some_number += 1           
    if some_number >= 2:
        print ("It's not a prime number.")
    else:
        print ("It's a prime number.")



#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
