
'''FishFrenzy_VIS_FOR_TK3.py
Version of Sept. 15, 2022.
'''
from tkinter import font
from PIL import Image, ImageTk
import winsound

myFont=None

WIDTH = 590
HEIGHT = 520
TITLE = 'Fishing Frenzy'

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
        myFont = font.Font(family="Helvetic", size=10, weight="bold")
    print("In render_state, state is "+str(s))
    # Create the default array of colors
    white = (255, 255, 255)
    salmonColor = (218, 144, 13)
    tunaColor = (143, 1, 27)
    bassColor = (128,128,0)
    halibutColor = (184, 115, 51)
    pompanoColor = (255, 243, 128)
    codColor = (170, 255, 0)
    blue = (25, 25, 112)

    row = ["ocean2.jpg"]*7
    the_color_array = [row]
    for i in range(10):
        the_color_array.append(row[:])
    # Now create the default array of string labels.
    row = ['' for i in range(7)]
    the_string_array = [row]
    for j in range(10):
        the_string_array.append(row[:])

    # Adjust colors and strings to match the state.
    j = 0
    fishTotal = 0
    for fish in s.fishList:
        fishBars = int(fish.number / 1000)
        fishTotal += fish.number
        colorList = ["salmon.jpg", "tuna.jpg", "cod.jpg", "pompano.jpg", "stripedBass.jpg", "halibut.jpg"]
        for i in range(fishBars):
            the_color_array[9 - i][j + 1] = colorList[j]
        j+=1
    #Vertical colors for margins
    the_color_array[0][0] = blue
    the_color_array[1][0] = blue
    the_color_array[2][0] = blue
    the_color_array[3][0] = blue
    the_color_array[4][0] = blue
    the_color_array[5][0] = blue
    the_color_array[6][0] = blue
    the_color_array[7][0] = blue
    the_color_array[8][0] = blue
    the_color_array[9][0] = blue
    the_color_array[10][0] = "WARMD_Logo.jpg"

    #Lables for the table to help the player know how many fish there are
    the_string_array[0][0] = '10,000'
    the_string_array[1][0] = '9,000'
    the_string_array[2][0] = '8,000'
    the_string_array[3][0] = '7,000'
    the_string_array[4][0] = '6,000'
    the_string_array[5][0] = '5,000'
    the_string_array[6][0] = '4,000'
    the_string_array[7][0] = '3,000'
    the_string_array[8][0] = '2,000'
    the_string_array[9][0] = '1,000'

    #Horizontal colors for margins
    the_color_array[10][1] = blue
    the_color_array[10][2] = blue
    the_color_array[10][3] = blue
    the_color_array[10][4] = blue
    the_color_array[10][5] = blue
    the_color_array[10][6] = blue

    #Fish Names in boxes at bottom of grid
    the_string_array[10][1] = s.fishList[0].name +'\n' + str(s.fishList[0].number)
    the_string_array[10][2] = s.fishList[1].name +'\n' + str(s.fishList[1].number)
    the_string_array[10][3] = s.fishList[2].name +'\n' + str(s.fishList[2].number)
    the_string_array[10][4] = s.fishList[3].name +'\n' + str(s.fishList[3].number)
    the_string_array[10][5] = s.fishList[4].name +'\n' + str(s.fishList[4].number)
    the_string_array[10][6] = s.fishList[5].name +'\n' + str(s.fishList[5].number)
    
    
    #root = Label(STATE_WINDOW, text = "Username").place(x = 40, y = 60) 

    caption="Current state of the puzzle. Textual version: "+str(s)

    the_state_array = STATE_ARRAY(color_array=the_color_array,
                                  string_array=the_string_array,
                                  text_font=myFont,
                                  caption=caption)
    ico = Image.open("fishfrenzyLogo.ico")
    photo = ImageTk.PhotoImage(ico)
    STATE_WINDOW.winfo_toplevel().wm_iconphoto(False, photo)
    #print("the_state_array is: "+str(the_state_array))
    the_state_array.show()
    if fishTotal <= 0:
        winsound.PlaySound("explosin.wav",  winsound.SND_FILENAME)
    

print("The FishFrenzy VIS file has been imported.")
    

    