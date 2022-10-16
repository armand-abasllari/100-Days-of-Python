# This is taking the input from the user and splitting it into a list. Then it is converting the list
# into integers.
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

# This is taking the highest score and comparing it to the next score in the list. If the next score
# is higher than the highest score, then it will replace the highest score with the new score.
highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score

    
print(f"The highest score in the class is: {highest_score}")


