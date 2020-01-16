import pygame
import sys

pygame.init()

screen = pygame.display.set_mode( (1000, 1000) )

font = pygame.font.Font("CourierM.ttf", 250)
text = font.render("Letters", True, (200, 200, 200))
xpos = 50
ypos = 50

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
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            screen.blit(text, (xpos, ypos))
            pygame.display.flip()
    elif check_code == 'compound2':
        hrkjh
    elif check_code == 'compound3':
        hkjg
    else:
        print("You do not have the correct decoder to try this door. Find the encryption and try again.")

door_unlocking()