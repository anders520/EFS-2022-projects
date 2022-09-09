#!/usr/bin/python3
"""Tk_SOLUZION_Client3.py
    Works with the example files
       Missionaries3.py
         and
       Missionaries3_VIS_FOR_TK3.py.

Differences from Tk_SOLUZION_Client.py:

1. Allows putting image file names in the array of colors
  that was used in show_state_array.py, and attempts to
  show the image, loading it into Tkinter if it has not already been
  loaded and converted to a PhotoImage object.
  (So in each element of the array of colors, you can either have
  a color, given as an rgb triple as before, or a string giving an image filename.)

2. Does not use the shell for user input. All user input is
  in the Tkinter GUI window.  But diagnostic info and the help message still
  comes to the shell.

3. Operators are applied by selecting them from a drop-down "combo" box
  and then clicking on the "Apply" button.

4. Does not require a separate file show_state_array.py

Last updated 17 Sept. 2019. --Steve Tanimoto

    """

# global variables for the problem and solving process:

STEP=0; DEPTH=0; OPERATORS=[]; CURRENT_STATE=None; STATE_STACK=[]
APPLICABILITY_VECTOR = []

problem_name = 'Missionaries3' # Default problem name. Edit or give a command-line parameter to change it.


def compute_applicability_vector():
    global CURRENT_STATE, APPLICABILITY_VECTOR
    APPLICABILITY_VECTOR = [op.is_applicable(CURRENT_STATE) for op in OPERATORS]  

def show_instructions():
  tkprint('''\nINSTRUCTIONS:\n
The current state of your problem session represents where you
are in the problem-solving process.  You can try to progress
forward by applying an operator to change the state.
To do this, type the number of an applicable operator.
The program shows you a list of what operators are 
applicable in the current state.

You can also go backwards (undoing a previous step)
by typing 'B'.  

If you reach a goal state, you have solved the problem,
and the computer will usually tell you that, but it depends
on what kind of problem you are solving.''')

'''      
def apply_one_op():
    """Populate a popup menu with the names of currently applicable
       operators, and let the user choose which one to apply."""
    currently_applicable_ops = applicable_ops(CURRENT_STATE)
    #print "Applicable operators: ",\
    #    map(lambda o: o.name, currently_applicable_ops)
    #print("Now need to apply the op")

def applicable_ops(s):
    """Returns the subset of OPERATORS whose preconditions are
       satisfied by the state s."""
    return [o for o in OPERATORS if o.is_applicable(s)]
'''
# Define the general infrastructure for visualizations.
import tkinter as tk
from tkinter import ttk

# PIL is from the Pillow package. Needed to convert jpg images to PhotoImages,
 # and for resizing images.
from PIL import Image as PIL_Image
from PIL import ImageTk as PIL_ImageTk

STATE_WINDOW = None
THE_CANVAS = None
CAPTION = None
LOWER_GUI_PART = None
ROOT = None

def initialize_tk(title="Tk_SOLUZION_Client3"):
  global ROOT, STATE_WINDOW, THE_CANVAS, CAPTION
  ROOT = tk.Tk()
  ROOT.title(title)
  STATE_WINDOW = tk.Frame(ROOT, width=VIS.WIDTH, height=VIS.HEIGHT+200)
  STATE_WINDOW.pack()
  THE_CANVAS = tk.Canvas(STATE_WINDOW, width=VIS.WIDTH, height=VIS.HEIGHT)
  THE_CANVAS.pack()
  CAPTION = tk.Label(STATE_WINDOW, text="caption goes here")
  CAPTION.pack()
  print("Generic VIS initialization finished")

