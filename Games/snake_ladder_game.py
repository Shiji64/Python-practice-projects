import random

print("----Snake Ladder Game----\n")

print("--------------------------\n")

print("Game Started\n")

print("------------\n")

player_pos = comp_pos = 0 
snake_points ={ 25:3 , 42:1,56:48,61:43,92:67,95:12,98:80 }  
ladder_points = { 7:30,16:33,20:38,36:83,50:68,63:81,71:89,86:97 }
print(f"Computer's Position : {comp_pos}")
print(f"Player's Position : {player_pos}")
while True:
    #Player's Turn

    print("\nPlayer's Turn")
    while True:
        player_inp = input("Press Enter to roll the dice: ")

        if(player_inp == ""):
            dice = random.randint(1,6)
            print("You rolled : ", dice)
            break
        else:
            print("Please press Enter only...")

    if player_pos+dice <= 100:

        player_pos = player_pos + dice
        print(f"You moved to {player_pos}!!!\n")
        if player_pos in snake_points:
            player_pos = snake_points[player_pos]
            print(f"You got a snake.You moved down to {player_pos}.")
        elif player_pos in ladder_points:
            player_pos = ladder_points[player_pos]
            print(f"You got a ladder.You climbed up to {player_pos}.")

        if player_pos == 100:
            print("Congratulations! You won the game !")
            print("------- Game Over -------")
            break
        else:
            print(f"You are at position {player_pos}.")
    else:
        print(f"You are at position {player_pos} and you rolled {dice},so you cannot move.")
        print(f"You remain at {player_pos}")

    #Computer's Turn


    print("\nComputer's Turn")

    comp_dice = random.randint(1,6)
    print("Computer rolled : ", comp_dice)

    if comp_pos+comp_dice <= 100:
        comp_pos = comp_pos + comp_dice
        print(f"Computer moved to {comp_pos}!!!\n")

        if comp_pos in snake_points:
            comp_pos = snake_points[comp_pos]
            print(f"Computer got a snake.Computer moved down to {comp_pos}.")
        elif comp_pos in ladder_points:
            comp_pos = ladder_points[comp_pos]
            print(f"Computer got a ladder.Computer climbed up to {comp_pos}.")

        if comp_pos == 100:
            print("Congratulations! Computer won the game !")
            print("------- Game Over -------")
            break
            
        else:
            print(f"Computer is at position {comp_pos}.")
    else:
            print(f"Computer is at position {comp_pos} and  rolled {comp_dice},so Computer cannot move.")
            print(f"Computer remains at {comp_pos}")

    print(f"Computer's Position : {comp_pos}")
    print(f"Player's Position : {player_pos}")          