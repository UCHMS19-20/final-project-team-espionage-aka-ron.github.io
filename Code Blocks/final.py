#Imports
import random
import sys
import time
import pygame

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

story_items = {}

skills: {
    'espionage': ['follow', 'record', 'plant'],
    'technology': ['decrypt', 'encrypt', 'storage'],
    'combat': ['hand_to_hand', 'firearm']
}

#Classes
class Location_Input():
    """Will take arguments from location function and return changed values"""

    hours = 25
    choice = ""
    stars = 0

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
    
    while open_package not in ['yes','no']:
        open_package = input("please choose if you would like to open the box. Answer with 'yes' or 'no'.")
    if open_package == 'yes':
        print(package)
    elif open_package == 'no':
        print("The package will be safely dealt with.")
        
def commands(command):
    """Function for receiving commands"""

    print("You have received a letter from HQ.")
    
    for items in command:
        print(items)

def park(stars):
    """Park location in Hagenstade"""

    time = 10.0
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
    print("If you don't have any time to explore any other areas, but still have a little remaining, feel free to walk around the center for the remainder.")
    print("The center will not give any main story elements, but may offer a chance to gain new tools and skills.")

    section = input("With all that said and done, which area would you like to explore first? ").lower()

    while section not in ["west" , "east" , "north" , "south" , "center"]:
        section = input("Choose one of the cardinal directions + the center where each thing is located. ").lower()
    
    while time > 0:

        while section in chosen:
                section = input(f"You have already chosen to go {section}. Please choose another section. ").lower()

        if section == 'north':
            
            chosen.append("north")

            print("The rocket looks very imposing as you approach. It is at least 50 meters tall, angled towards the sea.")
            print("It has a big black ribbed mount with a diameter of at least 3 meters.")
            print('A lone plaque behind the rocket reads, "Markareshi III Rocket. First rocket in failed nuclear weapons program."')
            
            rusure = input("There isn't much to see here. Do you still want to explore the area? ").lower()

            while rusure not in ["yes","no"]:
                rusure = input("Please state a yes or no answer. ")

            if rusure == "no":
                time -= 0.5
                print(f"You have {time} hours left.")
                section = input("Which area would you like to explore next? ").lower()
                continue
            
            if rusure == "yes" and time >= 0.5:
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

                while going_up not in ["yes","no"]:
                    going_up = input("No time to spare. The rocket looms overhead. Do you climb it? ")
                
                if going_up == "no":
                    print(f"you have {time} hours left.")
                    section = input("Which area would you like to explore next? ").lower()
                    continue
                
                if going_up == "yes" and time >= 5.5:
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
                    stars += 1
                    
                    time_removed = base(time)
                    time -= time_removed
                    time -= 5.5
                    
                    print("...The bathroom.")
                    print("This must be the unknown building on the south side. Go figure.")

                    chosen.append("south")
                
                    print(f"you have {time} hours left.")
                    section = input("Which area would you like to explore next? ").lower()
                    continue
            
            else:
                print("You do not have enough time to explore this area. Please choose a different section")
                section = input("Which area would you like to explore next? ").lower()
                continue

        if section == "south":
            
            chosen.append("south")
            
            print("The building seems rather small as you approach")
            print("It has no windows and has a single door on the side.")
            print("You have no idea what's in the building should you go in.")

            going_in = input("Do you enter the building? ").lower()

            while going_in not in ["yes","no"]:
                going_in = input("Are you going into the building or not? ")

            if going_in == "no":
                time -= 0.5
                print(f"You have {time} hours left.")
                section = input("Which area would you like to explore next? ").lower()
                continue
            
            if going_in == "yes" and time >= 0.5:
                time -= 0.5
                print("You enter the building and look around.")
                print("It seems to be an abandoned bathroom. Everything looks dirty and broken.")
                print("You look around, peeking in each stall. One of them still had some human excrement that who knows how long was there.")
                print("Behind the last stall, there is a door. You're not sure what's behind it. Or who.")

                entering = input("Do you go in? ").lower()

                while entering not in ["yes","no"]:
                    entering = input("Do you enter or do you not? ").lower()
                
                if entering == "no":
                    print(f"you have {time} hours left.")
                    section = input("Which area would you like to explore next? ").lower()
                    continue
                
                if entering == "yes" and time >= 5.5:
                    stars += 1

                    time_removed = base(time)
                    time -= time_removed
                    time -= 5.5

                    print("...The rocket.")
                    print("Who knew the rocket would hold a secret exit. Go figure.")

                    chosen.append("north")

                    print(f"you have {time} hours left.")
                    section = input("Which area would you like to explore next? ").lower()
                    continue
                
            else:
                print("You do not have enough time to explore this area. Please choose a different section")
                section = input("Which area would you like to explore next? ").lower()
                continue

        if section == "west":

            chosen.append("west")

            print("Although the Translutian people hate any association with American culture, they do agree that the sport of basketball is not so bad.")
            print("Translutia is home to some of the greatest basketball players of all time, and the people here take the sport very seriously.")
            print("To that extent, basketball is labelled as the official sport of the country, making it very odd why no one is playing right now.")
            print("I would proceed with caution. A lack of populous is generally not a good sign, especially for a scout such as yourself.")
            print("The basketball court looks very derelict and abandoned. The court has cracks running through it with weeds covering the court.")
            print("The lines are barely visible and the hoops are broken and lopsided.")
            print("Still, there is a half-deflated ball lying in the field next to the court.")
            print("Maybe something will happen later...")

            playing = input("Do you want to wait for something to happen or move on? ").lower()

            while playing not in ["wait","move on"]:
                print("I suppose you're going to wait then.")
                playing = input("If not, please decide if you are going to wait or move on.").lower()
            
            if playing == "move on":
                time -= 0.5
                print(f"You have {time} hours left.")
                section = input("Which area would you like to explore next? ").lower()
                continue
            
            if playing == "wait" and time >= 1.5:
                time -= 1.5
                print("You wait for an hour and a half, and nothing happens.")
                print("Just as you start to leave a loud noise comes around the block. It seems to be a car.")
                print("It approaches and parks at the parking lot. Five guys exit the car and start walking towards the court. One has a basketball in hand.")
                print("The first one stops, then points at you. Everyone else stops as well. Maybe he is the leader. He seems confused.")
                print("Fortunately, your training in acting the part and disguise will help you in this situation.")
                print('"Hello friends!" you say. "Im afraid that Im lost. I am a tourist here from the nearby Poldrack Islands."')
                print('"What are you doing here?" one asks.')
                print('"Im trying to learn more about our neighboring countries. I thought I would visit Translutia myself and experience the culture.')
                print('"I dont know, sir." the leader says. "I dont remember learning about the Poldrack Islands."')
                print("Silently, you curse at yourself. But you have handled these stressful situations before.")
                print('"Listen," you say. "Your leader Rotendero has invited a representative of my country to visit for a formal dinner gathering."')
                print('"I need help finding where we might meet," you continue.')
                print('"Why should we help you?" he asks.')
                print('"You dont want to help a big ambassador from a foreign nation?"')
                print('"Tell you what." the leader says. "I challenge you to a pickup game of basketball. If you win, we will help you. If not, we will report you."')
                print('"And why would I agree to that?" you respond.')
                print('"Because if not, the authorities will put you in prison, which is famously lethal."')

                do_you_play = input("Do you play with the group or run away and risk capture? ").lower()

                while do_you_play not in ["play","run away"]:
                    do_you_play = input("They are closing in. You need to make a decision and fast. ").lower()

                if do_you_play == "run away":
                    
                    time = run_away(time)

                if do_you_play == "play" and time >= 2.0:
                    print('"Wait," you say aloud. "Ill play."')
                    print("The leader smiles. He gestures to the court. You walk onto the court, and see the team of five facing you.")
                    print('"What is this, a 1 v 5?" you ask. The leader only smiles.')
                    print('"You get ball first," he said. "First to sink three shots wins." He throws the ball at you, which you awkwardly catch.')
                    print("You start dribbling the ball. Two of the guys rush at you, you dodge them both and run right at the basket.")
                    print("Just as you were about to throw the ball in, the ball is stolen from your hand. The leader smirks as he runs to the other end and makes the shot.")
                    print('"Thats 1 - 0," he said.')
                    print('"Thats a foul," you replied. Theres just no winning with these guys. It seems playing dirty is the name of the game.')
                    print("You start the second round with a burst of energy. You round around three guys before one of them jumps on your back and drags you back.")
                    print('The leader grabs the ball and scores another point. "One more and we win," he grinned.')
                    print("You know you need a new strategy.")

                    what_strategy = input("Should you try and make a two-point shot or should you make a slam dunk? ").lower()

                    while what_strategy not in ["two-point shot","slam dunk"]:
                        what_strategy = input("You need a plan of action. Make sure you're writing the hyphen between two and point. ").lower()

                    if what_strategy == "slam dunk":
                        print("You grab the ball, and begin the round. You dribble around two guys and reach the box.")
                        print("You jump up, arcing your hand and the ball into the basket, when a big shove from the side throws you off balance.")
                        print("You collapse to the floor as the leader dribbles the ball and scores for the third time.")
                        print('"Thats a foul. Its my free throws now," you yell angrily.')
                        print('The leader laughs. "Well, since you didnt win, I guess that means the authorities are getting a new inmate."')
                        print('"I dont think so," you respond.')

                        time = run_away(time)
                    
                    if what_strategy == "two-point shot":
                        print("You begin the round. Three guys close in. You dodge the first two, and shoot the ball before the third reaches you.")
                        print("The ball arcs over the players, and sinks right into the basket.")
                        print('"2 - 2," you smile. You scoring has given you a massive boost of confidence.')
                        print("The leader starts the round, and tries to fake a pass. You, being an intelligent agent, you see the deception, and snag the ball.")
                        print("You run up to the opposition basket and make the shot. Everyone watches with bated breath as the ball bounces once, twice, and ...")
                        print("")
                        print("...sinks into the basket")
                        print("")
                        print("You smile and look at the leader. He is furious. The rest of the group is livid too.")
                        print('"You owe me some information, man. That will help me most,"you say.')
                        print('"What do you want to know," the leader says begrudgingly. You appreciate that he sticks to his word.')
                        print('"Any information on the parade would be nice," you say.')
                        print('"Information how?"')
                        print('"I want to know if there is anything strange going on with the parade tomorrow. I dont want the celebrations to be cut short early."')
                        print('"I dont follow."')
                        print('"Tell me what you know kid. I know youre hiding something."')
                        print('He sighs. "Fine, all I know is that a secret organization calling themselves The Agenda is planning on setting a trap for some supposed American spies."')
                        print('"Where?"')
                        print('"In front of the national bank. You cant miss it."')
                        print('"Youve been of great assistance," you say. You watch as the group walk back to their car and drive away.')
                        print("You've just gained some very valuable information that may just save this mission.")

                        time -= 2

                        print(f"You have {time} hours left.")
                        section = input("Which area would you like to explore next? ").lower()
                        continue

            else:
                print("You do not have enough time to explore this area. Please choose a different section")
                section = input("Which area would you like to explore next? ").lower()
                continue
        
        if section == "east":

            chosen.append("east")

            print("The dried fountain lies to the left. The gardens are on the right.")

            which_side = input("Which side do you go to? ").lower()

            while which_side not in ["fountain","gardens","left","right"]:
                which_side = input(f"{which_side} is not found on the east side.").lower()
            
            if which_side == "gardens" or which_side == "right":
                print("The garden seems gray and wilted as you enter through the hedges.")
                print("It is evident that no one has been here to maintain the gardens in a very long time.")
                print("Suddenly, you spot a bag hidden in one of the hedges. When you reach out to grab it, a laser starts scanning your arm.")
                print("Startled, you jump back. You take a closer look and see a whole network of lasers, cameras, and microphones.")
                print("The bag, however, is beckoning for it to be opened and exhumed.")

                grab_bag = input("Do you grab the bag, or leave it alone? ").lower()

                while grab_bag not in ["grab the bag", "leave it alone"]:
                    grab_bag = input("The bag still beckons. Do you grab the bag or leave it alone? ").lower()
                
                if grab_bag == "grab the bag":
                    print("Your hand darts into the hedges, and you snatch the bag.")
                    print("The lasers seem to capture the contours of your arm. Oh well, you can't dwell on it.")
                    print("You open the bag, and out falls three pieces of paper. They are all grids with varying numbers and letters.")
                    print("A loud bang is heard, and the hedges begin to move and shift. The entrance closes behind you.")
                    print("You move into the new area and find two paths. One on the left and one on the right.")

                    which_path = input("Which path do you take? ").lower()
                    
                    while which_path not in ["left","right"]:
                        which_path = input("You can't go straight. Choose right or left. ").lower()
                    
                    if which_path == "left":
                        decoder = 'garden_1'
                    
                    if which_path == "right":
                        decoder = 'garden_2'
                    
                    door_unlocking(decoder)

                    while True:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                sys.exit()
                            else:
                                break
                
            if which_side == "fountain" or which_side == "left":
                print("The dried fountain has stains of green and black. Leaves are scattered in the basin.")
                print("It is clear no one has taken care of the fountain in years.")

                decoder = 'statue_1'

                door_unlocking(decoder)

                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            sys.exit()
                        else:
                            break

        if section == "central":
            print(chosen)

    if time <= 0:
        print("You have ran out of time for today. You must return to the hotel immediately.")
        print(f"Good night agent. Your next instructions will be sent tomorrow morning.")
         
