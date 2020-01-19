#Imports
import random
import sys
import time
#import pygame

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

story_items {}

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
    ##(2.5)
    original_name = input("I'm going to need your real name before we get started: ").lower()
    first_letter = original_name[0]
    last_letter = original_name[-1]
    
    code = first_word[first_letter] + " " + second_word[last_letter]  
    
    ##(3.5)
    print("Working...")
    ##(3.5)
    print(f"Alright, from now on, you will be known as {code} or {first_letter.lower()}_{last_letter.upper()} for short.")
    ##(1.5)
    print("Now you're ready to go.")

    return code

def packages(package):
    """Opens and sends messages about reports"""

    print("You have received a package.")
    open_package = input("Would you like to open it? ").lower()
    
    while open_package != 'yes' or 'y' or 'n' or 'no':
        print("please choose if you would like to open the box. Answer with 'yes', 'y', 'no', or 'n'.")
    if open_package == 'yes' or 'y':
        print(package)
    elif open_package == 'no' or 'n':
        print("The package will be safely dealt with.")
        
def commands(command):
    """Function for receiving commands"""

    print("You have received a letter from HQ.")
    
    for items in command:
        print(items)

def park():
    """Park location in Hagenstade"""

    time = 10
    chosen = []
    
    print("You have arrived at Freedom Park.") 
    print("Yes, I realize that it is an oxymoron to have a park named 'Freedom' in a dictatorship country. Don't ask about it.")
    print("This park is about a square kilometer in area, and is right by the sea. There isn't much going on here, though.")
    print("On the north side, there is a giant mounted rocket, probably to instill fear in the people.")
    print("The east side, where you are right now, has a wilting flower garden to the side, and a dried out fountain to the other side.")
    print("The south side has a big square building, but we're not sure what is there.")
    print("The west side has a degraded basketball court, and the center of the park has a big grassy oval.")
    print("Everything is pretty barren and devoid of life. You're the only one in the entire park.")
    print(f"The time right now is 10:00. You have {time} hours to explore and get back to your dormitory before curfew.")
    print("Each section will take a different chunk of your time, so choose wisely.")

    section = input("Which area would you like to explore first? ").lower()

    while section not in ["west" , "east" , "north" , "south" , "center"]:
        section = input("Choose one of the cardinal directions + the center where each thing is located. ").lower()
    
    while time > 0:
        if section == 'north':
            while section in chosen:
                section = ("You have already chosen to go north. Please choose another section. ").lower()
            
            chosen.append("north")

            print("The rocket looks very imposing as you approach. It is at least 50 meters tall, angled towards the sea.")
            print("It has a big black ribbed mount with a diameter of at least 3 meters.")
            print('A lone plaque behind the rocket reads, "Markareshi III Rocket. First rocket in failed nuclear weapons program."')
            
            rusure = input("There isn't much to see here. Do you still want to explore the area? ").lower()

            while rusure != "yes" and "no":
                rusure = input("Please state a yes or no answer.")

            if rusure == "no":
                time -= 0.5
                print(f"You have {time} hours left.")
                section = input("Which area would you like to explore next? ").lower()
            
            if rusure == "yes" and time > 0.5:
                time -= 0.5
                print("After further inspection of the rocket, you find a small panel of the rocket where the exterior was ripped off.")
                print("Hidden behind one of the wall panels, you find a small keycard, with a blue stripe and the letters Ξ Π Λ Γ")
                story_items["keycard"] = 1
                print("You continue to look around the rocket. You notice a little crack near the base of the mount.")
                print("The crack oddly looks like the shape of an arrow going up. You look up at the rocket.")
                print("Maybe you should use your binoculars...")
                print("You zoom in with the binoculars, and spot a little slit right at the base of the nose cone. It has to be at least 40 meters up.")
                print("A fall from that height would surely break bones. Worse yet, someone could spot you, and the mission would be in jeopardy.")
                print("Is it worth the mission if it's just a crack and not anything special?")

                going_up = input("Do you want to climb the rocket, knowing full well of the consequences? ").lower()

                while going_up != "yes" and "no"
                    going_up = input("No time to spare. The rocket looms overhead. Do you climb it? ")
                
                if going_up == "no":
                    print(f"you have {time} hours left.")
                    section = input("Which area would you like to explore next? ").lower()
                
                if going_up == "yes":
                    print("You slowly go up the rocket, being careful of each step.")
                    print("Suddenly a whistle pierces the silence of the park. You've been spotted!")
                    print("You scramble up the rocket faster. You are now making plenty of noise. It seems you've caught the attention of the whole city.")
                    print("The guard below you is shouting at you. You can't understand him, however.")
                    print("Just as you make it to the nose cone, you hear a loud bang. A quick glanse beneath you reveals the guard holding a handgun.")
                    print("You have only seconds. You insert the keycard into the slot, and wait. The guard shoots again.")
                    print("A third shot rings out. This guard has terrible aim. *cough* plot armor *cough*")
                    print("Miraculously, the keycard ejects from the slot and the nose cone begins to lift.")
                    print("The hydraulics reveal an opening, and you quickly stumble through. In your haste, your flashdrive gets caught on the metal and falls.")
                    del tools["flashdrive"]
                    print("You can't think about the lost flashdrive however. Let's hope nothing important was on there.")
                    
                    #rocket()
                
            else:
                print("You do not have enough time to explore the area. Please choose a different section")
                section = input("Which area would you like to explore next? ").lower()
    
    if time == 0:
        print("You have ran out of time for today. You must return to the hotel immediately.")
        print(f"Good night Agent {agent_name}. Your next instructions will be sent tomorrow morning.")
         
def rocket()

