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
        time.sleep(0.0)


def start_game():
    """
    gets the players name
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
    intro()
    

def intro():
    delay_print("You lie dreaming of your wife and kids, of freedom and a tankard of ale by the fire..\n")
    delay_print("Until Red Hugh shakes you awake, come on! now's our chance to get out of this dam castle\n")
    delay_print("Red Hugh unlocks your cufflinks with the key he stole from the guard\n")
    delay_print("This is our chance says Red but what's our plan where do we go from here " + name +"?\n")
    


def main():
    start_game()

main()