def base(time):
    """Extension to park() function"""

    time = 0
    
    print("You enter into a dimly-lit chamber.")
    print("You quickly move to the side of the wall. You put the binoculars to your eyes and turn on night-vision.")
    print("You seem to be in a small storage room. On the wall lay a crowbar and a hammer.")
    print("A table by the corner contains some rounds of ammunition and some newspapers in a foreign language.")
    print("A flashlight and a matchbox lie on the floor next to a broken tool box containing some nails and screws, and a screwdriver.")
    print("There is a mop and a janitorial outfit to the side. Next to it is a small backpack, which is empty.")
    print("On the far wall is a door. You peek out the door and see empty hallways with flickering lights.")
    print("Just as you are about to go out for a better look, you hear some voices of people speaking.")
    print("You crouch in the shadows and watch as two suited men walk past the closet and around a corner.")
    print("If you go out there like this and get caught, it will surely mean trouble. Maybe something in the room can help you...")
    print("You immediately go to the janitor's outfit and put it on. Blending in is better than sneaking around.")
    print("You pick up the backpack. There's enough room in there for one item you saw above.")

    grabbed_item = input("Which item do you pick up and put in your bag? ").lower()

    while grabbed_item not in ["matches,", "flashlight", "crowbar", "hammer","ammunition","newspapers","nails and screws","screwdriver"]:
        print("You didn't see that object in the room.")
        grabbed_item = input("Choose an object you did see before. ").lower()
    
    if grabbed_item == "crowbar":
        story_items["crowbar"] = 1
    elif grabbed_item == "matches":
        story_items["matches"] = 5
    elif grabbed_item == "flashlight":
        story_items["flashlight"] = 1
    elif grabbed_item == "hammer":
        story_items["hammer"] = 1
    elif grabbed_item == "ammunition":
        story_items["ammunition"] = 3
    elif grabbed_item == "newspapers":
        story_items["newspapers"] = 2
    elif grabbed_item == "nails and screws":
        story_items["nails"] = 4
        story_items["screws"] = 5
    elif grabbed_item == "screwdriver":
        story_items["screwdriver"] = 1
    
    print(f"You place the bag and your {grabbed_item} in the janitor's cart and you walk out of the closet all dressed up.")
    print("You place a bug in your pocket and set it to record. You can send any of the dialogue to the Egg for further analysis.")
    print("You walk down the hallway and turn at the corner the two men turned at.")
    print("There is one big door in front of you. You quietly enter the room.")
    print("The room is bright white with crates and boxes lining the edges of the walls. In the middle, the two suited men are talking with another man.")
    print("The man wore dark glasses and had a headset on. He nodded to the other men, then turned and walked into a back room.")
    print("The two other men then grab a box from the side, and empty it out.")
    print("They sort through the objects before finding something, which they quickly pocketed.")
    print("They then both followed the man into the back room.")
    print("You quickly go up to the emptied box and inspect the contents.")
    print("Old newspapers and crumpled papers seem to be the only things there.")

    inspect_further = input("Do you wish to inspect the contents further? ").lower()
    
    if inspect_further == "yes":
        time += 1.0
        print("You inspected the papers further, but you could not find anything else of importance.")
    
    print("You enter the back room, which was much more dimly lit, and hide behind a trash can.")
    print("The men are talking to a woman now. She had a very harsh tone and paced around the men. She seemed to be a general of sorts.")
    print('Suddenly, you hear "General, the strike team is in position."')
    print("You gasp, surprised at the sound of English in a country that hates any languages apart from its own.")
    print("The two men and the woman whip around to your location. You know you've been caught.")
    
    what_now = input("Do you run, or give up? ").lower()

    while what_now not in ["run","give up"]:
        what_now = input("You can't dwell on this, they're approaching the can!")
    
    if what_now == "give up":
        print("You can't give up. Giving up means mission failure. Run!")

    print("You run out of the door, the two men chasing you.")
    print("One of them grabs the backpack, but you manage to yank it back in your direction.")
    print("You keep running. You run to the door to the rocket.")
    print("IT'S LOCKED!!!")
    print("You keep running, turning left and right at each corner.")
    print("The sound of running boots fade behind you. You lost them.")
    print("You open the door next to you, and close it.")
    print("This new room has nothing special, except for a handgun on the side.")
    print("On the other side of the room you see...")
    print("")
    print("SUNLIGHT!!!")
    print("")
    print("There is a door with a window looking out. You exit the door and find yourself in...") 
    
    return time

