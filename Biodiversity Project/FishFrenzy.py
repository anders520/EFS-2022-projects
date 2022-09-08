#<METADATA>
SOLUZION_VERSION = "0.2"
PROBLEM_NAME = "FishFrenzy"
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
        self.codNum = 100
        self.herringNum = 100
        self.roundsLeft = 12
        self.biodiversityIndex = 1
        
        if not old is None:
            self.biodiversityScore = old.biodiversityScore
            self.biodiversityIndex = old.biodiversityIndex
            self.money = old.money
            self.codNum = old.codNum
            self.herringNum = old.herringNum
            self.roundsLeft = old.roundsLeft


    def can_move(self, method):
        if method != 0 and self.codNum <= 0 and self.herringNum <= 0:
            return False
        return True
    

    def move(self, method):
        #Creates a new state if it is legal
        newState = State(old=self) # Make a copy of the current state.
        self.roundsLeft -= 1
        newState.roundsLeft = self.roundsLeft
        fish1Caught = 0
        fish2Caught = 0
        if method == 1:
          fish1Caught = r.randint(20, 30)
          fish2Caught = r.randint(20, 30)
        
        fish1inOcean = max(self.codNum - fish1Caught, 0)
        fish2inOcean = max(self.herringNum - fish2Caught, 0)
        profit = ((self.codNum - fish1inOcean) * 10 + (self.herringNum - fish2inOcean) * 8)
        fish1inOcean = int(fish1inOcean * 1.25)
        fish2inOcean = int(fish2inOcean * 1.25)
        newState.codNum = fish1inOcean
        newState.herringNum = fish2inOcean
        
        #Calculation of Simpson's Diversity Index
        N = (fish1inOcean + fish2inOcean)
        nSum = fish1inOcean * (fish1inOcean - 1) + fish2inOcean * (fish2inOcean - 1)
        if N > 1:
          newState.biodiversityIndex = 1 - round(nSum / (N * (N-1)), 3)
        else:
          newState.biodiversityIndex = 1.0 - 0
        
        fishList = [fish1inOcean, fish2inOcean]
        speciesLeft = len(fishList)
        scoreMultiplier = (100.0 / speciesLeft)
        for f in fishList:
          if f == 0:
            speciesLeft -= 1
        newState.biodiversityScore = (1 - newState.biodiversityIndex) * speciesLeft * scoreMultiplier
        newState.money += profit
        return newState

    def describe_state(self):
        return

    def is_goal(self):
        if self.roundsLeft == 0:
          return True
        return False
    
    def __eq__(self, s2):
        if s2==None: return False
        if self.money != s2.money: return False
        if self.biodiversityScore != s2.biodiversityScore: return False
        if self.biodiversityIndex != s2.biodiversityIndex: return False
        if self.codNum != s2.codNum: return False
        if self.herringNum != s2.herringNum: return False
        return True

    def __str__(self):
      currentState = '(Profit: '+str(self.money)
      currentState += ', Biodiversity Index: '+str(self.biodiversityIndex)
      currentState += ', Biodiversity Score: '+str(self.biodiversityScore)
      currentState += ', cod left: '+str(self.codNum)
      currentState += ', herring left: '+str(self.herringNum)+')'
      return currentState

    def __hash__(self):
      return (str(self)).__hash__()
    
    def goal_message(self):
      return "You have completed the game!"

def copy_state(s):
  return State(old=s)

class Fish:
  def __init__(self, price, repRate):
    self.price = price
    
#tuna costs $1200
#salmon costs $750
#cod costs $75
#pompano costs $10
#halibut costs $6000
#Striped bass costs $480
salmon = Fish(750, 1)
tuna = Fish(1200, 1)
cod = Fish(75, 1)
pompano = Fish(10, 1)
stripedBass = Fish(480, 1)
halibut = Fish(6000, 1)

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
phi0 = Operator("Do nothing",
  lambda s: s.can_move(0),
  lambda s: s.move(0))

phi1 = Operator("Using a net for more than one fish species",
  lambda s: s.can_move(1),
  lambda s: s.move(1))

OPERATORS = [phi0, phi1]
#</OPERATORS>