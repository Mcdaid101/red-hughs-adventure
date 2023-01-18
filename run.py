import time
import sys
from time import sleep
import os
import re
import colorama
from colorama import Fore
from images import art
from scripts import script
from rich.panel import Panel
from rich.text import Text


def clear_screen():
    """
    Function clears screen after each scene/function is called.
    """
    os.system('cls' if os.name=='nt' else 'clear')

def delay_print(s):
    """
    This function delays text output to a slower speed for style purposes. 

    """
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.0)


def start_game():
    """
    gets the players name and begins the game. 
    """
    delay_print(Fore.GREEN + "It's christmas night in Dublin castle, the year is 1591 AD")
    print(art['start'])
    delay_print(script['start'])
    global name
    user = input("What is your name prisoner?\n")
    name = user.capitalize()
    delay_print("Welcome " + name + " and best of luck on your quest!\n")
    delay_print("L O A D I N G  G A M E ...\n")
    clear_screen()
    intro()
    

def intro():
    """
    The opening scene of the game.
    """
    print(art['intro'])
    delay_print(script['intro_one'])
    delay_print("This is our chance says Red let's go " + name +"!\n")
    delay_print(script['intro_two'])
    print("Go: forward / right / left")
    user_input = input()

    while not re.match("^[forward, right, left]*$", user_input):
        user_input = input("Please enter either: forward, right or left: \n")
    else:
        if user_input == "forward":
            delay_print("You chose " + user_input + " to enter the Watchhouse\n")
            delay_print("Loading Area........\n")
            watch_house()
        elif user_input == "right":
            delay_print("You chose " + user_input + " to enter the Courtyard\n")
            delay_print("Loading Area........\n")
        else:
            delay_print("You chose " + user_input + " to enter the Cells\n")
            delay_print("Loading Area........\n")
    


def watch_house():
    """
    Loads the watchhouse area.
    """
    clear_screen()
    print(art['watch_house'])                                            
    delay_print(script['watch_house_one'])
    delay_print("There's not much in here " + name + " we should move on to the next room I already looted the place.\n")
    delay_print(script['watch_house_two'])
    print("Go: forward / right / left")
    user_input = input()

    while not re.match("^[forward, right, left]*$", user_input):
        user_input = input("Please enter either: forward, right or left: \n")
    else:
        if user_input == "forward":
            delay_print("You chose " + user_input + " to enter your old cell\n")
            delay_print("Loading Area........\n")
        elif user_input == "left":
            delay_print("You chose " + user_input + " to enter the Courtyard\n")
            delay_print("Loading Area........\n")
        else:
            delay_print("You chose " + user_input + " to enter the Cells\n")
            delay_print("Loading Area........\n")
    


def main():
    start_game()

main()

