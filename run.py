import time
import sys
from time import sleep
import os
import re

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
        time.sleep(0.05)


def start_game():
    """
    gets the players name and begins the game. 
    """
    delay_print("Welcome to Red Hugh's adventure!\n")
    delay_print("A text adventure game where you must escape Dublin castle\n")
    delay_print("with the gaelic chieftain Red Hugh O'Donnell\n")
    delay_print("Enter your name to begin your escape...\n")
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
    print("    ____       _                               ____") 
    print("   / __ \_____(_)________  ____     ________  / / /") 
    print("  / /_/ / ___/ / ___/ __ \/ __ \   / ___/ _ \/ / /")   
    print(" / ____/ /  / (__  ) /_/ / / / /  / /__/  __/ / /")    
    print("/_/   /_/  /_/____/\____/_/ /_/   \___/\___/_/_/")      

    delay_print("You lie dreaming of your wife and kids, of freedom and a tankard of ale by the\n")
    delay_print("fire..\n")
    delay_print("Until Red Hugh shakes you awake, come on! now's our chance to get out of this\n")
    delay_print("dam castle\n")
    delay_print("Red Hugh unlocks your cufflinks with the key he stole from the guard\n")
    delay_print("This is our chance says Red let's go " + name +"!\n")
    delay_print("The cell door swings open, now how will you escape?\n")
    clear_screen()
    delay_print("The watchhouse is straight ahead, the courtyard is on the right and the cells are on our left whispers Red")
    print("Go: Forward / Right / Left")
    user_input = input()

    while not re.match("^[forward, right, left]*$", user_input):
        user_input = input("Please enter either: forward, right or left: ")
    else:
        if user_input == "forward":
            delay_print("You chose " + user_input + " to enter the Watchhouse")
            delay_print("Loading Area........\n")
            watch_house()
        elif user_input == "right":
            delay_print("You chose " + user_input + " to enter the Courtyard")
            delay_print("Loading Area........\n")
        else:
            delay_print("You chose " + user_input + " to enter the Cells")
            delay_print("Loading Area........\n")
    


def watch_house():
    print(" _       __      __       __    __")
    print("| |     / /___ _/ /______/ /_  / /_  ____  __  __________")
    print("| | /| / / __ `/ __/ ___/ __ \/ __ \/ __ \/ / / / ___/ _ \ ")
    print("| |/ |/ / /_/ / /_/ /__/ / / / / / / /_/ / /_/ (__  )  __/")
    print("|__/|__/\__,_/\__/\___/_/ /_/_/ /_/\____/\__,_/____/\___/")
                                                        
    delay_print("You open the door of the watch house, the prison guard lies dead on the cold floor\n")



def main():
    start_game()

main()

