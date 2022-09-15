#<METADATA>
SOLUZION_VERSION = "0.2"
PROBLEM_NAME = "FishFrenzy"
PROBLEM_VERSION = "0.1"
AUTHORS = ['Anders C.', 'Dawson H.', 'Ren C.', 'Will Z.', 'Mason C.']
CREATION_DATE = "06-SEP-2022"
DESC = ""
#</METADATA>

#<COMMON_CODE>
import random as r
class State:
    def __init__(self, old=None):
        self.codNum = 100
        self.herringNum = 100
        self.roundsLeft = 12
        
        if not old is None:
            self.codNum = old.codNum
            self.herringNum = old.herringNum
            self.roundsLeft = old.roundsLeft


    def can_move(self, method):
        return True
    

    def move(self, method):
        #Creates a new state if it is legal
        newState = State(old=self) # Make a copy of the current state.
        newState.roundsLeft = self.roundsLeft - 1
        if method == 1:  
          fish1Caught = 25
          fish2Caught = 25
        else:
          fish1Caught = 0
          fish2Caught = 0
        fish1inOcean = max(self.codNum - fish1Caught, 0)
        fish2inOcean = max(self.herringNum - fish2Caught, 0)
        newState.codNum = fish1inOcean
        newState.herringNum = fish2inOcean

        return newState

    def describe_state(self):
        return

    def is_goal(self):
        if self.roundsLeft == 0 or (self.codNum == 0 and self.herringNum == 0):
          return True
        return False
    
    def __eq__(self, s2):
        if s2==None: return False
        if self.codNum != s2.codNum: return False
        if self.herringNum != s2.herringNum: return False
        return True

    def __str__(self):
      currentState = '(cod left: '+str(self.codNum)
      currentState += ', herring left: '+str(self.herringNum)+')'
      return currentState

    def __hash__(self):
      return (str(self)).__hash__()
    
    def goal_message(self):
      return "You have completed the game!"

def copy_state(s):
  return State(old=s)

class Operator:
  def __init__(self, name, precond, state_transf):
    self.name = name
    self.precond = precond
    self.state_transf = state_transf

  def is_applicable(self, s):
    return self.precond(s)

  def apply(self, s):
    return self.state_transf(s)
#</COMMON_CODE>

#<INITIAL_STATE>
INITIAL_STATE = State()
#</INITIAL_STATE>

#<OPERATORS>
phi0 = Operator("Using a net for more than one fish species",
  lambda s: s.can_move(1),
  lambda s: s.move(1))

OPERATORS = [phi0]
#</OPERATORS>