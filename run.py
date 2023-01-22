import time
import sys
from time import sleep
import os
import re
import colorama
from colorama import Fore
from images import art
from scripts import script
from rich.progress import track
import random


key = False
sword = False


def progress_bar():
    """
    Adds a progress bar to simulate each function room /area
    being loaded
    """
    for i in track(range(3), description="Loading Area..."):
        time.sleep(0.33)


def clear_screen():
    """
    Function clears screen after each scene/function is called.
    """
    os.system("cls" if os.name == "nt" else "clear")


def delay_print(s):
    """
    This function delays text output to a slower speed,
    making it look like the text is being printed out one
    letter at a time

    """
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)


def display_scene(x="", y=""):
    """
    This function displays the scenes image and script at
    the beginning of each scene / area. 
    takes paramters from the art and script dictionaries
    """
    print(Fore.GREEN + art[x])
    delay_print(Fore.GREEN + script[y])


def start_game():
    """
    gets the players name and begins the game.
    A while loop makes sure the player enters a name
    before letting them continue.
    """
    global user
    clear_screen()
    delay_print(
        Fore.GREEN + "It's christmas night in Dublin castle, the year is 1591 AD"
    )
    display_scene("start", "start")
    while True:
        user = input("What is your name prisoner:  ")
        if not user:
            print(Fore.RED + "You must enter a name to continue")
            continue
        else:
            break
    global name
    name = user.capitalize()
    delay_print(Fore.GREEN + "Welcome " + name + " and best of luck on your quest!\n")
    progress_bar()
    clear_screen()
    intro()


def intro():
    """
    The opening scene of the game.
    """
    display_scene("intro", "intro_one")
    delay_print("This is our chance says Red let's go " + name + "!\n")
    delay_print(script["intro_two"])
    print("Enter: forward / right / left")
    user_input = input()

    while not re.match("^[forward, right, left]*$", user_input):
        user_input = input(Fore.RED + "Please enter either: forward, right or left: \n")
    else:
        if user_input == "forward":
            delay_print(
                Fore.GREEN + "You chose " + user_input + " to enter the Watchhouse\n"
            )
            progress_bar()
            clear_screen()
            watch_house()
        elif user_input == "right":
            delay_print(
                Fore.GREEN + "You chose " + user_input + " to enter the Courtyard\n"
            )
            progress_bar()
            clear_screen()
            courtyard()
        else:
            delay_print(
                Fore.GREEN + "You chose " + user_input + " to enter the Dungeon\n"
            )
            progress_bar()
            clear_screen()
            dungeon()


def courtyard():
    """
    Loads the courtyard function
    """
    display_scene("courtyard", "courtyard")
    print("Enter: north / south / east / west / back")
    user_input = input()

    while not re.match("^[north, south, east, west, back]*$", user_input):
        user_input = input(
            Fore.RED + "Please enter either: north, south, east, west or back\n"
        )
    else:
        if user_input == "north":
            delay_print(
                Fore.GREEN + "You chose " + user_input + " to enter the Armoury\n"
            )
            progress_bar()
            clear_screen()
            armoury()
        elif user_input == "south":
            delay_print(
                Fore.GREEN + "You chose " + user_input + " to enter the Tunnels\n"
            )
            progress_bar()
            clear_screen()
            tunnels()
        elif user_input == "east":
            delay_print(
                Fore.GREEN + "You chose " + user_input + " to enter the Gates\n"
            )
            progress_bar()
            clear_screen()
            gates()
        elif user_input == "back":
            delay_print(
                Fore.GREEN + "You chose " + user_input + " to enter the Dungeon\n"
            )
            progress_bar()
            clear_screen()
            dungeon()
        elif user_input == "west":
            delay_print(
                Fore.GREEN + "You chose " + user_input + " to enter the Infirmary\n"
            )
            progress_bar()
            clear_screen()
            infirmary()


def watch_house():
    """
    Loads the watchhouse area.
    """
    display_scene("watch_house", "watch_house_one")
    delay_print(
        "There's not much in here "
        + name
        + " we should move on to the next room I already\nlooted the place.\n"
    )
    delay_print(script["watch_house_two"])
    print("Enter: right / left")
    user_input = input()

    while not re.match("^[forward, right, left]*$", user_input):
        user_input = input(Fore.RED + "Please enter either: right or left: \n")
    else:
        if user_input == "left":
            delay_print(
                Fore.GREEN + "You chose " + user_input + " to enter the Courtyard\n"
            )
            progress_bar()
            clear_screen()
            courtyard()
        else:
            delay_print(
                Fore.GREEN + "You chose " + user_input + " to enter the Dungeon\n"
            )
            progress_bar()
            clear_screen()
            dungeon()


def dungeon():
    """
    Loads the Dungeon cells area
    """
    display_scene("dungeon", "dungeon")
    print("Go: left/ right")
    user_input = input()

    while not re.match("^[left, right]*$", user_input):
        user_input = input(Fore.RED + "Please enter either: left or right\n")
    else:
        if user_input == "left":
            delay_print(
                Fore.GREEN
                + "You chose "
                + user_input
                + " to enter the Warden's office\n"
            )
            progress_bar()
            clear_screen()
            wardens_office()
        else:
            delay_print(
                Fore.GREEN + "You chose " + user_input + " to enter the Barracks\n"
            )
            progress_bar()
            clear_screen()
            barracks()


