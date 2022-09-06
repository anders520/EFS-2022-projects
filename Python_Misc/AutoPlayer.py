#!/usr/bin/python3
"""AutoPlayer.py
  derived from Tk_SOLUZION_Client.py
 This file implements an automatic player for a game or
 problem that is in SOLUZION format. 


    """

# The following line is used in the Tk_SOLUZION_Client and the IDLE_Text_SOLUZION_Client.
problem_name = 'Missionaries2'
policy_is_set = True  # Chance this to False if you want the player to prompt the user to set the mode.
MODE = 0 # Default mode is random moves.

STEP_LIMIT = -1 # no step limit if negative
WAIT_TIME_PER_MOVE = 1.0

print("\nWelcome to the AutoPlayer for SOLUZION!")
print("The problem, puzzle or game is: "+problem_name+"\n\n")

def set_policy():
  global MODE
  answer = input('''Select a policy for making moves.
0. Random
1. First legal move
2. Last legal move
Enter 0, 1, or 2: >> ''')
  try:
    MODE = int(answer)
    if MODE < 0 or MODE > 2:
       print("Illegal mode number. Using 0 (random).")
       MODE = 0
  except:
    print("Illegal mode number. Using 0 (random).")


import random, time
def player_mainloop():
  global policy_is_set
  print(TITLE)
  print(PROBLEM.PROBLEM_NAME+"; "+PROBLEM.PROBLEM_VERSION)
  global STEP, OPERATORS, CURRENT_STATE
  CURRENT_STATE = PROBLEM.copy_state(PROBLEM.INITIAL_STATE)  



  STEP = 0

  PROBLEM.render_state(CURRENT_STATE)
  if not policy_is_set:
    set_policy()
    policy_is_set = True
  while(True):
    print("\nStep "+str(STEP))
    #print("CURRENT_STATE = "+str(CURRENT_STATE))
    if PROBLEM.goal_test(CURRENT_STATE):
      print('''CONGRATULATIONS!
You have solved the problem by reaching a goal state.'
''')
      time.sleep(4*WAIT_TIME_PER_MOVE)
      print("Starting a new game...")
      CURRENT_STATE = PROBLEM.copy_state(PROBLEM.INITIAL_STATE)  

    applicability_vector = get_applicability_vector(CURRENT_STATE)
    #print("applicability_vector = "+str(applicability_vector))
    for i in range(len(OPERATORS)):
      if applicability_vector[i]:
        print(str(i)+": "+OPERATORS[i].name)
    legal_op_numbers = list(filter(lambda i:applicability_vector[i], range(len(OPERATORS))))
    if MODE==0:
       command = random.choice(legal_op_numbers)
    elif MODE==1:
      command = legal_op_numbers[0]
    elif MODE==2:
      command = legal_op_numbers[-1]

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
       PROBLEM.render_state(CURRENT_STATE)
       STEP += 1
       time.sleep(WAIT_TIME_PER_MOVE)
       continue
    else:
       print("Operator "+str(i)+" is not applicable to the current state.")
       continue
    #print("Operator "+command+" not yet supported.")

def get_applicability_vector(s):
    #print("OPERATORS: "+str(OPERATORS))
    return [op.is_applicable(s) for op in OPERATORS]  
      
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
TITLE="AutoPlayer_for_SOLUZION (Version 0-1)"

import threading
class AutoPlayer(threading.Thread):
  def __init__(self, tk_root):
    self.root = tk_root
    threading.Thread.__init__(self)
    self.start()

  def run(self):
    player_mainloop()
    self.root.quit()
    exit(0)
    #self.root.update()
  
# The following is only executed if this module is being run as the main
# program, rather than imported from another one.
if __name__ == '__main__':
  import show_state_array
  player = AutoPlayer(show_state_array.STATE_WINDOW)
  show_state_array.STATE_WINDOW.mainloop()
  print("The session is finished.")
