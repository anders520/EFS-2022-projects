#Dawson Harris & Anders Choy

'''Missionaries_Array_VIS_FOR_TK.py
Version of Aug. 29, 2018. Works with the formulation of
Missionaries and Cannibals that uses a State class for
representing states.

'''

from show_state_array import initialize_tk, state_array, state_display, STATE_WINDOW, test

from tkinter import font

myFont=None

WIDTH = 200
HEIGHT = 750
TITLE = 'Instant Insanity'

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
    red = (255, 50, 0)
    green = (60, 180, 115)
    blue = (80,80,255)
    yellow = (255, 255, 122)
    white = (255, 255, 255)
    
    row = [white]*4
    the_color_array = [row]
    for i in range(14):
        the_color_array.append(row[:])
    # Now create the default array of string labels.
    row = ['' for i in range(4)]
    the_string_array = [row]
    for j in range(14):
        the_string_array.append(row[:])

    # Adjust colors and strings to match the state.
    for j in range(4):
        if j == 0: cube_list = s.first_cube_list
        elif j == 1: cube_list = s.second_cube_list
        elif j == 2: cube_list = s.third_cube_list
        elif j == 3: cube_list = s.fourth_cube_list
        for i in range(6):
            c = cube_list[i]
            if c == 0: color = red
            elif c == 1: color = green
            elif c == 2: color= blue
            elif c == 3: color = yellow
            if i <= 3:
                the_color_array[j * 4 + 1][i] = color
            elif i == 4:
                the_color_array[j * 4][1] = color
            elif i == 5:
                the_color_array[j * 4 + 2][1] = color

    caption="Current state of the puzzle. Textual version: "+str(s)        
    the_state_array = state_array(color_array=the_color_array,
                                  string_array=the_string_array,
                                  text_font=myFont,
                                  caption=caption)
    #print("the_state_array is: "+str(the_state_array))
    the_state_array.show()

    
    

    
