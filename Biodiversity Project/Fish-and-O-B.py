#<METADATA>
SOLUZION_VERSION = "0.2"
PROBLEM_NAME = "Fish-and-O-B"
PROBLEM_VERSION = "1.0"
AUTHORS = ['Anders C.', 'Dawson H.', 'Ren C.', 'Will Z.', 'Mason C.']
CREATION_DATE = "06-SEP-2022"
DESC = ""
#</METADATA>

#<COMMON_CODE>
import random as r
class State:
    def __init__(self, old=None):
        self.biodiversityScore = 100
        self.money = 0
        self.fish1Num = 100
        self.fish2Num = 100
        if not old is None:
            self.biodiversityScore = old.biodiversityScore
            self.money = old.money
            self.fish1Num = old.fish1Num
            self.fish2Num = old.fish2Num


    def can_move(self, fish1, fish2):
        return True
    

    def move(self,fish1,fish2, method):
        #Creates a new state if it is legal
        newState = State(old=self) # Make a copy of the current state.
        if method == 0:
          fish1inOcean = max(self.fish1Num - r.randint(20, 30), 0)
          fish2inOcean = max(self.fish2Num - r.randint(20, 30), 0)
        '''fish1inOcean = max(self.fish1Num - fish1, 0)
        fish2inOcean = max(self.fish2Num - fish2, 0)'''
        newState.fish1Num = fish1inOcean
        newState.fish2Num = fish2inOcean
        return newState

    def describe_state(self):
        return

    def is_goal(self):
        if self.fish1Num > 0 and self.fish2Num > 0:
          return False
        return True
    
    def __eq__(self, s2):
        if s2==None: return False
        if self.money != s2.money: return False
        if self.biodiversityScore != s2.biodiversityScore: return False
        if self.fish1Num != s2.fish1Num: return False
        if self.fish2Num != s2.fish2Num: return False
        return True

    def __str__(self):
      currentState = '('+str(self.money)
      currentState += ','+str(self.biodiversityScore)
      currentState += ','+str(self.fish1Num)
      currentState += ','+str(self.fish2Num)+')'
      return currentState

    def __hash__(self):
      return (str(self)).__hash__()

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
  lambda s: s.can_move(25, 25),
  lambda s: s.move(r.randint(20, 30), r.randint(20, 30), 0))

OPERATORS = [phi0]
#</OPERATORS>