def warden_game():
    """
    Mini game to pickpocket keys in the wardens office function.
    The player must choose a number between 1 and 2 for the correct
    answer which is randomly generated.
    """
    global key
    keys = random.randint(1, 2)
    pick = int(input("Enter 1 for coat, 2 for trousers  "))

    if pick == keys:
        key = True
        delay_print("You got the key! Now lets head to the courtyard\n")
        progress_bar()
        clear_screen()
        courtyard()
    else:
        clear_screen()
        print(Fore.RED + "You searched the wrong place and woke the warden!")
        game_over()


def wardens_office():
    """
    Loads the wardens office area.
    The player can then choose whether to play the pickpocket game
    or leave.
    """
    display_scene("wardens_office", "warden_office_script")
    print("What do you think " + name + " should we try pickpocket him?")
    print("Enter: yes / no")
    pickpocket = input()

    while not re.match("^[yes, no]*$", pickpocket):
        pickpocket = input(Fore.RED + "Please enter either: yes or no\n")
    else:
        if pickpocket == "yes":
            delay_print(Fore.GREEN + "Go on " + name + " you can do it!\n")
            delay_print(script["accept_pick_pocket"])
            warden_game()
        else:
            delay_print(script["refuse_pick_pocket"])
            print("Enter: forward / right")
            direction = input()
            while not re.match("^[forward, right]*$", direction):
                direction = input(Fore.RED + "Please enter either: forward or right\n")
            else:
                if direction == "forward":
                    delay_print(
                        Fore.GREEN
                        + "You chose "
                        + direction
                        + " to enter the Barracks\n"
                    )
                    progress_bar()
                    clear_screen()
                    barracks()
                else:
                    delay_print(
                        Fore.GREEN + "You chose " + direction + "to enter the Courtyard"
                    )
                    progress_bar()
                    clear_screen()
                    courtyard()


def armoury():
    """
    Loads the Armoury scene.
    The player can choose whether to pick up a sword
    """
    global sword
    display_scene("armoury", "armoury")
    print("Enter: yes / no")
    user_input = input()

    while not re.match("^[yes, no]*$", user_input):
        user_input = input(Fore.RED + "Please enter either: yes / no\n")
    else:
        if user_input == "yes":
            sword = True
            delay_print(Fore.GREEN + script["accept_sword"])
            progress_bar()
            clear_screen()
            courtyard()
        else:
            delay_print(Fore.GREEN + script["deny_sword"])
            progress_bar()
            clear_screen()
            courtyard()


def barracks():
    """
    Loads the barracks function.
    The way this scene is played out depends on if the player
    has found/ or accepted to pick up the sword from the armoury.
    """
    global sword
    display_scene("barracks", "barracks")

    if sword:
        delay_print(script["barracks_win"])
        delay_print("You and Red cut down the guard like a knife through butter\n")
        delay_print(
            "We did it "
            + name
            + " we're finally free, jump out and get back to Donegal!\n"
        )
        clear_screen()
        escape_play_again()
    else:
        delay_print("The guard slays you and Red as you were weaponless!\n")
        delay_print("Don't bring fists to a sword fight!\n")
        clear_screen()
        game_over()


def tunnels():
    """
    Loads the tunnels scene
    """
    display_scene("tunnels", "tunnels")
    progress_bar()
    clear_screen()
    courtyard()


def gates():
    """
    Loads the castle gates scene.
    The way this scene is played out depends on if the player
    has acquired the key from the warden.
    """
    global key

    if key:
        display_scene("gates", "gates_key")
        delay_print(
            "We did it "
            + name
            + " we're finally free, let's take those horses and get back to Donegal!"
        )
        clear_screen()
        escape_play_again()
    else:
        display_scene("gates", "gates_nokey")
        progress_bar()
        clear_screen()
        courtyard()


def infirmary():
    """
    Loads the infirmary scene
    """
    display_scene("infirmary", "infirmary")
    progress_bar()
    clear_screen()
    courtyard()


def escape_play_again():
    """
    Appears at games finish if the player escapes.
    Lets them play again if they choose to.
    """
    delay_print(Fore.GREEN + art["escaped"])
    print("Congratulations " + name + " you win!")
    print("Would you like to play again?")
    print("Enter: yes / no")
    user_input = input()

    if user_input == "yes":
        start_game()
    else:
        print(art["goodbye"])


def game_over():
    """
    Appears if they player is caught or killed.
    Lets them play again if they choose to.
    """
    print(Fore.RED + art["dead"])
    print(script["game_over"])
    print("Would you like to play again?")
    print("Enter: yes / no")
    user_input = input()

    if user_input == "yes":
        clear_screen()
        start_game()
    else:
        clear_screen()
        print(art["goodbye"])


def main():
    """
    Main game function
    """
    start_game()


main()
