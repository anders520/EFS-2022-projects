#!/usr/bin/python3
"""Text_SOLUZION_Client.py
 This file implements a simple "SOLUZION" client that
 permits a user ("problem solver") to explore a search tree
 for a suitably-formulated problem.  The user only has to
 input single-character commands to control the search.
 Output is purely textual, and thus the complexity of a
 graphical interface is avoided.

 This client runs standalone -- no server connection.
 It thus provides a bare-bones means of testing a problem
 formulation.

Updated Sept. 2, to work from IDLE, with a fixed problem
 formulation (Missionaries). You can replace that name as needed
 for other problem formulations.
 
 Updated Sept. 1, 2020 to be compatible with the latest
version of Missionaries.py (Sept. 1, 2020 version).
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


def mainloop():
  print(TITLE)
  print(PROBLEM.PROBLEM_NAME+"; "+PROBLEM.PROBLEM_VERSION)
  global STEP, DEPTH, OPERATORS, CURRENT_STATE, STATE_STACK
  CURRENT_STATE = PROBLEM.copy_state(PROBLEM.INITIAL_STATE)  

  STATE_STACK = [CURRENT_STATE]
  STEP = 0
  DEPTH = 0
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
      CURRENT_STATE = STATE_STACK[-1]
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
  problem_name = "Biodiversity Project\FishFrenzy" # Change this, e.g., for FarmerFox.
#  
#  print('''
#       Usage: 
#./Text_SOLUZION_Client <PROBLEM NAME>
#       For example:
#./Text_SOLUZION_Client Missionaries
#  ''')
#  exit(1)
#  
#problem_name = sys.argv[1]
print("problem_name = "+problem_name)

try:
  spec = importlib.util.spec_from_file_location(problem_name, problem_name+".py")
  PROBLEM = spec.loader.load_module()
  spec.loader.exec_module(PROBLEM)
except Exception as e:
  print(e)
  exit(1)

#  import Mondrian as PROBLEM

OPERATORS=PROBLEM.OPERATORS
STATE_STACK = []
TITLE="Text_SOLUZION_Client (Version 0-4)"
      
# The following is only executed if this module is being run as the main
# program, rather than imported from another one.
if __name__ == '__main__':
  mainloop()
  print("The session is finished.")