def run_away(time):
    """Park function west section running away result"""

    print("You ditch the group and run away from the west end. They're chasing after you.")
    print("The group splits up. One goes south, one goes north, and the other three follow you to the center circle.")
    print("Being a little older than the group, they are quickly gaining ground.")
    print("You know you have some tools at your disposal in addition to your martial arts background.")
    print("You can't overpower them with combat alone. You'll need a tool to ward them off.")
    print("With you, you brought:")
    print("")

    for keys in tools:
        print(f" - {keys}")
    
    print("")

    which_tool = input("Which tool are you going to use? ").lower()

    while which_tool not in tools:
        which_tool = input("Without tools, you will surely be captured. Pick one to use. ").lower()
    
    if which_tool == "phone":
        print("You press the self-destruct button and count to two.")
        print("Then, you quickly throw it behind you.")
        print("A large and loud explosion sounds behind you and you are thrown forward.")
        print("You turn around and see...well, better not look too long. You keep running forward and exit out of the park.")
        print("You have some Translutian blood on your hands now. This was not how the mission was meant to go down.")

        del tools["phone"]

        time = 0

        return time
    
    print(f"You pull out the {which_tool} from your backpack.")
    print("You stop, turn around, and throw it at the closest person.")
    print(f"The {which_tool} hits him square on the nose and he collapses to the floor.")
    print("You keep running toward the exit. One stays behind to tend to their friend. The leader chases you down.")
    print("Just as you exit the center oval, a hand grabs the back of your collar. Instinctively, you spin around and push the leader away.")
    print("The leader retaliates with a punch to the gut.") 
    print("As you're wheezing from the blow, you see the two guys who split up to the north and south of the park running back. Its now or never.")
    print("You pick yourself up and perform a vicious uppercut to the leader's jaw. You follow up with an elbow hit to the chest.")
    print("The leader goes down like a sack of potatoes. You run the remaining few paces out of the exit.")
    print("The mission needed to be smoother. You're going to have to do better next time.")

    del tools[which_tool]
    
    time = 0

    return time

