#Dawson Harris & Anders Choy

'''FishFrenzy_Array_VIS_FOR_TK.py
Version of Sep. 13, 2022.
'''

from show_state_array import initialize_tk, state_array, state_display, STATE_WINDOW, test

from tkinter import font

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


    #Bar Variables
    salmonBars = int(s.fishList[0].number / 1000)
    tunaBars = int(s.fishList[1].number / 1000)
    bassBars = int(s.fishList[2].number / 1000)
    halibutBars = int(s.fishList[3].number / 1000)
    pompanoBars = int(s.fishList[4].number / 1000)
    codBars = int(s.fishList[5].number / 1000)


    # Adjust colors and strings to match the state.
    for i in range(salmonBars):
        the_color_array[9 - i][0] = salmonColor

    for i in range(tunaBars):
        the_color_array[9 - i][1] = tunaColor

    for i in range(bassBars):
        the_color_array[9 - i][2] = bassColor

    for i in range(halibutBars):
        the_color_array[9 - i][3] = halibutColor

    for i in range(pompanoBars):
        the_color_array[9 - i][4] = pompanoColor

    for i in range(codBars):
        the_color_array[9 - i][5] = codColor
        

    '''for j in range(6):
        if j == 0: cube_list = s.fishList[0].number
        elif j == 1: cube_list = s.fishList[1].number
        elif j == 2: cube_list = s.fishList[2].number
        elif j == 3: cube_list = s.fishList[3].number
        elif j == 4: cube_list = s.fishList[4].number
        elif j == 5: cube_list = s.fishList[5].number
        for i in range(6):
            c = cube_list[i]
            if c == 0: color = salmonColor
            elif c == 1: color = tunaColor
            elif c == 2: color = bassColor
            elif c == 3: color = halibutColor
            if i <= 3:
                the_color_array[j * 4 + 1][i] = color
            elif i == 4:
                the_color_array[j * 4][1] = color
            elif i == 5:
                the_color_array[j * 4 + 2][1] = color'''

    caption="Current state of the puzzle. Textual version: "+str(s)        
    the_state_array = state_array(color_array=the_color_array,
                                  string_array=the_string_array,
                                  text_font=myFont,
                                  caption=caption)
    #print("the_state_array is: "+str(the_state_array))
    the_state_array.show()

    
    

    
