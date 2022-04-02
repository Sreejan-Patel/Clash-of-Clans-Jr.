from src.village import Village
import os

os.system('clear')

print("Choose a level to start the game:\n1 - Easy\n2 - Medium\n3 - Hard\n")
level = int(input("Enter a number: "))
if level != 1 and level != 2 and level != 3:
    print("Invalid level.\n")
    exit()
else:
    village = Village(level)

    if village.level != 0:
        while(True):
            key = village.get_key()
            if key == 'c':
                break
            elif village.game_result == 0:
                village.render()
            else:
                break
    