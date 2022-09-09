'''Missionaries3_VIS_FOR_TK3.py
Version of Sept. 17, 2019.
This visualization file works with Missionaries3.py and
Tk_SOLUZION_Client3.py.
It uses three jpg images for showing missionaries, cannibals, and the boat.

'''
from tkinter import font

myFont=None

WIDTH = 400
HEIGHT = 300
TITLE = 'The Missionaries and Cannibals Puzzle'

STATE_WINDOW = None
STATE_ARRAY = None

def initialize_vis(st_win, state_arr, initial_state):
  global STATE_WINDOW, STATE_ARRAY
  STATE_WINDOW = st_win
  STATE_ARRAY = state_arr
  STATE_WINDOW.winfo_toplevel().title(TITLE)
  render_state(initial_state)
  
def render_state(s):
    # Note that font creation is only allowed after the Tk root has been
    # defined.  So we check here if the font creation is still needed,
    # and we do it (the first time this method is called).
    global myFont
    if not myFont:
        myFont = font.Font(family="Helvetica", size=18, weight="bold")
    #print("In render_state, state is "+str(s))
    # Create the default array of colors
    tan = (200,190,128)
    blue = (100,100,255)
    brown = (100, 80, 0)
    purple = (128, 0, 192)
    cyan = (100, 200, 200)
    
    row = [tan]*3 + [blue]*2 + [tan]*3
    the_color_array = [row, row[:]]
    # Now create the default array of string labels.
    row = ['' for i in range(8)]
    the_string_array = [row, row[:]]

    # Adjust colors and strings to match the state.
    mright = s.n_missionaries_on_right
    mleft = 3 - mright
    for i in range(mleft):
        #the_color_array[0][i]=purple
        the_color_array[0][i]="missionary.jpg"
        the_string_array[0][i]='M'
    for i in range(mright):
        #the_color_array[0][i+5]=purple
        the_color_array[0][i+5]="missionary.jpg"
        the_string_array[0][i+5]='M'
    cright = s.n_cannibals_on_right
    cleft = 3 - cright
    for i in range(cleft):
        #the_color_array[1][i]=cyan
        the_color_array[1][i]="cannibal.jpg"
        the_string_array[1][i]='C'
    for i in range(cright):
        #the_color_array[1][i+5]=cyan
        the_color_array[1][i+5]="cannibal.jpg"
        the_string_array[1][i+5]='C'
    if s.n_boats_on_right==0:
        #the_color_array[1][3]=brown
        the_color_array[1][3]="boat.jpg"
        the_string_array[1][3]='B'
    else:
        #the_color_array[1][4]=brown
        the_color_array[1][4]="boat.jpg"
        the_string_array[1][4]='B'

    caption="Current state of the puzzle. Textual version: "+str(s)
    print(caption)
    the_state_array = STATE_ARRAY(color_array=the_color_array,
                                  string_array=the_string_array,
                                  text_font=myFont,
                                  caption=caption)
    #print("the_state_array is: "+str(the_state_array))
    the_state_array.show()

print("The Missionaries VIS file has been imported.")
    

    
