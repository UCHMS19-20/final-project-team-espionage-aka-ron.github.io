#Plan: Create a Code Name Function that takes an input and returns a code name.

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
        'u': "uncinia", 
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

    
    print("So you're from the Western district? I had a brother live there a few years ago. We have a few westerners here at base. You'll fit right in.")
    original_name = input("Before you head inside, chief is going to need your name: ")
    first_letter = original_name[0]
    last_letter = original_name[-1]
    
    if first_letter not in original_name:
        print("I don't have all day. Either give me your name or get out.")
    
   
    
    code = first_word[first_letter] + " " + second_word[last_letter]  
    
    print("Now just to give you a code name. We can't risk any foreign interceptions revealing your assignment.")
    print(f"Looks like your name was chosen. From now on, you will be known as {code} or {first_letter.upper()}{last_letter.upper()} for short.")

while True:
    code_name()
