#Imports
import random
import sys
import time

#Classes
class Inventory:
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
class Skills:
    """A bank of skills that player will collect on mission"""

    skills: {
        'espionage': ['follow', 'record', 'plant'],
        'technology': ['decrypt', 'encrypt', 'storage'],
        'combat': ['hand_to_hand', 'firearm']
    }

#Functions
def code_name():
    """Takes the name input from user and returns code name"""

    first_word = {
        'a': "anaconda", 
        'b': "barracuda", 
        'c': "cobra", 
        'd': "desert", 
        'e': "eagle", 
        'f': "fishlake", 
        'g': "grass", 
        'h': "hill", 
        'i': "ibis", 
        'j': "jaguar", 
        'k': "kiwi", 
        'l': "lagoon", 
        'm': "mountain", 
        'n': "nightingale", 
        'o': "ocean", 
        'p': "plateau", 
        'q': "quill", 
        'r': "reef", 
        's': "serpent", 
        't': "tree", 
        'u': "uranus", 
        'v': "volcano", 
        'w': "waterfall", 
        'x': "xeranthemum", 
        'y': "yellowhammer", 
        'z': "zebra"
    }
    second_word = {
        'a': "arch", 
        'b': "bridge", 
        'c': "canyon", 
        'd': "desert", 
        'e': "earthquake", 
        'f': "fountain", 
        'g': "garrison", 
        'h': "hurricane", 
        'i': "island", 
        'j': "jewel", 
        'k': "keystone", 
        'l': "lightning", 
        'm': "monastery", 
        'n': "nubbin", 
        'o': "obelisk", 
        'p': "plain", 
        'q': "quarry", 
        'r': "rapids", 
        's': "storm", 
        't': "tornado", 
        'u': "umbrella", 
        'v': "valley", 
        'w': "waterfall", 
        'x': "xenagogy", 
        'y': "yardang", 
        'z': "zimmer"
    }

    print("Now just to give you a code name. We can't risk any foreign interceptions revealing your assignment.")
    time.sleep(2.5)
    original_name = input("I'm going to need your real name before we get started: ").lower()
    first_letter = original_name[0]
    last_letter = original_name[-1]
    
    code = first_word[first_letter] + " " + second_word[last_letter]  
    
    time.sleep(3.5)
    print("Working...")
    time.sleep(3.5)
    print(f"Alright, from now on, you will be known as {code} or {first_letter.lower()}_{last_letter.upper()} for short.")
    time.sleep(1.5)
    print("Now you're ready to go.")

    return code

#Introductory Procedure
time.sleep(3.0)
print("")
print("")
print("Welcome to the Egg, the headquarters of the GSS")
time.sleep(1.5)
print("The CIA sent you here to aid in our hunt of the corrupt Prime Minister of Translutia, who the FBI have labelled as a national security threat of the highest order.")
time.sleep(3)
print("You have shown good discipline in the field, and you could be a great asset to us.")
time.sleep(1.5)
code_name()
time.sleep(1.5)
print("You've been given some basic tools to help you in addition to your own skillset.")
time.sleep(1.5)
print("You'll be going in to scout the area before we send in the senior team.")
time.sleep(1.5)
print("You are to stay silent and report ONLY. We don't want to cause an international crisis here.")
time.sleep(1.5)
print("With that all said and done, your train to Translutia leaves in 20 minutes. Don't miss it.")
time.sleep(2)
print("")
time.sleep(0.75)
print("")
time.sleep(0.75)
print("                                         (▀̿Ĺ̯▀̿ ̿)                                              ")
time.sleep(0.75)
print("")
time.sleep(0.75)
print("")
time.sleep(0.75)