class State_array:

  def __init__(self, color_array=[], string_array=None, column_headers=[],
               column_footers=[],row_labels_left=[],row_labels_right=[],
               text_color="white",
               text_font=None,
               background=(128,128,128),
               caption="Current State"):
    self.color_array=color_array
    self.string_array=string_array
    self.column_headers=column_headers
    self.column_footers=column_footers
    self.row_labels_left=row_labels_left
    self.row_labels_right=row_labels_right
    self.text_color=text_color
    self.text_font=text_font
    self.background=background
    self.caption=caption
    self.ncols = len(self.color_array[0])
    self.nrows = len(self.color_array)

  def show(self):
    global STATE_WINDOW, THE_CANVAS, LOWER_GUI_PART, CAPTION
    print("In State_array.show()")
    # Clear away any stuff from showing the last state.  This avoids
    # what would otherwise be a memory leak, in which more and more
    # rectangles, text objects, and images get piled on top of those
    # from previous states.
    THE_CANVAS.delete("all")

    # Now create the rectangles, canvas images, strings for the current state.
    x0 = 0; y0 = 0;
    sww = VIS.WIDTH # state window width.
    swh = VIS.HEIGHT
    cellw = sww / self.ncols # cell width
    cellh = swh / self.nrows
    i = 0
    for r in self.color_array:
      j = 0
      for c in r:
        if type(c)==type('foo.jpg'):
            img = get_photo_image(c, cellw, cellh)
            THE_CANVAS.create_image((x0+j*cellw, y0+i*cellh), image=img,\
                                    anchor=tk.NW)
        else:
            tk_rgb = "#%02x%02x%02x" % c
            THE_CANVAS.create_rectangle(x0+j*cellw, y0+i*cellh,
                                                 x0+(j+1)*cellw, y0+(i+1)*cellh,
                                                 fill=tk_rgb)
        if self.string_array:
          THE_CANVAS.create_text(x0+(j+0.5)*cellw, y0+(i+0.5)*cellh,
                                          text=self.string_array[i][j],
                                          fill=self.text_color,
                                          font=self.text_font)
        j += 1
      i += 1
    CAPTION.config(text=self.caption)

PHOTOIMAGES = {}
def get_photo_image(filename, w, h):
    '''See if a PhotoImage has already been created for this filenam.
    If so, return that.  Otherwise, use PIL to load it, resize it,
    and make a PhotoImage out of it. Cache it in a dict. '''
    try:
        img = PHOTOIMAGES[filename]
        return img
    except:
        try:
          w = int(w); h = int(h) # make sure these are not floats.
          non_photoimage = (PIL_Image.open(filename)).resize((w,h))
          photoimage = PIL_ImageTk.PhotoImage(non_photoimage)
          PHOTOIMAGES[filename]=photoimage
          return photoimage
        except Exception as e:
          print("Error while trying to load an image named: "+filename)
          print(e)

  
CHOICE = None
class lower_gui_part(tk.Frame):
  def __init__(self, parent):#, width=300, height=300):
    tk.Frame.__init__(self, parent)
    self.pack()
    self.parent=parent
    self.label2 = tk.Label(self,  text="List of applicable operators")
    self.label2.pack(padx=20, pady=20)
    self.combo = ttk.Combobox(self, width=50,
                            values=[
                                    "0: January", 
                                    "1: February",
                                    "2: March",
                                    "3: April",
                                    "H: Help",
                                    "B: Back",
                                    "Q: Quit"]) # These particular values are very temporary.
    self.combo.pack()
    global CHOICE; CHOICE=self.combo
    self.gobutton = tk.Button(self, text="Apply", command=self.apply)
    self.gobutton.pack()

  def get_choice(self):
    chosen_item = self.combo.get()
    #print("Selected item is: "+chosen_item)
    return chosen_item
      
  def apply(self):
    #print("In the new apply method.")
    item = self.get_choice()
    parts = item.split(":") # The take_turn function only needs the
                            # operator number or 'code' before the colon.
    take_turn(parts[0])

  def update_choices(self):
    "This makes sure that only legal operators (for the current state) are shown in the combo box."
    global APPLICABILITY_VECTOR, OPERATORS
    new_values = [(str(i)+": "+OPERATORS[i].name)  for i in range(len(OPERATORS)) if APPLICABILITY_VECTOR[i]]
    new_values += ["H: Help", "B: Back", "Q: Quit"]
    self.combo.configure(values=new_values)