def door_unlocking(code):
    """'Function that unlocks doors'"""

    pygame.init()

    font = pygame.font.SysFont("Courier New", 100)
    
    print("You are approaching a panel.")

    if code == "garden_1":

        screen = pygame.display.set_mode( (525, 500) ) 

        textL = font.render("L T X G", True, (225, 225, 225))
        textS = font.render("S D P R", True, (225, 225, 225))
        textM = font.render("M F E A", True, (225, 225, 225))
        textU = font.render("U J Q K", True, (225, 225, 225))
        xpos = 50
        ypos = 50

        print("It is partially hidden away in the bushes. It was a stroke of luck that you were able to spot it.") 
        print("There is a big rhombus on the plaque. It has an arrow on the right side.")
        print("There is a 4x4 keypad on the side with various letters. There is no clear pattern to it.")
        print("Maybe the decoder will help...")
        
        screen.blit(textL, (xpos, ypos))
        ypos += 100
        screen.blit(textS, (xpos, ypos))
        ypos += 100
        screen.blit(textM, (xpos, ypos))
        ypos += 100
        screen.blit(textU, (xpos, ypos))
        pygame.display.flip()

        rhombus = input("What is the code to open the box? ").upper()

        if rhombus == "RAQJMSTX":
            print("The box clicks open!")
        
    elif code == 'garden_2':

        screen = pygame.display.set_mode( (400, 400) )

        text8 = font.render(str("8 9 1"), True, (225, 225, 225))
        text3 = font.render(str("3 6 7"), True, (225, 225, 225))
        text2 = font.render(str("2 4 5"), True, (225, 225, 225))
        xpos = 50
        ypos = 50

        print("The panel is right at your feet. A big circle is imprinted in the center. There is downward arrow on the left endpoint.")
        print("There is a 3x3 keypad with digits 1-9. There is no clear pattern.")
        print("maybe the decoder will help.")

        screen.blit(text8, (xpos, ypos))
        ypos += 100
        screen.blit(text3, (xpos, ypos))
        ypos += 100
        screen.blit(text2, (xpos, ypos))
        pygame.display.flip()

        circle = input("What is the code to open the box? ").lower()
        
        if circle == "32457198":
            print("The box clicks open!")

    elif code == 'statue_1':
       
        screen = pygame.display.set_mode( (650, 650) )
       
        text_1 = font.render("~ - ~ - ~", True, (225, 225, 225))
        text_2 = font.render("[ + = - ]", True, (225, 225, 225))
        text_3 = font.render("< ( * ) >", True, (225, 225, 225))
        text_4 = font.render("! $ ^ & ?", True, (225, 225, 225))
        text_5 = font.render("_ | _ | _", True, (225, 225, 225))
        xpos = 50
        ypos = 50

        print("The panel is hidden at the base of the fountain. It has the shape of an X inscribed onto it.")
        print("There is an arrow at the top right and bottom right of the X going towards the center. A small 1 is next to the top right arrow.")
        print("There is a 5x5 keypad with radom symbols next to the plaque.")
        print("Maybe the decoder will help...")

        screen.blit(text_1, (xpos, ypos))
        ypos += 100
        screen.blit(text_2, (xpos, ypos))
        ypos += 100
        screen.blit(text_3, (xpos, ypos))
        ypos += 100
        screen.blit(text_4, (xpos, ypos))
        ypos += 100
        screen.blit(text_5, (xpos, ypos))
        pygame.display.flip()

        x_symbol = input("What is the correct code to open the box? ").lower()

        if x_symbol == "~-*$__&*+~":
            print("The box clicks open!")

    else:
        print("You do not have the correct decoder to try this door. Find the encryption and try again.")

