
def warden_game():
    """
    Mini game to pickpocket keys in the wardens office function
    """
    pick = input()
    if pick == "a":
        print("You got the key")
        key = True
    else:
        print("You died")