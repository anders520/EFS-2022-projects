#!/usr/bin/python3
"""Tk_SOLUZION_Client.py
 This file implements a simple "SOLUZION" client that
 permits a user ("problem solver") to explore a search tree
 for a suitably-formulated problem.  The user only has to
 input single-character commands to control the search.
 Output is purely textual, and thus the complexity of a
 graphical interface is avoided.

 This client runs standalone -- no server connection.
 It thus provides a bare-bones means of testing a problem
 formulation.

 Tk is the graphics and GUI Toolkit that ships with Python.
 This client program uses Tk only for its graphics, setting up
 a graphics window that is used for the display of each state
 of the problem-solution process.

 To take advantage of this, the problem formulation file should
 check to see if the global USE_TK_GRAPHICS is True, and if so, it
 should import a visualization file with a name similar to:
 Missionaries_Array_VIS_FOR_TK.py.

 One technical challenge in creating this client is that Tk graphics
 requires that the main execution thread be devoted to Tk,
 which means that a normal text-input loop cannot easily be
 sync'd with Tk.  The solution is to use a separate thread for
 the text loop and have it make calls re-draw the Tk graphic.
 Tk still runs the mainloop method in the main thread, which
 not only is there to handle any GUI events (but there are not any
 in this program) but also just to show the graphics window.
 If we don't call the mainloop method, the Tk graphic window
 will not show up until the rest of the program completely
 finishes, which is useless.  So there is a separate thread
 here for the user interaction loop.

 Status: Started on Aug. 2.
   Aug. 3. Basic array graphics is working. But now we
   need the strings and advanced options.
   
   Need example file Missionaries_Array_VIS_FOR_TK.py.
   Need code to display a color array, with defaults if anything
      is not provided.
   Need code to display a corresponding string array.
      consider options to include column headers, footers, and
      row titles on left and right.
   Add caption feature.
   The file for these features:  show_state_array.py

----

PURPOSE OF THIS MODULE:
        
    This module supports what we can call "interactive state
    space search".  Whereas traditional search algorithms in the
    context of artificial intelligence work completely automatically,
    this module lets the user make the moves.  It provides support
    to the user in terms of computing new states, displaying that
    portion of the state space that the user has embodied, and
    providing controls to permit the user to adapt the presentation
    to his or her needs.  This type of tool could ultimately be a
    powerful problem solving tool, useful in several different
    modes of use: interactive processing of individual objects,
    programming by demonstration (the path from the root to any
    other node in the state space represents a way of processing
    any object similar in structure to that of the root object.)

    """

# The following line is used in the Tk_SOLUZION_Client and the IDLE_Text_SOLUZION_Client.
problem_name = 'Missionaries'

def client_mainloop():
  print(TITLE)
  print(PROBLEM.PROBLEM_NAME+"; "+PROBLEM.PROBLEM_VERSION)
  global STEP, DEPTH, OPERATORS, CURRENT_STATE, STATE_STACK
  CURRENT_STATE = PROBLEM.copy_state(PROBLEM.INITIAL_STATE)  

  STATE_STACK = [CURRENT_STATE]
  STEP = 0
  DEPTH = 0
  PROBLEM.render_state(CURRENT_STATE)
  while(True):
    print("\nStep "+str(STEP)+", Depth "+str(DEPTH))
    print("CURRENT_STATE = "+str(CURRENT_STATE))
    if CURRENT_STATE.is_goal():
      print('''CONGRATULATIONS!
You have solved the problem by reaching a goal state.
Do you wish to continue exploring?
''')
      answer = input("Y or N? >> ")
      if answer=="Y" or answer=="y": print("OK, continue")
      else: return

    applicability_vector = get_applicability_vector(CURRENT_STATE)
    #print("applicability_vector = "+str(applicability_vector))
    for i in range(len(OPERATORS)):
      if applicability_vector[i]:
        print(str(i)+": "+OPERATORS[i].name)
    command = input("Enter command: 0, 1, 2, etc. for operator; B-back; H-help; Q-quit. >> ")
    if command=="B" or command=="b": 
      if len(STATE_STACK)>1:
        STATE_STACK.pop()
        DEPTH -= 1
        STEP += 1
      else:
        print("You're already back at the initial state.")
        continue
      CURRENT_STATE = STATE_STACK[-1]
      PROBLEM.render_state(CURRENT_STATE)
      continue

    if command=="H" or command=="h": show_instructions(); continue
    if command=="Q" or command=="q": break
    if command=="": continue
    try:
      i = int(command)
    except:
      print("Unknown command or bad operator number.")
      continue
    print("Operator "+str(i)+" selected.")
    if i<0 or i>= len(OPERATORS):
      print("There is no operator with number "+str(i))
      continue
    if applicability_vector[i]:
       CURRENT_STATE = OPERATORS[i].apply(CURRENT_STATE)
       STATE_STACK.append(CURRENT_STATE)
       PROBLEM.render_state(CURRENT_STATE)
       DEPTH += 1
       STEP += 1
       continue
    else:
       print("Operator "+str(i)+" is not applicable to the current state.")
       continue
    #print("Operator "+command+" not yet supported.")

def get_applicability_vector(s):
    #print("OPERATORS: "+str(OPERATORS))
    return [op.is_applicable(s) for op in OPERATORS]  

def exit_client():
  print("Terminating Text_SOLUZION_Client session.")
  log("Exiting")
  exit()
  

def show_instructions():
  print('''\nINSTRUCTIONS:\n
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
      
def apply_one_op():
    """Populate a popup menu with the names of currently applicable
       operators, and let the user choose which one to apply."""
    currently_applicable_ops = applicable_ops(CURRENT_STATE)
    #print "Applicable operators: ",\
    #    map(lambda o: o.name, currently_applicable_ops)
    print("Now need to apply the op")

def applicable_ops(s):
    """Returns the subset of OPERATORS whose preconditions are
       satisfied by the state s."""
    return [o for o in OPERATORS if o.is_applicable(s)]

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
  sys.argv = ['Tk_SOLUZION_Client.py', problem_name] # IDLE and Tk version only.
  # Sets up sys.argv as if it were coming in on a Linux command line.
  
problem_name = sys.argv[1]
print("problem_name = "+problem_name)

try:
  spec = importlib.util.spec_from_file_location(problem_name, problem_name+".py")
  PROBLEM = spec.loader.load_module()
  spec.loader.exec_module(PROBLEM)
except Exception as e:
  print(e)
  exit(1)

try:
  spec = importlib.util.spec_from_file_location(problem_name+'_Array_VIS_FOR_TK',
                                                problem_name+'_Array_VIS_FOR_TK.py')
  VIS = spec.loader.load_module()
  spec.loader.exec_module(VIS)
  print("Using TK vis routine")
  PROBLEM.render_state = VIS.render_state
  VIS.initialize_vis()
except Exception as e:
  print(e)
  exit(1)


OPERATORS=PROBLEM.OPERATORS
STATE_STACK = []
TITLE="Tk_SOLUZION_Client (Version 0-1)"

import threading
class Client(threading.Thread):
  def __init__(self, tk_root):
    self.root = tk_root
    threading.Thread.__init__(self)
    self.start()

  def run(self):
    client_mainloop()
    self.root.quit()
    exit(0)
    #self.root.update()
  
# The following is only executed if this module is being run as the main
# program, rather than imported from another one.
if __name__ == '__main__':
  import show_state_array
  client = Client(show_state_array.STATE_WINDOW)
  show_state_array.STATE_WINDOW.mainloop()
  print("The session is finished.")
