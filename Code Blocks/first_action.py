#Brought from introduction to make code work

#Imports
import random
import sys

#Classes
class Inventory():
    """Creating player's inventory for their mission"""

    tools = {
        'binoculars': {
            'quantity': 1,
            'uses': ['zoom_in', 'night_vision', 'thermal_vision']
        },
        'bug' :  {
            'quantity': 3,
            'uses': ['eavesdrop', 'record']
        },
        'camera':  {
            'quantity': 1,
            'uses': ['zoom_in', 'taking_pictures', 'image_filtering', 'image_to_chip']
        },
        'flashdrive':  {
            'quantity': 1,
            'uses': ['storage']
        },
        'phone':  {
            'quantity': 1,
            'uses': ['receive_instructions', 'erase', 'tracking', 'self_destruct']
        }
    }
class Skills():
    """A bank of skills that player will collect on mission"""

    skills: {
        'espionage': ['follow', 'record', 'plant'],
        'technology': ['decrypt', 'encrypt', 'storage'],
        'combat': ['hand_to_hand', 'firearm']
    }


def Packages(package):
    """Opens and sends messages about reports"""

    print("You have received a package.")
    open_package = input("Would you like to open it? ").lower()

    if open_package == 'yes':
        print(package)
    else:
        print("The package will be safely dealt with.")

def Commands(command):
    """Function for receiving commands"""

    print("You have received a letter from HQ.")
    print(command)

Commands(CommA)    

CommA = {
    print(f"Agent {code}.")
    print(f"    Welcome to Translutia, more specifically, the biggest port city of Hagenstade.")
    print(f"    This city is the most democratic in the country, and as a result is under strict supervision under the dictatorship.")
    print(f"    This city is crawling with spies and counterspies. Be of utmost precaution.")        
    print(f"    The city will be hosting its annual celebratory festival in honor of dictator Bashmany Rotendero.")
    print(f"    We need you to scout the parade that will be held there. ")
    print(f"    The parade begins in Hagenstade, and ends at the capital, Rotendale. The senior team will then infiltrate the dictator's compound.")
    print(f"    You are there to make sure no one sabotages the parade, and intervenes in our plans. ")
    print(f"    The senior team will arrive in two days. The parade will be the day after.")
    print(f"    We will be sending you some packages as well. These packages contain valuable tools and information.")
    print(f"    However, we urge you to be wary. The dictator most surely knows you are in the country, and they will be trying to put a stop to the mission.")
    print(f"    Be suspicious of everything. You will know something is ours if we mention it beforehand, or a decrypted message reads GSS.")
    print(f"    Good luck agent. Your first package is at the back left door of the train station.")
}