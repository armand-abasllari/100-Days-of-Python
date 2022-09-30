# Adding all the even numbers from 1 to 100.
x = 0
for i in range(1,101):
    if i % 2 == 0:
        x += i 
print (x)