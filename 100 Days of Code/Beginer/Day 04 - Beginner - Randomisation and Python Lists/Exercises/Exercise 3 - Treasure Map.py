# Creating a map with 3 rows and 3 columns.
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# Taking the input from the user and putting it into the map.

y = int(position[0])
x = int(position[1])
map[x-1][y-1] = "x"

print(f"{row1}\n{row2}\n{row3}")