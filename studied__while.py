
from winsound import PlaySound
from random import randint


distance = 0

while distance < 20:

    print("i'M RUNNING:", distance, "km")
    distance = distance+1

# Python Casino


print("Welcome to python Casino")
pc_choice = randint(1, 50)

playing = True

while playing:
    user_choice = int(input("Choose number(1~100):"))
    if user_choice == pc_choice:
        print("You won!", pc_choice)
        playing = False
    elif user_choice > pc_choice:
        print("Lower!", pc_choice)
    elif user_choice < pc_choice:
        print("Higher!", pc_choice)
