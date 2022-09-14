#Dawson H, Anders C, Ren C, Mason C, Will Z

'''FishFrenzy_Array_VIS_FOR_TK.py
Version of Sep. 13, 2022.
'''

from show_state_array import initialize_tk, state_array, state_display, STATE_WINDOW, test

from tkinter import font
from tkinter import *
from tkinter import ttk
import sys
myFont=None

WIDTH = 400
HEIGHT = 400
TITLE = 'FishFrenzy'

def initialize_vis():
  initialize_tk(WIDTH, HEIGHT, TITLE)
  
def render_state(s):
    # Note that font creation is only allowed after the Tk root has been
    # defined.  So we check here if the font creation is still needed,
    # and we do it (the first time this method is called).
    global myFont
    if not myFont:
        myFont = font.Font(family="Helvetica", size=18, weight="bold")
    print("In render_state, state is "+str(s))
    # Create the default array of colors
    white = (255, 255, 255)
    salmonColor = (218, 144, 13)
    tunaColor = (143, 1, 27)
    bassColor = (128,128,0)
    halibutColor = (184, 115, 51)
    pompanoColor = (255, 243, 128)
    codColor = (170, 255, 0)
    
    row = [white]*6
    the_color_array = [row]
    for i in range(9):
        the_color_array.append(row[:])
    # Now create the default array of string labels.
    row = ['' for i in range(6)]
    the_string_array = [row]
    for j in range(9):
        the_string_array.append(row[:])

    # Adjust colors and strings to match the state.
    j = 0
    fishTotal = 0
    for fish in s.fishList:
        fishBars = int(fish.number / 1000)
        fishTotal += fish.number
        colorList = [salmonColor, tunaColor, codColor, pompanoColor, bassColor, halibutColor]
        for i in range(fishBars):
            the_color_array[9 - i][j] = colorList[j]
        j+=1


    caption="Current state of the puzzle. Textual version: "+str(s)        
    the_state_array = state_array(color_array=the_color_array,
                                  string_array=the_string_array,
                                  text_font=myFont,
                                  caption=caption)
    #print("the_state_array is: "+str(the_state_array))
    the_state_array.show()
    #if fishTotal <= 0:
        #sys.exit()

    
    

    
