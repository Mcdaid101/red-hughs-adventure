import time
import sys
from time import sleep
import os
import re
import colorama
from colorama import Fore
from images import art
from scripts import script
from games import warden_game


key = False
sword = False


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
        time.sleep(0.0001)


def start_game():
    """
    gets the players name and begins the game. 
    """
    clear_screen()
    delay_print(Fore.GREEN + "It's christmas night in Dublin castle, the year is 1591 AD")
    print(art['start'])
    delay_print(script['start'])
    user = input("What is your name prisoner?  ")
    global name
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
            clear_screen()
            watch_house()
        elif user_input == "right":
            delay_print("You chose " + user_input + " to enter the Courtyard\n")
            delay_print("Loading Area........\n")
            clear_screen()
            courtyard()
        else:
            delay_print("You chose " + user_input + " to enter the Dungeon\n")
            delay_print("Loading Area........\n")
            clear_screen()
            dungeon()
    


def watch_house():
    """
    Loads the watchhouse area.
    """
    print(art['watch_house'])                                            
    delay_print(script['watch_house_one'])
    delay_print("There's not much in here " + name + " we should move on to the next room I already\nlooted the place.\n")
    delay_print(script['watch_house_two'])
    print("Go: right / left")
    user_input = input()

    while not re.match("^[forward, right, left]*$", user_input):
        user_input = input("Please enter either: right or left: \n")
    else:
        if user_input == "left":
            delay_print("You chose " + user_input + " to enter the Courtyard\n")
            delay_print("Loading Area........\n")
            clear_screen()
            courtyard()
        else:
            delay_print("You chose " + user_input + " to enter the Dungeon\n")
            delay_print("Loading Area........\n")
            clear_screen()
            dungeon()


def dungeon():
    """
    Loads the Dungeon cells area
    """
    print(art['dungeon'])
    delay_print(script['dungeon'])
    print("Go: left/ right")
    user_input = input()

    while not re.match("^[left, right]*$", user_input):
        user_input = input("Please enter either: left or right\n")
    else:
        if user_input == "left":
            delay_print("You chose " + user_input + " to enter the Warden's office\n")
            delay_print("Loading Area........\n")
            clear_screen()
            wardens_office()
        else:
            delay_print("You chose " + user_input + " to enter the Barracks\n")
            delay_print("Loading Area........\n")
            clear_screen()


def warden_game():
    """
    Mini game to pickpocket keys in the wardens office function
    """
    global key
    pick = input()
    if pick == "a":
        key = True
        print("You got the key")
        delay_print("Now lets head to the courtyard")
        delay_print("Loading Area........\n")
        clear_screen()
        courtyard()
    else:
        print("You died")


def wardens_office():
    """
    Loads the wardens office area
    """
    print(art['wardens_office'])
    delay_print(script['warden_office_script'])
    print("What do you think " + name + " should we try pickpocket him?")
    print("Enter: yes / no")
    pickpocket = input()

    while not re.match("^[yes, no]*$", pickpocket):
        pickpocket = input("Please enter either: yes or no\n")
    else:
        if pickpocket == "yes":
            delay_print("Go on " + name + " you can do it!\n")
            delay_print(script['accept_pick_pocket'])
            warden_game()
        else:
            delay_print(script['refuse_pick_pocket'])
            print("Enter: forward / right")
            direction = input()
            while not re.match("^[forward, right]*$", direction):
                direction = input("Please enter either: forward or right\n")
            else:
                if direction == "forward":
                    delay_print("You chose " + direction + " to enter the Barracks\n")
                    delay_print("Loading Area........\n")
                    clear_screen()
                else:
                    delay_print("You chose " + direction + "to enter the Courtyard")
                    delay_print("Loading Area........\n")
                    clear_screen()
                    courtyard()


def courtyard():
    """
    Loads the courtyard function
    """
    print(art['courtyard'])
    delay_print(script['courtyard'])
    print("Enter: north / south / east / west / back")
    user_input = input()

    while not re.match("^[north, south, east, west, back]*$", user_input):
        user_input = input("Please enter either: north, south, east, west or back\n")
    else:
        if user_input == "north":
            delay_print("You chose " + user_input + " to enter the Armoury\n")
            delay_print("Loading Area........\n")
            clear_screen()
            armoury()
        elif user_input == "south":
            delay_print("You chose " + user_input + " to enter the Tunnels\n")
            delay_print("Loading Area........\n")
            clear_screen()
            tunnels()
        elif user_input == "east":
            delay_print("You chose " + user_input + " to enter the Gates\n")
            delay_print("Loading Area........\n")
            clear_screen()
            gates()
        elif user_input == "back":
            delay_print("You chose " + user_input + " to enter the Dungeon\n")
            delay_print("Loading Area........\n")
            clear_screen()
            dungeon()
        elif user_input == "west":
            delay_print("You chose " + user_input + " to enter the Infirmary\n")
            delay_print("Loading Area........\n")
            clear_screen()
            infirmary()


def armoury():
    """
    Loads the Armoury scene
    """
    global sword
    print(art['armoury'])
    delay_print(script['armoury'])
    print("Enter: yes / no")
    user_input = input()

    while not re.match("^[yes, no]*$", user_input):
        user_input = input("Please enter either: yes / no\n")
    else:
        if user_input == "yes":
            sword = True
            delay_print(script['accept_sword'])
            delay_print("Loading Area........\n")
            clear_screen()
            courtyard()
        else:
            delay_print(script['deny_sword'])
            delay_print("Loading Area........\n")
            clear_screen()
            courtyard()

    
    


def tunnels():
    """
    Loads the tunnels scene
    """
    print(art['tunnels'])
    delay_print(script['tunnels'])
    delay_print("Loading Area........\n")
    clear_screen()
    courtyard()



def gates():
    """
    Loads the castle gates scene
    """
    global key
    print(art['gates'])
    
    if key:
        delay_print(script['gates_key'])
        delay_print("We did it " + name + " we're finally free, let's take those horses and get back to Donegal!")
        clear_screen()
        play_again()
    else:
        delay_print("Looks like it is locked we need to find a key, let's head back")
        delay_print("Loading Area........\n")
        clear_screen()
        courtyard()



def infirmary():
    """
    Loads the infirmary scene
    """
    print(art['infirmary'])


def play_again():
    delay_print(art['escaped'])
    print("Congratulations " + name + " you win!")
    print("Would you like to play again?")
    print("Enter: yes / no")
    user_input = input()
    
    if user_input == "yes":
        start_game()
    else:
        delay_print(art['goodbye'])

def main():
    """
    Main game function
    """
    start_game()
    
 
main()

