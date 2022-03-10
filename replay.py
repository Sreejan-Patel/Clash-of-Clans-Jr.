import os
import sys
from colorama import Fore, Style, Back
import numpy as np

def print_replay(replay_file):
    """
    Prints the contents of a replay file.
    """
    with open(replay_file, 'r') as f:
        lines = f.readlines()
        frame = []
        check_clear = 0
        for line in lines:
            frame.append(line)
            check_clear += 1
            if check_clear % 41 == 0:
                os.system('clear')
                print(''.join(frame))
                os.system('sleep 0.1')
                frame.clear()

replay_number = input("Enter the number of the replay file you want to view: ")
replay_file = "./replays/replay_" + replay_number + ".txt"
print_replay(replay_file)