#Dawson Harris & Anders Choy

'''Missionaries_Array_VIS_FOR_TK.py
Version of Aug. 29, 2018. Works with the formulation of
Missionaries and Cannibals that uses a State class for
representing states.

'''

from show_state_array import initialize_tk, state_array, state_display, STATE_WINDOW, test

from tkinter import font

myFont=None

WIDTH = 400
HEIGHT = 200
TITLE = 'The Farmer, the Fox, the Chicken, and the Grain Puzzle'

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
    tan = (200,190,128)
    blue = (100,100,255)
    brown = (100, 80, 0)
    purple = (128, 0, 192)
    cyan = (100, 200, 200)
    green = (31, 191, 45)
    orange = (218, 144, 13)
    
    row = [tan] + [blue]*2+ [tan]
    the_color_array = [row, row[:], row[:], row[:],]
    # Now create the default array of string labels.
    row = ['' for i in range(8)]
    the_string_array = [row, row[:], row[:], row[:]]

    # Adjust colors and strings to match the state.
    frmrRight = s.farmerLocation
    frmrLeft = 1 - frmrRight
    for i in range(frmrLeft):
        the_color_array[0][i]=purple
        the_string_array[0][i]='Farmer'
    for i in range(frmrRight):
        the_color_array[0][i+3]=purple
        the_string_array[0][i+3]='Farmer'
    foxRight = s.foxLocation
    foxLeft = 1 - foxRight
    for i in range(foxLeft):
        the_color_array[1][i]=cyan
        the_string_array[1][i]='Fox'
    for i in range(foxRight):
        the_color_array[1][i+3]=cyan
        the_string_array[1][i+3]='Fox'
    cRight = s.chickenLocation
    cLeft = 1 - cRight
    for i in range(cLeft):
        the_color_array[2][i]=green
        the_string_array[2][i]='Chicken'
    for i in range(cRight):
        the_color_array[2][i+3]=green
        the_string_array[2][i+3]='Chicken'
    gRight = s.grainLocation
    gLeft = 1 - gRight
    for i in range(gLeft):
        the_color_array[3][i]=orange
        the_string_array[3][i]='Grain'
    for i in range(gRight):
        the_color_array[3][i+3]=orange
        the_string_array[3][i+3]='Grain'
    if s.boatLocation==0:
        the_color_array[0][1]=brown
        the_string_array[0][1]='Boat'
    else:
        the_color_array[0][2]=brown
        the_string_array[0][2]='Boat'

    caption="Current state of the puzzle. Textual version: "+str(s)        
    the_state_array = state_array(color_array=the_color_array,
                                  string_array=the_string_array,
                                  text_font=myFont,
                                  caption=caption)
    #print("the_state_array is: "+str(the_state_array))
    the_state_array.show()