def Hagenstade(score, hours):
    """Sequence for player"""

    if hours == 73:
        print("The parade will be held in three days, and begins at 09:00. The time right now is 08:00. That leaves you with 73 hours.")
        print("Until then, explore the area, collect intel, and gain skills and tools to help you in Translutia.")
        print("While you do explore Hagenstade, be wary of the curfew, which is at 20:00 sharp. Anyone not in their house by curfew will be arrested.")
        print("Hagenstade has five major locations worth investigating. Each one will take a day of your time, so make sure to choose wisely. You can only visit three before the parade.")
        print("Each location will be patrolling with guards and police. However, each location has differing security measures and officers.")
        print("The five locations are as follows, in increasing security levels: the park, the train station, the port, the tallest building, and the national bank.")
        print("The building and the bank offer the most to gain, but also pose the most risk. We do not need to remind you that capture and arrest is not an option.")
        print("Your capture puts the whole operation at risk. The GSS trusts you to make the right decisions. Other than that, your time is yours.")

        first_loc = input("Where would you like to go first? (exclude the 'the' in your answer)  ").lower()

        while first_loc not in ["park", "train station", "port", "building", "bank", "tallest building", "national bank"]:
            first_loc = input("Please choose one of the five locations. You only have a limited time to explore. ").lower()

        hours = locations(first_loc, hours)

def locations(choice, hours):
    """To be used with Hagenstade function for ease of use"""

    if choice == "park":
        hours -= 24
        park()
        return hours

def main():
    #Introductory Procedure
    ##(3.0)
    print("")
    print("")
    print("Welcome to the Egg, the headquarters of the GSS")
    ##(1.5)
    print("The CIA sent you here to aid in our hunt of the corrupt Prime Minister of Translutia, who the FBI have labelled as a national security threat of the highest order.")
    ##(3)
    print("You have shown good discipline in the field, and you could be a great asset to us.")
    ##(1.5)
    agent_name = code_name()
    ##(1.5)
    print("You've been given some basic tools to help you in addition to your own skillset.")
    ##(1.5)
    print("You'll be going in to scout the area before we send in the senior team.")
    ##(1.5)
    print("You are to stay silent and report ONLY. We don't want to cause an international crisis here.")
    ##(1.5)
    print("I will be helping you along the way, making sure you're on the right track.")
    ##(1.5)
    print("Headquarters will also send you some commands, which you will receive on your phone. Don't lose it.")
    ##(1.5)
    print("Expect your first command at exactly 08:00. Make sure you read it in secret.")
    ##(1.5)
    print("With that all said and done, your train to Translutia leaves in 20 minutes. Don't miss it.")
    ##(2)
    print("")
    ##(0.75)
    print("")
    ##(0.75)
    print("                                         (▀̿Ĺ̯▀̿ ̿)                                              ")
    ##(0.75)
    print("")
    ##(0.75)
    print("")
    ##(0.75)

    #First Action Variables
    hours = 73
    score = 0

    command_1 = [
        f"Agent {agent_name}.",
        f"    Welcome to Translutia, more specifically, the biggest port city of Hagenstade.",
        f"    This city is the most democratic in the country, and as a result is under strict supervision under the dictatorship.",
        f"    This city is crawling with spies and counterspies. Be of utmost precaution.",       
        f"    The city will be hosting its annual celebratory festival in honor of dictator Bashmany Rotendero.",
        f"    We need you to scout the parade that will be held there. ",
        f"    The parade begins in Hagenstade, and ends at the capital, Rotendale.",
        f"    The parade will provide perfect cover for the senior team.",
        f"    The senior team will then infiltrate the parade, and then enter Rotendero's compound."
        f"    You are there to make sure no one sabotages the parade, and intervenes in our plans. ",
        f"    The senior team will arrive in two days. The parade will be the day after.",
        f"    We will be sending you some packages as well. These packages contain valuable tools and information.",
        f"    However, we urge you to be wary. The dictator most surely knows you are in the country, and they will be trying to put a stop to the mission.",
        f"    Be suspicious of everything. You will know something is ours if we mention it beforehand, or a decrypted message reads GSS.",
        f"    Good luck agent. Your first package will be dropped tomorrow."
        ]

    commands(command_1)

    hours = Hagenstade(score, hours)

if __name__ == "__main__":
    main()

"""pygame.init()

screen = pygame.display.set_mode( (1200, 650) )

font = pygame.font.SysFont("Courier New", 250)

codes = {
    'door': ['compound1', 'compound2']
}

sequence = 'door'

def door_unlocking():
    """'Function that unlocks doors'"""

    print("You are approaching a door.")

    check_code = codes['door']
    if 'compound1' == check_code:
        text1 = font.render("L T X G", True, (225, 225, 225))
        text2 = font.render("L T X G", True, (225, 225, 225))
        text3 = font.render("L T X G", True, (225, 225, 225))
        text4 = font.render("L T X G", True, (225, 225, 225))
        xpos = 50
        ypos = 50

        print("It seems to be a strong metal door.") 
        print("There is a 4x4 keypad on the side with a wide assortment of symbols, letters, and numbers.")
        print("Maybe the decoder will help...")
        
        screen.blit(text1, (xpos, ypos))
        ypos += 250
        screen.blit(text2, (xpos, ypos))
        ypos += 250
        screen.blit(text3, (xpos, ypos))
        ypos += 250
        screen.blit(text4, (xpos, ypos))
        pygame.display.flip()
        
    elif check_code == 'compound2':
        Filler
    elif check_code == 'compound3':
        Filler
    else:
        print("You do not have the correct decoder to try this door. Find the encryption and try again.")

while True:"""

