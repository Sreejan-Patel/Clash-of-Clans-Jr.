import os
import time
from src.village import Village

class Start():

    @staticmethod
    def intro():
        '''
        This function plays the intro sound
        '''
        os.system('afplay sounds/intro.wav -t 5 &')
        os.system("clear")
        print("\t\t\t\t\t\t\tWelcome to Clash of Clans Jr.!")
        time.sleep(5)

    @staticmethod
    def start_game():
        '''
        This function plays the starts the game
        '''
        win_level_1 = 0
        win_level_2 = 0
        win_level_3 = 0

        level = 1
        village = Village(level)

        while(True):
            key = village.get_key()
            if key == 'c':
                quit()
            elif village.game_result == 0:
                village.render()
            else:
                if village.game_result == 1:
                    win_level_1 = 1
                else:
                    win_level_1 = 0
                break

        if win_level_1 == 1:

            level = 2
            village = Village(level)

            while(True):
                key = village.get_key()
                if key == 'c':
                    quit()
                elif village.game_result == 0:
                    village.render()
                else:
                    if village.game_result == 1:
                        win_level_2 = 1
                    else:
                        win_level_2 = 0
                    break
            
            if win_level_2 == 1:
                    
                level = 3
                village = Village(level)
            
                while(True):
                    key = village.get_key()
                    if key == 'c':
                        quit()
                    elif village.game_result == 0:
                        village.render()
                    else:
                        if village.game_result == 1:
                            win_level_3 = 1
                        else:
                            win_level_3 = 0
                            break

                if win_level_3 == 1:
                    os.system('clear')
                    print("\t\t\t\t\t\t\t\t\tYou Win!!!")
                    time.sleep(2)
                    quit()
                else:
                    os.system('clear')
                    print("\t\t\t\t\t\t\t\t\tYou Lose!!!")
                    time.sleep(2)
                    quit()
            
            else:
                os.system('clear')
                print("\t\t\t\t\t\t\t\t\tYou Lose!!!")
                time.sleep(2)
                quit()
            
        else:
            os.system('clear')
            print("\t\t\t\t\t\t\t\t\tYou Lose!!!")
            time.sleep(2)
            quit()