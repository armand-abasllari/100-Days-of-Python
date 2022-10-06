import random


# A rock paper scissors game.
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice = [rock,paper,scissors]



user = int(input ("Pick your shape 0-Rock or 1-Paper or 2-Scissors: "))


if user == 0:
    print (choice[user])
    robot = (choice[random.randint(0,2)])
    print(robot)
    if robot == (choice[1]):
        print("You Lose")
    elif robot == (choice[0]):
        print("You Draw")
    else:
        print("You Win")
elif user == 1:
    print (choice[user])
    robot = (choice[random.randint(1,2)])
    print(robot)
    if robot == (choice[0]):
        print("You Win")
        print(robot)
    elif robot == (choice[1]):
        print("You Draw")
    else:
        print("You Lose")
        
elif user == 2:
    print (choice[user])
    robot = (choice[random.randint(1,2)])
    print(robot)
    if robot == (choice[0]):
        print("You Win")
        print(robot)
    elif robot == (choice[2]):
        print("You Draw")
    else:
        print("You Lose")
else:
    user <= 0 or user >= 3
    print("You picked a wrong number. Start Again")
