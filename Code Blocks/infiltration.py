import pygame

codes = {
    'door': ['compound1', 'compound2'],

}

def door_unlocking():
    """Function that unlocks doors"""

    print("You are approaching a door.")

    check_code = codes['door'][0]
    if check_code == 'compound1':
        print("It seems to be a strong metal door.") 
        print("There is a 4x4 keypad on the side with a wide assortment of symbols, letters, and numbers.")
        print("Maybe the decoder will help...")
        
    elif check_code == 'compound2':
        hrkjh
    elif check_code == 'compound3':
        hkjg
    else:
        print("You do not have the correct decoder to try this door. Find the encryption and try again.")

door_unlocking()