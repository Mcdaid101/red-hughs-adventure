from images import art

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
    

