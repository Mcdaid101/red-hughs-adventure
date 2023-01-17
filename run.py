import time
import sys
from time import sleep

def delay_print(s):
    """
    This function delays text output to a slower speed
    """
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1)


def get_player_name():
    """
    gets the players name
    """
    delay_print("Welcome to Red Hugh's adventure\n")
    delay_print("Enter your name to begin your escape!\n")
    name = input("What is your name prisoner?\n")
    delay_print("Welcome " + name.capitalize() + " and best of luck!\n")
    delay_print("L O A D I N G -- G A M E ...")

get_player_name()