LOWER_GUI_PART = None    
def take_turn(command):
    global CURRENT_STATE, STATE_STACK, DEPTH, STEP, OPERATORS, APPLICABILITY_VECTOR
    global ROOT, LOWER_GUI_PART
    #print("In take_turn, command is: "+command)
    if command=="B" or command=="b": 
      if len(STATE_STACK)>1:
        STATE_STACK.pop()
        DEPTH -= 1
        STEP += 1
      else:
        tkprint("You're already back at the initial state.")
        return
      CURRENT_STATE = STATE_STACK[-1]
      PROBLEM.render_state(CURRENT_STATE)
      return

    if command=="H" or command=="h": show_instructions(); return
    if command=="Q" or command=="q": ROOT.destroy()
    if command=="": return
    try:
      i = int(command)
    except:
      tkprint("Unknown command or bad operator number.")
      return
    tkprint("Operator "+str(i)+" selected.")
    if i<0 or i>= len(OPERATORS):
      tkprint("There is no operator with number "+str(i))
      return
    if APPLICABILITY_VECTOR[i]:
       CURRENT_STATE = OPERATORS[i].apply(CURRENT_STATE)
       STATE_STACK.append(CURRENT_STATE)
       PROBLEM.render_state(CURRENT_STATE)
       compute_applicability_vector()
       LOWER_GUI_PART.update_choices()
       DEPTH += 1
       STEP += 1
       return
    else:
       tkprint("Operator "+str(i)+" is not applicable to the current state.")
       return
    #print("Operator "+command+" not yet supported.")

def tkprint(txt): print(txt) # Could be changed to render text on the GUI.

# The following is only executed if this module is being run as the main
# program, rather than imported from another one.
if __name__ == '__main__':
  # Now import the problem formulation and the problem-specific visualization stuff.

  import sys, importlib.util

  # Get the PROBLEM name from the command-line arguments

  if len(sys.argv)<2:
    """ The following few lines go with the LINUX version of the text client.
    print('''
         Usage: 
  ./IDLE_Text_SOLUZION_Client <PROBLEM NAME>
         For example:
  ./IDLE_Text_SOLUZION_Client Missionaries
    ''')
    exit(1)
    """
    sys.argv = ['Tk_SOLUZION_Client3.py', problem_name] # IDLE and Tk version only.
    # Sets up sys.argv as if it were coming in on a Linux command line.
    
  problem_name = sys.argv[1]
  print("problem_name = "+problem_name)

  try:
    spec = importlib.util.spec_from_file_location(problem_name, problem_name+".py")
    PROBLEM = spec.loader.load_module()
  except Exception as e:
    print(e)
    exit(1)

  try:
    print("Trying to import the vis file.")
    spec = importlib.util.spec_from_file_location(problem_name+'_VIS_FOR_TK3',
                                                  problem_name+'_VIS_FOR_TK3.py')
    VIS = spec.loader.load_module()
    
  except Exception as e:
    print(e)
    exit(1)

  OPERATORS=PROBLEM.OPERATORS
  STATE_STACK = []
  TITLE="Tk_SOLUZION_Client (Version 3)"

  CURRENT_STATE = PROBLEM.State()  
  STATE_STACK = [CURRENT_STATE]
  compute_applicability_vector()

  try:
    print("Trying to initialize the visualization")
    PROBLEM.render_state = VIS.render_state
    initialize_tk()
    VIS.initialize_vis(STATE_WINDOW,State_array, CURRENT_STATE)
    LOWER_GUI_PART = lower_gui_part(STATE_WINDOW)
    LOWER_GUI_PART.update_choices()
  except Exception as e:
    print("Could not initialize the visualization.")
    print(e)

  STATE_WINDOW.mainloop() # This lets Tk take over the event loop, show graphics, etc.
  print("The session is finished.")