def Hagenstade(hour_star_input):
    """Sequence for player"""

    if hour_star_input.hours == 25:
        print(f"The parade will go on tomorrow, and begins at 09:00. The time right now is 08:00. That leaves you with {hour_star_input.hours} hours.")
        print("Until then, explore the area, collect intel, and gain skills and tools to help you in Translutia.")
        print("While you do explore Hagenstade, be wary of the curfew, which is at 20:00 sharp. Anyone not in their house by curfew will be arrested.")
        print("We have received reports that the park in Hagenstade has had some recent activity worth investigating.")
        print("We don't need to remind you that arrest or capture is not an option.")
        print("Your capture puts the whole operation at risk. The GSS trusts you to make the right decisions. Other than that, your time is yours.")

        hour_star_input.choice = input("Please input 'park' to begin the game. ").lower()

        while hour_star_input.choice not in ["park", "port", "bank", "nationalbank"]:
            hour_star_input.choice = input("Please input 'park'. You only have a limited time to explore. ").lower()

        locations(hour_star_input)


def locations(hour_star_choice_input):
    """To be used with Hagenstade function for ease of use"""

    if hour_star_choice_input.choice == "park":
        hour_star_choice_input.hours -= 24
        hour_star_choice_input.stars = park(hour_star_choice_input.stars)
        

def main():
    """Introductory Procedure"""

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
        f"    The senior team has already arrived and is getting ready. The parade will begin tomorrow.",
        f"    We will be sending you some packages as well. These packages contain valuable tools and information.",
        f"    However, we urge you to be wary. The dictator most surely knows you are in the country, and they will be trying to put a stop to the mission.",
        f"    Be suspicious of everything. You will know something is ours if we mention it beforehand, or a decrypted message reads GSS.",
        f"    Good luck agent. Godspeed."
        ]

    commands(command_1)

    main_inputs = Location_Input()

    Hagenstade(main_inputs)

if __name__ == "__main__":
    main()

