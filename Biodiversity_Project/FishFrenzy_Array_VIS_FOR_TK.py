#Dawson H, Anders C, Ren C, Mason C, Will Z

'''FishFrenzy_Array_VIS_FOR_TK.py
Version of Sep. 13, 2022.
'''

from ast import operator
from show_state_array import initialize_tk, state_array, state_display, STATE_WINDOW, test

from tkinter import font
from tkinter import *
from tkinter import ttk
import sys, importlib.util

try:
  spec = importlib.util.spec_from_file_location("FishFrenzy", "FishFrenzy"+".py")
  PROBLEM = spec.loader.load_module()
  spec.loader.exec_module(PROBLEM)
except Exception as e:
  print(e)
  exit(1)


myFont=None

WIDTH = 580
HEIGHT = 530
TITLE = 'Fishing Frenzy'


def initialize_vis():
  initialize_tk(WIDTH, HEIGHT, TITLE)
  
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
    

    row = [white]*7
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
        colorList = [salmonColor, tunaColor, codColor, pompanoColor, bassColor, halibutColor]
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
    the_color_array[10][0] = blue

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

    the_state_array = state_array(color_array=the_color_array,
                                  string_array=the_string_array,
                                  text_font=myFont,
                                  caption=caption)
    #print("the_state_array is: "+str(the_state_array))
    the_state_array.show()
