# Taking the input of a list of student heights and then splitting them into a list. Then it is
# converting the list into integers. Then it is adding the total heights of the students. Then it is
# dividing the total heights by the number of students. Then it is rounding the average to the nearest
# whole number. Then it is printing the average.
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
    total_heights = 0
    for x in student_heights:
        total_heights += int(x)  
average = round(total_heights / (n + 1))
print(average)